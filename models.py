# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class SssaAppAlst(models.Model):
    id = models.BigAutoField(primary_key=True)
    catalogue_name = models.CharField(max_length=100, blank=True, null=True)
    catalogue_number = models.CharField(max_length=100, blank=True, null=True)
    comments = models.CharField(max_length=250, blank=True, null=True)
    data_last_amended = models.CharField(max_length=100, blank=True, null=True)
    data_record_input = models.CharField(max_length=100, blank=True, null=True)
    date = models.CharField(max_length=100, blank=True, null=True)
    disc_matrix_number = models.CharField(max_length=100, blank=True, null=True)
    fieldworker = models.CharField(max_length=100, blank=True, null=True)
    informant_artist = models.CharField(max_length=100, blank=True, null=True)
    native_area_county = models.CharField(max_length=100, blank=True, null=True)
    old_number_rl = models.CharField(max_length=100, blank=True, null=True)
    place_recorded = models.CharField(max_length=150, blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    summary = models.CharField(max_length=250, blank=True, null=True)
    tale_reference = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    type_of_material = models.CharField(max_length=150, blank=True, null=True)
    camera_operator = models.CharField(max_length=100, blank=True, null=True)
    first_line = models.CharField(max_length=100, blank=True, null=True)
    instrument = models.CharField(max_length=100, blank=True, null=True)
    parent = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sssa_app_alst'


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
    catalogue_number_copy = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sssa_jason_db'
