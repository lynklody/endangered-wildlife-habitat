visualization of the geographic distribution of endangered wildlife species on Google Earth 

A picture from the conference:
https://www.instagram.com/p/BhZr41gAixk/?utm_source=ig_web_copy_link


Why I decided to do this project:

Data management for geographic data of wildlife has been a difficult task for researchers.  The main objective of this study is to create a method to generate KML files which aims at displaying geographic data on Google Earth in the hope that my method of organizing the data would pinpoint the relation between wildlife and their geographic distribution.  Furthermore, the product would contribute to future studies in the conservation of biodiversity and preservation of the ecological environment where the wildlife resides.


What I did in this project:

The data source of this project is the data set of Terrestrial Mammals from the International Union for Conservation Nature (IUCN) Red List (www.iucnredlist.org/technical-documents/spatial-data).  Original shapefiles, a popular geospatial vector data format for geographic information system (GIS) software, are provided on this website.  A GIS software called ArcGIS Map was used to convert the shapefiles into a kmz file, and then decompressed into a 1.6-gigabyte KML file.  It was necessary to write 13 functions in Python for this project. First, the large KML file was split into 5305 XML code sections in different text files.  Then a combine function was created to generate functioning KML files with desired geodata of one species to be displayed on Google Earth.  Later, an updated version of this function was coded in order to display the geographical distribution of several species at the same time for comparison.  Moreover, an updated split function was created to shrink the size of the final KML files by leaving only five decimal places of precision for representing longitudes and latitudes.  The reason why I chose this level of precision was that it measures positions on the earth to within 1 meter, which is sufficiently precise for this project.  Finally, a help function was created to provide the user with a list of 1175 genera to start with, since the binomial name of each species consists of genus and species.  The whole process of the functioning KML file generating is very interactive and user friendly. 
