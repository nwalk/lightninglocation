from django.contrib.gis.db import models


class Sensors(models.Model):
    """Regular Django fields corresponding to the attributes in the
    pi_locations shapefile."""
    lat = models.FloatField()
    lon = models.FloatField()
    gid = models.IntegerField(max_length=2)
    point = models.PointField()
    objects = models.GeoManager()

    # Returns the string representation of the model.
    # def __str__(self):              # __unicode__ on Python 2
    #     return self.gid