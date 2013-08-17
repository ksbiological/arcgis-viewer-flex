Decoupling the web maps from Django
===================================

At some point, KBS may decide to fully transition away from a Django installation. At that time, if KBS is to continue using the web maps, it must decouple them from Django. Nearly all installations of the Esri's ArcGIS Viewer for Flex work without Django; the Django integration was added at KBS to reduce redundancy in the web map configuration files.

There should be no visible difference to consumers of the flex viewer from decoupling the web maps from Django. The primary difference is that internally, each map will have a single map configuration XML file, which would wholly and completely define the configuration for that web map, instead of inheriting from a base configuration file and overriding portions of it.

The web maps are coupled to Django in the following ways:

* The web map configuration files currently use Django template tags and some template variables.
* The web pages which load the web maps are served by Django.

  * The URLs (e.g. ``/maps/sgpchat/``) get handled by Django.
  * The HTML responses are rendered by Django from the ``kbsdjango/templates/map.html`` template of the ``kbsdjango`` project instead of ``viewer/index.html`` (which is generated from ``html-template/index.template.html`` in the ``flexviewer`` repository.) ``kbsdjango/templates/map.html`` is a slightly-modified version of ``viewer/index.html``:

    * The page title is set dynamically depending on which map is being requested.
    * The location of the configuration XML file to use is set dynamically depending on which map is being requested.
    * The Google Analytics ID is set dynamically depending on which site the map is being viewed on (e.g. ``kars.ku.edu``, ``kbs.ku.edu``, etc.)

      * Note that the KARS Google Analytics code has been added to ``html-template/index.template.html`` in the ``flexviewer`` repository, so the analytics code should appear in ``viewer/index.html`` and should still work for maps on the KARS website even after the maps have been decoupled from Django.

    * The absolute URLs of ``viewer/swfobject.js`` and ``viewer/index.swf`` are hardcoded (e.g. to ``http://kars.ku.edu/media/viewer/swfobject.js`` and ``http://kars.ku.edu/media/viewer/index.swf``, if on the KARS website.)

* Web maps are assciated with (and pull some data from) the Django ``Map`` model defined in the ``kbsdjango`` project.

To decouple the web maps from Django:

* Export the latest version of each web map configuration file. This involves copying the rendered version of the configuration file (e.g. the file served after all of Django's templating tags have been applied and the template variables have been substituted in.) For a web map served at e.g. http://kars.ku.edu/maps/sgpchat/, the fully-rendered configuration file is served at http://kars.ku.edu/maps/sgpchat/config.xml. Save rendered versions of the configuration files to a folder, and name them each according to the application slug used for the map. For example, http://kars.ku.edu/maps/sgpchat/config.xml should be saved as ``sgpchat.xml``.
* Configure Apache to serve the web maps. Some URL rewriting needs to occur in order for the web maps to stay available at the same URLs. Basically, the viewer will be located in a folder called ``viewer``. The configuration files will be saved in a folder called, for example, ``map-configs``.
* The web maps are served at http://kars.ku.edu/maps/APP_SLUG/, where "APP_SLUG" is the URL-friendly "application slug" associated with the web map. These "slugs" should consist of lowercase letters and may contains hyphens in between words to improve readibility. Requests to http://kars.ku.edu/maps/APP_SLUG/ need to be served the contents of the ``viewer`` folder. Assuming the ``viewer`` folder is located inside of a ``media`` folder of static media which is made publicly availabe at http://kars.ku.edu/media/, and assuming the ``map-configs`` folder is located inside ``viewer``, make each ``/map/APP_SLUG/`` directory serve the contents of ``/media/viewer/``, with the exception that requests made to ``/map/APP_SLUG/config.xml`` should be served the contents of ``/media/viewer/map-configs/APP_SLUG.xml``.

After this decoupling has occurred, the web maps will load everything from their configuration XML. That means that if Django is still used, changes made to ``Map`` objects in the Django admin site will not be automatically applied to the web maps. For example, if you change a map's title in the Django administration site, you must also change it in the web map configuration XML in order for the title to appear differently when browsing the actual web map.
