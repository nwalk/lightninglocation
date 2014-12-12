from apps.spatial import models, serializers
from rest_framework import generics
import django_filters

# views section of quick start guide
# http://www.django-rest-framework.org/tutorial/quickstart


class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type): integers})
        return qs


class SensorsFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Sensors
        fields = ['lat', 'lon', 'gid']


class SensorsCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Sensors.objects.all()
    serializer_class = serializers.SensorsSerializer
    filter_class = SensorsFilter