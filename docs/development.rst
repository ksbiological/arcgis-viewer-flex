Viewer development
==================

The viewer's files are in a version-controlled folder at ``\\groups2.home.ku.edu\KBS_General\web_site\code\flexviewer``.

Reminder: Read Esri's documentation
-----------------------------------

Esri publishs extensive, helpful documentation about its ArcGIS Viewer for Flex. Esri's documentation is located in the "Concepts" section of `Esri's ArcGIS Viewer for Flex Community <http://resources.arcgis.com/en/communities/flex-viewer/>`. KBS' documentation focuses on our modifications to the viewer; Esri's documentation is highly recommended and should be used as a primary reference.

Overview of KBS' changes
------------------------

The primary changes made by KBS to the viewer are:

* We updated the label of the layer list to be "Layers" instead of "More...".
* We customized the label of the button on the Splash widget.
* We made it possible to specify the geometryservice to use in the overall map configuration XML instead of in the widget configuration XML.
* We made it possible to remove certain layers from the table of contents by specifying the layer names in an "excludelayers" element in the map configuration XML.
* We wrote our own About widget which lists the map description, disclaimer, and copyright information after loading that data from the map configuration XML.
* We are using a third-party Identify widget (one is not provided in the ArcGIS Viewer for Flex) to provide Identify capabilities.
* We are using a third-party MapProgressBar widget to show a "Loading..." bar to users when waiting on ArcGIS for Server to update the map.
* We extended the Locate widget to create "Zoom to PLSS" functionality.
* We customized the TOC to be click-based instead of timer-based. By default in the ArcGIS Viewer for Flex, the TOC expands when you roll over the "More..." label and retracts after a certain amount of time, if your mouse is no longer on the TOC. We changed this to require explicitly clicking the TOC layers button to expand or retract the TOC.
* We made the TOC pane resizable. This required non-trivial modifications.

How to get started
------------------

1. Install Adobe Flash Builder 4.6 (the previous student developer, Patrick, used a free student/educational license. As a student or educator, you can probably do the same.)
2. Map the GBS_General network share to a drive on your Windows machine.
3. In Flash Builder, select "File > Import Flash Builder Project". Select the 'flexviewer' folder (e.g. ``web_site\code\flexviewer`` inside of your mapped network drive.) Click "Finish".

You should now be able to administer the flex viewer project from within Flash Builder.

Widgets
-------

ESRI's ArcGIS Viewer for Flex 3.4 uses components called *widgets* to provide functionality in their viewer. KBS' version uses many of the included widgets without modification, and some that have been modified to meet the Survey's specifications. KBS' viewer also utilizes third-party widgets and a custom widget built from scratch.

How to add a widget
^^^^^^^^^^^^^^^^^^^

1. Copy the widget source code into the "src/widgets" directory of the source code.
2. In Flash Builder 4.6, go to "Project > Properties > Flex modules". Click "Add" to enable a module. Click "Browse" to browse the project source to find the .mxml file of the widget you want to enable. It will probably reside in "/src/widgets/" in a folder named after the widget.
3. Add the widget into the application configuration XML for whatever web map you are trying to add the widget to. Refer to ESRI's documentation for more details.
4. After you have added the module, just like any other time you update the viewer, you will need to export a release build of the viewer and copy it to the appropriate location on the server.

Custom Report Widget
^^^^^^^^^^^^^^^^^^^^^

The Custom Report widget is a custom tool enabling creation of printable data tables for applications configured for use with the widget.

The tool is activated by clicking on the appropriate icon in the widget bar. A user selects one of the shape selection options and draws a polygon. After drawing occurs, the draw tool turns off and the Flex application queries the associated service for records which intersect with the drawn polygon. It loads specified attributes into a data table in the widget, and links to a printable page generated by the KBS website.

The Custom Report widget is expected to be retired as part of the migration of KBS' websites to the KU CMS. Esri-developed widgets such as the Attribute Table widget, the Geoprocessing widget, and the Print widget replace functionality provided by the Custom Report widget.

Upgrading to a new version of the viewer
----------------------------------------

