This is my identify widget for FlexViewer 2.2.1

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

* 2.1.5 - This version uses it's own drawtool and not the map managers so that drawtooltips
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