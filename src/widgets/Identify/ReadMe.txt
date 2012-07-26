This is my identify widget for FlexViewer 3.0

* 3.0 - Recompiled for Flex Viewer 3.0

* 2.5.8 - Fixed issue with cached/tiled layers not returning identify results.
	- Fixed issue with greater than and less than symbols in identify results.
	- Now uses the ProxyURL from the main config.xml and does not require you to add
	  httpproxy to the IdentifyWidget.xml.
	- Removed ability to copy from results (due to the negative effect on performance
	  of item renderer and occasionally not drawing text). You can copy the results
	  from the popup.

* 2.5.7 - Changed the useproxy child tag name to make it easier to understand the setup.
	  (see Identify Widget XML Configuration.pdf for details).
	- Added ability to copy from results.

* 2.5.6 - Fixed issue with duplicate identity results and getting results for some layers even
          if they are not visible when using visible option.
	- Fields can now have formatting such as currencyformat, dateformat and numberformat. 

* 2.5.5 - Verified and tested with Adobe Flex SDK 4.6 (Required for Flex Viewer 3.0)
	- Added infoautoclosemilliseconds to xml to delay closing the info window when moving from
          the results to the infowindow the infowindow does not disappear before you get there.
	- Added excludebasemaps as an option to the xml.
	- Fields have been broken out to individual field elements like most other widgets. This allows
	  for field aliases to be assigned to fields that will override the alias from the map service.
	- You can now specify that a field is popuponly which means that it will not be displayed in the
	  widgets results item renderer.
	- The widget results item renderer has had a good overhaul and uses less space and other significant
	  optimizations.
	- The top identifylayeroption now performs as most people would expect it only returns the top 
	  most result from the whole map and not each map service.

* 2.5.4 - Scale dependency and group layers are now honored when using the Identify option of visible.
	- Links can now have a tool tip specified.
	- Layer definitions are now honored when set on a layer in Flex Viewer. 
	- When you identify multiple results and hover over a result record in the widget's results
          the graphic is highlighted on the screen if you are returning geometry.
	- bug fixed for info popups not closing when you clear the identify results.
	- If you choose not to return geometry than the geometry drawn when identifying features
	  is used when hovering over a record in the widgets results list.

* 2.5.3 - Made a simple enhancement where when you use the point tool to identify
          the popup will always use where you click as it's anchor point instead
          of the identified geometries centroid.

* 2.5.2 - Fixed some issues with the new multi-links of v2.5.1
        - Fixed issue when identifylayeroption is set to visible and nothing is visible
          The loading icon does not go away.
        - Enhanced the identify geometry button to act as toggle button that way you can turn off
          identifying even when keepidentifyactive is set to true.
        - fixed issue when returngeometryforzoom is false and you use a geometry such as a extent
          and identify several features the extent you drew would be added as a graphic for each
          feature identified (overlapping extent graphics).
        - If you have more than one link specified and those links contain urls to images than
          the popup will contain all the images in the media browser of the popup.

* 2.5.1 - Added the ability to specify multiple links. You can specify that a link field
        is still included in the results. Links can have an alias specified for display
        in the Info Popup, and each link can have its own icon specified. 

* 2.5 - Added the ability to disable the line, extent, and polygon selection buttons
        in the IdentifyWidget.xml
      - Added the ability to turn off map popups when hovering or map graphics and or
        widget result records.

* 2.4.0.1 - Fixed bug with polyline geometry an using the betareturngeometryfix option
          - Remove code that was limiting panning when the widget was open.
	  - Added the Flex API PopUpRenderSkin.mxml to the code base to resolve Bug that
            is found in the 2.4 API.
        

* 2.4 - Recompiled for FlexViewer 2.4

* 2.3.3.1 - Fixed bug when you have keepidentifyactive="true" and close the widget panning the 
            map is disabled.

* 2.3.3 - Added a autoactivatedtool option to the IdentifyWidget.xml this enables the identify widget
          to activate on widget activation for those that want a simplified widget.
	- Reverted the change map in 2.3.2.2 as a found a work around, 
	  (which means DrawTool tips are gone again :) )

