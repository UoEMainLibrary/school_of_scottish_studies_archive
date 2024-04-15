from django.db import models
import os
import django_tables2 as tables


# Create your models here.

class Alst(models.Model):
    type = models.CharField(blank=True, default=None, null=True, max_length=20)
    catalogue_number = models.CharField(blank=True, default=None, null=True, max_length=100)
    parent = models.CharField(blank=True, default=None, null=True, max_length=100)
    catalogue_name = models.CharField(blank=True, default=None, null=True, max_length=100)
    fieldworker = models.CharField(blank=True, default=None, null=True, max_length=100)
    date = models.CharField(blank=True, default=None, null=True, max_length=100)
    informant_artist = models.CharField(blank=True, default=None, null=True, max_length=100)
    native_area_county = models.CharField(blank=True, default=None, null=True, max_length=100)
    comments = models.CharField(blank=True, default=None, null=True, max_length=250)
    place_recorded = models.CharField(blank=True, default=None, null=True, max_length=150)
    type_of_material = models.CharField(blank=True, default=None, null=True, max_length=150)
    summary = models.CharField(blank=True, default=None, null=True, max_length=250)
    disc_matrix_number = models.CharField(blank=True, default=None, null=True, max_length=100)
    tale_reference = models.CharField(blank=True, default=None, null=True, max_length=100)
    first_line = models.CharField(blank=True, default=None, null=True, max_length=100)
    instrument = models.CharField(blank=True, default=None, null=True, max_length=100)
    camera_operator = models.CharField(blank=True, default=None, null=True, max_length=100)
    title = models.CharField(blank=True, default=None, null=True, max_length=100)
    reference = models.CharField(blank=True, default=None, null=True, max_length=100)
    old_number_rl = models.CharField(blank=True, default=None, null=True, max_length=100)
    data_record_input = models.CharField(blank=True, default=None, null=True, max_length=100)
    data_last_amended = models.CharField(blank=True, default=None, null=True, max_length=100)

    class Meta:
        managed = False
        db_table = "sssa_jason_db"

    def __str__(self):
        return self.type



class AlstTable(tables.Table):
    class Meta:
        model: Alst
