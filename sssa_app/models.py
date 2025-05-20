from django.db import models
import os
import django_tables2 as tables


# Create your models here.

class Alst(models.Model):
    id = models.AutoField(primary_key=True, blank=False)
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
    restricted = models.TextField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = "last_csv_file"


    def extract_word_matereial(self):
        word = self.type_of_material.replace(", ", "  ").split()
        return word




class AlstTable(tables.Table):
    class Meta:
        model: Alst