Esri releases new versions of the viewer from time to time. The source code is made available at `https://github.com/Esri/arcgis-viewer-flex/`.

It is possible to upgrade the viewer when a new version becomes available. For a programmer who is familiar with Git and with the code of the ArcGIS Viewer for Flex, it could take a few minutes. For someone who does not have much experience with Git or with the code of the viewer, it depends the changes made in the new version; it could take anywhere from an hour to several days, depending on how smoothly it goes. The main problem is if a new version of the viewer introduces changes that conflict with the modifications we have made here at the Survey. Merging the code and resolving those conflicts can be time-consuming to someone who does not do that kind of thing very frequently.

Someone familiar with Git should be able to upgrade the viewer by following this general process:

1. Make sure Git is installed and available on the command-line (this can be done on Windows with software such as Git for Windows.)
2. Make sure the 'develop' branch is checked out (run ``git branch --all`` on the command-line from inside the ``flexviewer`` folder and verify that an asterisk precedes the line that says "develop".)
3. Make sure all uncommitted changes in the ``flexviewer`` repository have been committed or stashed.
4. In the ``flexviewer`` folder, run ``git fetch esri``. This will pull Esri's updates to the local repository without updating the working directory.
5. Merge with the new Esri viewer version. For upgrading to version 3.4, the command used was ``git merge 3.4-src``.
6. If any merge conflicts occur (this is likely), resolve the conflicts and commit the merge. Be careful to resolve the conflicts appropriately! Don't allow custom KBS functionality to be removed (unless the removal is intentional), and make sure that the updates introduced in the new version of the viewer are all integrated to the maximum extent.

If these steps seem too technical, you may need to take some Git tutorials or have someone familiar with Git work with you to complete them. KU IT may be able to help; they use Git for some of their work.

Deploying the viewer
--------------------

In order for the changes you make in ``flexviewer`` to take effect on KBS' web maps, you must deploy the viewer. This process involves exporting a release build of the viewer from Flash Builder 4.6 and copying it to the appropriate location on the server. The release build contains the compiled .swf files which are necessary in order to load the web map in a browser. If you have made any changes to things in the currently-deployed viewer folder, you must copy over those changes to the ``flexviewer`` project beforehand, or the changes will be overwritten.

The hosted copy of the map viewer is located at ``\\Gremlin\media\viewer\``, or online at `http://kars.ku.edu/media/viewer/`. Remember that this is a copy of what is produced from the viewer source code when the project is built by Flash builder.

1. Verify that all changes made locally to the deployed viewer (at ``\\Gremlin\media\viewer\``) that you want to keep have been copied over to the ``flexviewer`` project. The ``flexviewer`` folder is the authoritative version of the project; the deployed viewer folder is an exported copy and changes made there will be lost upon redeployment of the server unless you bring them to ``flexviewer`` beforehand. You can use a tool such as WinMerge to compare two viewer folders (e.g. the currently-deployed one and the one you want to deploy) to more easily splot files that may have been changed in the currently-deployed viewer folder.
2. Delete the "bin-release" folder in the ``flexviewer`` project folder (it will be recreated in a later step.)
3. Export a release build of the viewer. In Flash Builder, select "Project > Export Release Build". The compiled viewer folder is saved as the "bin-release" folder inside the ``flexviewer`` project.
4. Delete the old viewer deployment folder, ``\\Gremlin\media\viewer\``, (or rename it to something else temporarily, until you are sure all of the local changes were successfully copied to ``flexviewer``.) Then copy ``bin-release`` into ``\\Gremlin\media\`` and rename the "bin-release" folder to "viewer".
5. Restart the Ubuntu virtual machine and clear the cache in your browser to make sure when you load the viewer again, it will load the updated version.

That is the basic process to make permanent changes to the viewer. Remember that local changes to the deployed viewer folder will be overwritten whenever a new version of the viewer is built and copied over to the server. Take care to copy over any changes you've made to the widget XML files into the ``flexviewer`` repository beforehand so that those changes don't get erased during deployment. (This currently applies only to the widget configuration files, not to the map configuration files. The map configuration files are currently stored in gremlin-vm, not in the ``flexviewer`` project or the deployed viewer folder.)
