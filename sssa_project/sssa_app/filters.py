import django_filters
from .models import Alst

class AlstFilter(django_filters.FilterSet):
    class Meta:
        model = Alst
        fields = {
            'id' : ['icontains'],
            'catalogue_number' : ['icontains'],
            'type' : ['icontains'],
            'type_of_material': ['icontains']
        }