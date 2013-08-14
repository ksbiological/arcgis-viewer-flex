Creating and editing web maps
=============================

The Kansas Biological Survey publishes online mapping applications (*web maps*) that provide in-browser interaction with some of the Survey's geodata. The Survey's web maps are powered by the KBS Map Viewer, which is an Adobe Flex application that is developed using the ArcGIS Viewer for Flex as a base. 

A web map consists of a configuration XML file, and a ``Map`` object in the Survey's django-powered website's database.

How to create a web map
-----------------------

 #. Add a ``Map`` object using the django administration site on the development server. The map's *app slug* determines the URL on which the web map will be available.
 #. Create the web map's configuration XML file at ``\\YORKTOWN\map-configs\[app_slug].xml`` (replace ``[app_slug]`` with the contents of the ``app slug`` field of the associated map object.) You may optionally copy the contents of an existing web map's configuration file into the newly-created file to serve as a starting point. In the configuration file, specify the applications' services and/or layers, as well as any other customizations (extra header links or widgets, etc.)
 #. *(Recommended)* Change the encoding of the configuration file to UTF-8. In Notepad++, this can be done through the 'Encoding' menu item (choose the 'Encode in UTF-8' option.)
 #. Test the application, which is at the URL ``http://sandbox.kars.ku.edu/maps/[app_slug]``. Make changes as necessary until it is ready for deployment.
 #. Copy the working configuration file to ``/srv/webgis/templates/map-configs/`` on *gremlin-vm*.
 #. Recreate the associated map object from the development server in the django administration site on the production site. Select *app published*.
 #. *If migrating the web map from .NET:* Remove the proxy pass lines to and from ``/[app_slug]`` and ``/maps/[app_slug]`` in the *proxies* apache configuration file, and add a redirect from ``/[app_slug]`` to ``/maps/[app_slug]`` in the KARS apache configuration file. ``sudo apache2ctl graceful`` will restart the server (may take a few seconds) and implement the new configuration files.

Writing the configuration XML file
----------------------------------

The primary reference for the structure of configuration file is on ESRI's website `here <http://help.arcgis.com/en/webapps/flexviewer/help/index.html>`_ (In the sidebar, click on 'Configure the Viewer', and then 'Main configuration file' to get the the correct page.)

The KBS Map Viewer adds a layer of processing to the configuration XML file system used in ESRI's ArcGIS Viewer for Flex 2.2; configuration files are rendered through django's template system. This enables applications to inherit from a base XML configuration file containing code that is common to all of the Survey's web maps. Information from the base configuration file can then be extended or overwritten as needed by individual web map configuration files. 

However, this also means those who will be working with the Survey's web map configuration files may benefit from learning some of the fundamentals of django's templating system. Django's own documentation has a page about that `here <http://docs.djangoproject.com/en/1.2/topics/templates/>`_. The introduction and the `template inheritance <http://docs.djangoproject.com/en/1.2/topics/templates/#template-inheritance>`_ section cover the importance concepts.

Review existing web map configuration XML files for examples of how django's templating system is applied.
