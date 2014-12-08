from django.contrib import admin
from django.contrib.gis import admin
from models import Sensors

admin.site.register(Sensors, admin.GeoModelAdmin)