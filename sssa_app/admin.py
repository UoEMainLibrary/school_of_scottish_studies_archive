from django.contrib import admin


from .models import Alst
from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
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

class CustomUserAdmin(BaseUserAdmin):
    # Add 'is_active' to the list display
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')

# Unregister the original User admin
admin.site.unregister(User)
# Register again with the custom one
admin.site.register(User, CustomUserAdmin)
