# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class SssaJasonDb(models.Model):
    id = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    catalogue_number = models.TextField(blank=True, null=True)
    parent = models.TextField(blank=True, null=True)
    catalogue_name = models.TextField(blank=True, null=True)
    fieldworker = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    informant_artist = models.TextField(blank=True, null=True)
    native_area_county = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    place_recorded = models.TextField(blank=True, null=True)
    type_of_material = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    disc_matrix_number = models.TextField(blank=True, null=True)
    tale_reference = models.TextField(blank=True, null=True)
    first_line = models.TextField(blank=True, null=True)
    instrument = models.TextField(blank=True, null=True)
    camera_operator = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    old_number_rl = models.TextField(blank=True, null=True)
    data_record_input = models.TextField(blank=True, null=True)
    data_last_amended = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sssa_jason_db'
