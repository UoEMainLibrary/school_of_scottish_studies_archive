from django.contrib import admin


from .models import Alst
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Alst)
class AlstAdmin(ImportExportModelAdmin):
    list_display = [
        'id',
        'catalogue_number',
        'collection',
        'collection_ref',
        'fieldworker',
        'date',
        'informant_artist',
        'native_area_county',
        'comments',
        'place_recorded',
        'type_of_material',
        'summary',
        'disc_matrix_number',
        'tale_reference',
        'title',
        'reference',
        'old_number_rl',
        'restricted',

    ]