* 2.3.2.2 - Reverted to using the Map Managers DrawTool (which means DrawTool tips are back :( ),
	    as this was the only way to fix the issue with navigations tools working when drawing
	    shapes on the map after selecting a nav tool.

* 2.3.2.1 - Hopefully fixed results localization issue
	- Fixed zooming issue when clicking on a record.
	-Fixed Issue with < and > symbols in the PopUpInfo window.

//*BETA*//////////////////////////////////////////////////////////////////////////////////////////////////////
//	- There is a portion of this widget that is BETA and it is a fix for the returned geometry.         //
//	  The API/REST has a bug that is documented and randomly returns geometry in its original           //
//        spatial reference when layer ids are defined. I have a work around for this that is disabled      //
//	  by default. If you want to test this new beta fix then set the betareturngeometryfix to true      //
//	  in the IdentifyWidget.xml                                                                         //
//////////////////////////////////////////////////////////////////////////////////////////////////////////////

* 2.3.1 - Old default behavior of the identify widget becoming immediately active has been removed
	- Widget has been updated to look and act more like standard esri widgets
	- Widget now uses PopUpInfo new in 2.3 API
	- Allow for the linkicon url for come from the iconsuffix only or iconprefix only or
	  to be concatenated with iconprefix and an iconfield and the iconsuffix. What this means
	  is you do not have to have an iconfield specified if you want to use a static icon
	  just defined as a complete url in the iconprefix and/or iconsuffix

//*BETA*//////////////////////////////////////////////////////////////////////////////////////////////////////
//	- There is a portion of this widget that is BETA and it is a fix for the returned geometry.         //
//	  The API/REST has a bug that is documented and randomly returns geometry in its original           //
//        spatial reference when layer ids are defined. I have a work around for this that is disabled      //
//	  by default. If you want to test this new beta fix then set the betareturngeometryfix to true      //
//	  in the IdentifyWidget.xml                                                                         //
//////////////////////////////////////////////////////////////////////////////////////////////////////////////

* 2.2.3f - Fixed issue with keepidentifyactive being ignored.

* 2.2.3 - Identify by point/line/extent/polygon are all now supported
	- Info window will appear at the center of identified geometry now if returngeometryforzoom is set to true in xml file.
	if returngeometryforzoom is true, when you mouse over a record the geometry for that particular record is drawn using the symbology defined in the xml
	- The symbology used by the draw tools is now user defined in the xml
	- Fixed an issues with link icon if prefix or suffix is supplied and a empty field.

* 2.2.2f addresses an issue with the Flex Viewer 2.2 compiled version of this widget not functioning

* 2.2.2 The zoom to now determines the returned geometry type and zooms to the
        extent of the returned geometry.

        Fixed an issues with link field and null values.

* 2.2.1 Depreciated selectionlabel in the IdentifyWidget.xml
	Added Identify Configuration.pdf that explains all the IdentifyWidget.xml options

* 2.2 - Minor code fixes, to include issue with fields list not working if you had spaces behind the comma. 
        Proxy Capability added thanks to Alex Bostic

* 2.1.7 - This release fixes issues with duplicate results when identifying grouped layers
        Thanks to Erwan for this fix. This release also fixes an issue with feature type layers that
        use a mapServer instead of a featureServer.

* 2.1.6 - This is a fix to the issue of not being able to click on the info popups hyperlink
        because it closes when you move off of the results record. Now you will have to manually
        close the info popup yourself.

* 2.1.5 - This version uses its own drawtool and not the map managers so that drawtooltips
	can be turned off and I could properly deactivate the tool when the widget is closed.

* 2.1.4 - Added option for only identifying the specified layers in the IdentifyWidget.xml. 
	Fixed bug when identifying feature type layers that are pointing to a MapServer
	layer and not a FeatureServer.

* 2.1.3 - Moved the zoom2message inside the labels parent of the xml file
        - Added the keepidentifyactive has been added to allow you
	to specify that the identify tool will remain active after each indentify
	click on the map instead of the default behavior of defaulting back to map 
	navigation.

* 2.1.2 A couple of enhancements

   1) Allow for a link field and a linkprefix string and a linksuffix
      so that you can have a field value of "hello" and the prefix string
      of "http://myserver/says/" and a suffix string of ".jpg"
   2) Allows the hyperlink icon to be customized in the same fashon as
      the link field i.e you can have a field that has a value of "littleblue"
      and the prefix string of "http://myserver/myassets/" and a suffix
      string of ".jpg"
   3) Individual layer zoom scales can be specified
   4) force scale when result is clicked option. The default way is if
      your maps scale is greater than the specified scale then it will zoom
      in, but if your maps scale is currently less than the scale than nothing
      happens. forceScale will zoom to the predefined scale either way if
      set to true.
   5) The zoom2message i.e tooltip that you get when hovering over a record
      is now an attribute you can change in the xml.

* 2.1.1 includes a fix to the hyperlink button on the results not working

It is a culmination of several different versions that I have produced 
for the last year or more for the Sample Flex Viewer 1.x.

This version allows you to specify particular layers of a map service to 
identify and the particular fields to display for those layers. This 
version also supports hyperlinks and truly honors the setting of visible 
in the xml configuration file. If you are using a featurelayer it will 
identify the MapServer that is the the same as the FeatureServer and just 
force indentification of the specified layer if there was one.

To install using the compiled version just copy the folder called Identify 
under the Widgets folder, and add this line to your config.xml

<widget label="Identify" left="330" top="80" preload="open"
                icon="assets/images/i_info.png"
                config="widgets/Identify/IdentifyWidget.xml"
                url="widgets/Identify/IdentifyWidget.swf"/>

For the Uncompiled you need to copy the Identify folder to src/widgets then 
add IdentifyWidget.mxml to your flex projects modules list, and compile your
project as well as add the widget line above to your config.xml.

Enjoy
Robert Scheitlin
