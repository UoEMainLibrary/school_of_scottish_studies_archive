import django_filters
from .models import Alst
from django.db.models import Q

class MultiWordCharFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value:
            # Split the input value by whitespace to handle multiple words
            words = value.split()
            # Start with an empty Q object
            query = Q()
            # Loop over words and add Q objects with icontains for each word
            for word in words:
                query &= Q(type_of_material__icontains=word)
            # Filter the queryset based on the accumulated Q objects
            return qs.filter(query)
        return qs

class AlstFilter(django_filters.FilterSet):
    id_exact = django_filters.CharFilter(field_name='id', lookup_expr='iexact')
    id_contains = django_filters.CharFilter(field_name='id', lookup_expr='icontains')
    type_exact = django_filters.CharFilter(field_name='type', lookup_expr='iexact')
    type_contains = django_filters.CharFilter(field_name='type', lookup_expr='icontains')
    catalogue_number_exact = django_filters.CharFilter(field_name='catalogue_number',lookup_expr='iexact')
    catalogue_number_contains = django_filters.CharFilter(field_name='catalogue_number',lookup_expr='icontains')
    parent_exact = django_filters.CharFilter(field_name='parent',lookup_expr='iexact')
    parent_contains = django_filters.CharFilter(field_name='parent',lookup_expr='icontains')
    type_of_material_exact = django_filters.CharFilter(field_name='type_of_material',lookup_expr='iexact')
    type_of_material_contains = MultiWordCharFilter(field_name='type_of_material',lookup_expr='icontains')

    class Meta:
        model = Alst
        fields = {
            'catalogue_number' : ['icontains'],
            'parent' : ['icontains'],
            'type' : ['icontains'],
            'type_of_material': ['icontains']
        }