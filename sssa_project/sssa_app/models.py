from django.db import models
import os

# Create your models here.

class Alst(models.Model):
    catalogue_number = models.CharField(blank=True, default=None, null=True, max_length=100)
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
    title = models.CharField(blank=True, default=None, null=True, max_length=100)
    reference = models.CharField(blank=True, default=None, null=True, max_length=100)
    old_number_rl = models.CharField(blank=True, default=None, null=True, max_length=100)
    data_record_input = models.CharField(blank=True, default=None, null=True, max_length=100)
    data_last_amended = models.CharField(blank=True, default=None, null=True, max_length=100)

    def __str__(self):
        return self.catalogue_number
