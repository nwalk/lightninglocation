from apps.spatial import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers

# REST framework serializer
# http://www.django-rest-framework.org/tutorial/quickstart


class SensorsSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Sensors
        geo_field = 'point'
        fields = ('lat', 'lon', 'gid')
