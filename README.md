www.lightninglocation.com
=================

This is the main repository for Nathan, AJ, and Daniel's project

The idea behind this project is to use 3 RaspberryPi-AS3935 lightning sensors to triangulate lightning strikes in the Gainesville Georgia area. The geoprocessing is in a different repository; lightning geoprocessing. I wrote the SQL for that in Python using psycopg2 and postGIS, but I may end up using GeoDjango functions instead. The program that gets the data from the sensors is in the RPi sensors repository.
