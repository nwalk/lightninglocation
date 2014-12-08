import os
from django.contrib.gis.utils import LayerMapping
from models import Sensors
import django
django.setup()


pilocation_mapping = {
    'lat' : 'lat',
    'lon' : 'lon',
    'gid' : 'gid',
    'point' : 'POINT',
}
pilocation_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/pi_locations.shp'))


def run(verbose=True):
    lm = LayerMapping(Sensors, pilocation_shp, pilocation_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
