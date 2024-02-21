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


class Batch(models.Model):
    bid = models.PositiveIntegerField(primary_key=True, db_comment='Primary Key: Unique batch ID.')
    token = models.CharField(max_length=64, db_collation='ascii_general_ci', db_comment="A string token generated against the current user's session id and the batch id, used to ensure that only the user who submitted the batch can effectively access it.")
    timestamp = models.BigIntegerField(db_comment='A Unix timestamp indicating when this batch was submitted for processing. Stale batches are purged at cron time.')
    batch = models.TextField(blank=True, null=True, db_comment='A serialized array containing the processing data for the batch.')

    class Meta:
        managed = False
        db_table = 'batch'
        db_table_comment = 'Stores details about batches (processes that run in…'


class BlockContent(models.Model):
    revision_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    type = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The ID of the target entity.')
    uuid = models.CharField(unique=True, max_length=128, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')

    class Meta:
        managed = False
        db_table = 'block_content'
        db_table_comment = 'The base table for block_content entities.'


class BlockContentBody(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    body_value = models.TextField()
    body_summary = models.TextField(blank=True, null=True)
    body_format = models.CharField(max_length=255, db_collation='ascii_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_content__body'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for block_content field body.'


class BlockContentFieldData(models.Model):
    id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (id, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField()
    type = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The ID of the target entity.')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    status = models.IntegerField()
    changed = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()
    revision_translation_affected = models.IntegerField(blank=True, null=True)
    reusable = models.IntegerField(blank=True, null=True)
    info = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_content_field_data'
        unique_together = (('id', 'langcode'),)
        db_table_comment = 'The data table for block_content entities.'


class BlockContentFieldRevision(models.Model):
    id = models.PositiveIntegerField()
    revision_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (revision_id, langcode) found, that is not supported. The first column is selected.
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    status = models.IntegerField()
    changed = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()
    revision_translation_affected = models.IntegerField(blank=True, null=True)
    info = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_content_field_revision'
        unique_together = (('revision_id', 'langcode'),)
        db_table_comment = 'The revision data table for block_content entities.'


class BlockContentRevision(models.Model):
    id = models.PositiveIntegerField()
    revision_id = models.AutoField(primary_key=True)
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    revision_user = models.PositiveIntegerField(blank=True, null=True, db_comment='The ID of the target entity.')
    revision_created = models.IntegerField(blank=True, null=True)
    revision_log = models.TextField(blank=True, null=True)
    revision_default = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_content_revision'
        db_table_comment = 'The revision table for block_content entities.'


class BlockContentRevisionBody(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    body_value = models.TextField()
    body_summary = models.TextField(blank=True, null=True)
    body_format = models.CharField(max_length=255, db_collation='ascii_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'block_content_revision__body'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for block_content field body.'


class CacheBootstrap(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_bootstrap'
        db_table_comment = 'Storage for the cache API.'


class CacheConfig(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_config'
        db_table_comment = 'Storage for the cache API.'


class CacheContainer(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_container'
        db_table_comment = 'Storage for the cache API.'


class CacheData(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_data'
        db_table_comment = 'Storage for the cache API.'


class CacheDefault(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_default'
        db_table_comment = 'Storage for the cache API.'


class CacheDiscovery(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_discovery'
        db_table_comment = 'Storage for the cache API.'


class CacheDiscoveryMigration(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_discovery_migration'
        db_table_comment = 'Storage for the cache API.'


class CacheDynamicPageCache(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_dynamic_page_cache'
        db_table_comment = 'Storage for the cache API.'


class CacheEntity(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_entity'
        db_table_comment = 'Storage for the cache API.'


class CacheMenu(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_menu'
        db_table_comment = 'Storage for the cache API.'


class CacheMigrate(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_migrate'
        db_table_comment = 'Storage for the cache API.'


class CachePage(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_page'
        db_table_comment = 'Storage for the cache API.'


class CacheRender(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_render'
        db_table_comment = 'Storage for the cache API.'


class CacheToolbar(models.Model):
    cid = models.CharField(primary_key=True, max_length=255, db_collation='ascii_bin', db_comment='Primary Key: Unique cache ID.')
    data = models.TextField(blank=True, null=True, db_comment='A collection of data to cache.')
    expire = models.BigIntegerField(db_comment='A Unix timestamp indicating when the cache entry should expire, or -1 for never.')
    created = models.DecimalField(max_digits=14, decimal_places=3, db_comment='A timestamp with millisecond precision indicating when the cache entry was created.')
    serialized = models.SmallIntegerField(db_comment='A flag to indicate whether content is serialized (1) or not (0).')
    tags = models.TextField(blank=True, null=True, db_comment='Space-separated list of cache tags for this entry.')
    checksum = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The tag invalidation checksum when this entry was saved.')

    class Meta:
        managed = False
        db_table = 'cache_toolbar'
        db_table_comment = 'Storage for the cache API.'


class Cachetags(models.Model):
    tag = models.CharField(primary_key=True, max_length=255, db_collation='ascii_general_ci', db_comment='Namespace-prefixed tag string.')
    invalidations = models.IntegerField(db_comment='Number incremented when the tag is invalidated.')

    class Meta:
        managed = False
        db_table = 'cachetags'
        db_table_comment = 'Cache table for tracking cache tag invalidations.'


class Config(models.Model):
    collection = models.CharField(primary_key=True, max_length=255, db_collation='ascii_general_ci', db_comment='Primary Key: Config object collection.')  # The composite primary key (collection, name) found, that is not supported. The first column is selected.
    name = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='Primary Key: Config object name.')
    data = models.TextField(blank=True, null=True, db_comment='A serialized configuration object data.')

    class Meta:
        managed = False
        db_table = 'config'
        unique_together = (('collection', 'name'),)
        db_table_comment = 'The base table for configuration data.'


class ConfigImport(models.Model):
    collection = models.CharField(primary_key=True, max_length=255, db_collation='ascii_general_ci', db_comment='Primary Key: Config object collection.')  # The composite primary key (collection, name) found, that is not supported. The first column is selected.
    name = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='Primary Key: Config object name.')
    data = models.TextField(blank=True, null=True, db_comment='A serialized configuration object data.')

    class Meta:
        managed = False
        db_table = 'config_import'
        unique_together = (('collection', 'name'),)
        db_table_comment = 'The base table for configuration data.'


class ConfigSnapshot(models.Model):
    collection = models.CharField(primary_key=True, max_length=255, db_collation='ascii_general_ci', db_comment='Primary Key: Config object collection.')  # The composite primary key (collection, name) found, that is not supported. The first column is selected.
    name = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='Primary Key: Config object name.')
    data = models.TextField(blank=True, null=True, db_comment='A serialized configuration object data.')

    class Meta:
        managed = False
        db_table = 'config_snapshot'
        unique_together = (('collection', 'name'),)
        db_table_comment = 'The base table for configuration data.'


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


class FileManaged(models.Model):
    fid = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=128, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    uid = models.PositiveIntegerField(blank=True, null=True, db_comment='The ID of the target entity.')
    filename = models.CharField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255, db_collation='utf8mb4_bin')
    filemime = models.CharField(max_length=255, db_collation='ascii_general_ci', blank=True, null=True)
    filesize = models.PositiveBigIntegerField(blank=True, null=True)
    status = models.IntegerField()
    created = models.IntegerField(blank=True, null=True)
    changed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'file_managed'
        db_table_comment = 'The base table for file entities.'


class FileUsage(models.Model):
    fid = models.PositiveIntegerField(primary_key=True, db_comment='File ID.')  # The composite primary key (fid, type, id, module) found, that is not supported. The first column is selected.
    module = models.CharField(max_length=50, db_collation='ascii_general_ci', db_comment='The name of the module that is using the file.')
    type = models.CharField(max_length=64, db_collation='ascii_general_ci', db_comment='The name of the object type in which the file is used.')
    id = models.CharField(max_length=64, db_collation='ascii_general_ci', db_comment='The primary key of the object using the file.')
    count = models.PositiveIntegerField(db_comment='The number of times this file is used by this object.')

    class Meta:
        managed = False
        db_table = 'file_usage'
        unique_together = (('fid', 'type', 'id', 'module'),)
        db_table_comment = 'Track where a file is used.'


class Flood(models.Model):
    fid = models.AutoField(primary_key=True, db_comment='Unique flood event ID.')
    event = models.CharField(max_length=64, db_collation='ascii_general_ci', db_comment='Name of event (e.g. contact).')
    identifier = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='Identifier of the visitor, such as an IP address or hostname.')
    timestamp = models.BigIntegerField(db_comment='Timestamp of the event.')
    expiration = models.BigIntegerField(db_comment='Expiration timestamp. Expired events are purged on cron run.')

    class Meta:
        managed = False
        db_table = 'flood'
        db_table_comment = 'Flood controls the threshold of events, such as the number…'


class KeyValue(models.Model):
    collection = models.CharField(primary_key=True, max_length=128, db_collation='ascii_general_ci', db_comment='A named collection of key and value pairs.')  # The composite primary key (collection, name) found, that is not supported. The first column is selected.
    name = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The key of the key-value pair. As KEY is a SQL reserved keyword, name was chosen instead.')
    value = models.TextField(db_comment='The value.')

    class Meta:
        managed = False
        db_table = 'key_value'
        unique_together = (('collection', 'name'),)
        db_table_comment = 'Generic key-value storage table. See the state system for…'


class KeyValueExpire(models.Model):
    collection = models.CharField(primary_key=True, max_length=128, db_collation='ascii_general_ci', db_comment='A named collection of key and value pairs.')  # The composite primary key (collection, name) found, that is not supported. The first column is selected.
    name = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The key of the key/value pair.')
    value = models.TextField(db_comment='The value of the key/value pair.')
    expire = models.IntegerField(db_comment='The time since Unix epoch in seconds when this item expires. Defaults to the maximum possible time.')

    class Meta:
        managed = False
        db_table = 'key_value_expire'
        unique_together = (('collection', 'name'),)
        db_table_comment = 'Generic key/value storage table with an expiration.'


class MenuLinkContent(models.Model):
    revision_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    bundle = models.CharField(max_length=32, db_collation='ascii_general_ci')
    uuid = models.CharField(unique=True, max_length=128, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')

    class Meta:
        managed = False
        db_table = 'menu_link_content'
        db_table_comment = 'The base table for menu_link_content entities.'


class MenuLinkContentData(models.Model):
    id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (id, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField()
    bundle = models.CharField(max_length=32, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    menu_name = models.CharField(max_length=255, db_collation='ascii_general_ci', blank=True, null=True)
    link_uri = models.CharField(db_column='link__uri', max_length=2048, blank=True, null=True, db_comment='The URI of the link.')  # Field renamed because it contained more than one '_' in a row.
    link_title = models.CharField(db_column='link__title', max_length=255, blank=True, null=True, db_comment='The link text.')  # Field renamed because it contained more than one '_' in a row.
    link_options = models.TextField(db_column='link__options', blank=True, null=True, db_comment='Serialized array of options for the link.')  # Field renamed because it contained more than one '_' in a row.
    external = models.IntegerField(blank=True, null=True)
    rediscover = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    expanded = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField()
    parent = models.CharField(max_length=255, blank=True, null=True)
    changed = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()
    revision_translation_affected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_link_content_data'
        unique_together = (('id', 'langcode'),)
        db_table_comment = 'The data table for menu_link_content entities.'


class MenuLinkContentFieldRevision(models.Model):
    id = models.PositiveIntegerField()
    revision_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (revision_id, langcode) found, that is not supported. The first column is selected.
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    link_uri = models.CharField(db_column='link__uri', max_length=2048, blank=True, null=True, db_comment='The URI of the link.')  # Field renamed because it contained more than one '_' in a row.
    link_title = models.CharField(db_column='link__title', max_length=255, blank=True, null=True, db_comment='The link text.')  # Field renamed because it contained more than one '_' in a row.
    link_options = models.TextField(db_column='link__options', blank=True, null=True, db_comment='Serialized array of options for the link.')  # Field renamed because it contained more than one '_' in a row.
    external = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField()
    changed = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()
    revision_translation_affected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_link_content_field_revision'
        unique_together = (('revision_id', 'langcode'),)
        db_table_comment = 'The revision data table for menu_link_content entities.'


class MenuLinkContentRevision(models.Model):
    id = models.PositiveIntegerField()
    revision_id = models.AutoField(primary_key=True)
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    revision_default = models.IntegerField(blank=True, null=True)
    revision_user = models.PositiveIntegerField(blank=True, null=True, db_comment='The ID of the target entity.')
    revision_created = models.IntegerField(blank=True, null=True)
    revision_log_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_link_content_revision'
        db_table_comment = 'The revision table for menu_link_content entities.'


class MenuTree(models.Model):
    menu_name = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment="The menu name. All links with the same menu name (such as 'tools') are part of the same menu.")
    mlid = models.AutoField(primary_key=True, db_comment='The menu link ID (mlid) is the integer primary key.')
    id = models.CharField(unique=True, max_length=255, db_collation='ascii_general_ci', db_comment='Unique machine name: the plugin ID.')
    parent = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The plugin ID for the parent of this link.')
    route_name = models.CharField(max_length=255, db_collation='ascii_general_ci', blank=True, null=True, db_comment='The machine name of a defined Symfony Route this menu item represents.')
    route_param_key = models.CharField(max_length=255, blank=True, null=True, db_comment='An encoded string of route parameters for loading by route.')
    route_parameters = models.TextField(blank=True, null=True, db_comment='Serialized array of route parameters of this menu link.')
    url = models.CharField(max_length=255, db_comment='The external path this link points to (when not using a route).')
    title = models.TextField(blank=True, null=True, db_comment='The serialized title for the link. May be a TranslatableMarkup.')
    description = models.TextField(blank=True, null=True, db_comment='The serialized description of this link - used for admin pages and title attribute. May be a TranslatableMarkup.')
    class_field = models.TextField(db_column='class', blank=True, null=True, db_comment='The class for this link plugin.')  # Field renamed because it was a Python reserved word.
    options = models.TextField(blank=True, null=True, db_comment='A serialized array of URL options, such as a query string or HTML attributes.')
    provider = models.CharField(max_length=50, db_collation='ascii_general_ci', db_comment='The name of the module that generated this link.')
    enabled = models.SmallIntegerField(db_comment='A flag for whether the link should be rendered in menus. (0 = a disabled menu item that may be shown on admin screens, 1 = a normal, visible link)')
    discovered = models.SmallIntegerField(db_comment='A flag for whether the link was discovered, so can be purged on rebuild')
    expanded = models.SmallIntegerField(db_comment='Flag for whether this link should be rendered as expanded in menus - expanded links always have their child links displayed, instead of only when the link is in the active trail (1 = expanded, 0 = not expanded)')
    weight = models.IntegerField(db_comment='Link weight among links in the same menu at the same depth.')
    metadata = models.TextField(blank=True, null=True, db_comment='A serialized array of data that may be used by the plugin instance.')
    has_children = models.SmallIntegerField(db_comment='Flag indicating whether any enabled links have this link as a parent (1 = enabled children exist, 0 = no enabled children).')
    depth = models.SmallIntegerField(db_comment='The depth relative to the top level. A link with empty parent will have depth == 1.')
    p1 = models.PositiveIntegerField(db_comment='The first mlid in the materialized path. If N = depth, then pN must equal the mlid. If depth > 1 then p(N-1) must equal the parent link mlid. All pX where X > depth must equal zero. The columns p1 .. p9 are also called the parents.')
    p2 = models.PositiveIntegerField(db_comment='The second mlid in the materialized path. See p1.')
    p3 = models.PositiveIntegerField(db_comment='The third mlid in the materialized path. See p1.')
    p4 = models.PositiveIntegerField(db_comment='The fourth mlid in the materialized path. See p1.')
    p5 = models.PositiveIntegerField(db_comment='The fifth mlid in the materialized path. See p1.')
    p6 = models.PositiveIntegerField(db_comment='The sixth mlid in the materialized path. See p1.')
    p7 = models.PositiveIntegerField(db_comment='The seventh mlid in the materialized path. See p1.')
    p8 = models.PositiveIntegerField(db_comment='The eighth mlid in the materialized path. See p1.')
    p9 = models.PositiveIntegerField(db_comment='The ninth mlid in the materialized path. See p1.')
    form_class = models.CharField(max_length=255, blank=True, null=True, db_comment='meh')

    class Meta:
        managed = False
        db_table = 'menu_tree'
        db_table_comment = 'Contains the menu tree hierarchy.'


class MigrateMapAlst(models.Model):
    source_ids_hash = models.CharField(primary_key=True, max_length=64, db_comment='Hash of source ids. Used as primary key')
    sourceid1 = models.CharField(max_length=255)
    destid1 = models.PositiveIntegerField(blank=True, null=True)
    source_row_status = models.PositiveIntegerField(db_comment='Indicates current status of the source row')
    rollback_action = models.PositiveIntegerField(db_comment='Flag indicating what to do for this item on rollback')
    last_imported = models.PositiveBigIntegerField(db_comment='UNIX timestamp of the last time this row was imported')
    hash = models.CharField(max_length=64, blank=True, null=True, db_comment='Hash of source row data, for detecting changes')

    class Meta:
        managed = False
        db_table = 'migrate_map_alst'
        db_table_comment = 'Mappings from source identifier value(s) to destination…'


class MigrateMapAlstDbo(models.Model):
    source_ids_hash = models.CharField(primary_key=True, max_length=64, db_comment='Hash of source ids. Used as primary key')
    sourceid1 = models.CharField(max_length=255)
    destid1 = models.PositiveIntegerField(blank=True, null=True)
    source_row_status = models.PositiveIntegerField(db_comment='Indicates current status of the source row')
    rollback_action = models.PositiveIntegerField(db_comment='Flag indicating what to do for this item on rollback')
    last_imported = models.PositiveBigIntegerField(db_comment='UNIX timestamp of the last time this row was imported')
    hash = models.CharField(max_length=64, blank=True, null=True, db_comment='Hash of source row data, for detecting changes')

    class Meta:
        managed = False
        db_table = 'migrate_map_alst_dbo'
        db_table_comment = 'Mappings from source identifier value(s) to destination…'


class MigrateMapMndx(models.Model):
    source_ids_hash = models.CharField(primary_key=True, max_length=64, db_comment='Hash of source ids. Used as primary key')
    sourceid1 = models.CharField(max_length=255)
    destid1 = models.PositiveIntegerField(blank=True, null=True)
    source_row_status = models.PositiveIntegerField(db_comment='Indicates current status of the source row')
    rollback_action = models.PositiveIntegerField(db_comment='Flag indicating what to do for this item on rollback')
    last_imported = models.PositiveBigIntegerField(db_comment='UNIX timestamp of the last time this row was imported')
    hash = models.CharField(max_length=64, blank=True, null=True, db_comment='Hash of source row data, for detecting changes')

    class Meta:
        managed = False
        db_table = 'migrate_map_mndx'
        db_table_comment = 'Mappings from source identifier value(s) to destination…'


class MigrateMapNewsystemAlst(models.Model):
    source_ids_hash = models.CharField(primary_key=True, max_length=64, db_comment='Hash of source ids. Used as primary key')
    sourceid1 = models.CharField(max_length=255)
    destid1 = models.PositiveIntegerField(blank=True, null=True)
    source_row_status = models.PositiveIntegerField(db_comment='Indicates current status of the source row')
    rollback_action = models.PositiveIntegerField(db_comment='Flag indicating what to do for this item on rollback')
    last_imported = models.PositiveBigIntegerField(db_comment='UNIX timestamp of the last time this row was imported')
    hash = models.CharField(max_length=64, blank=True, null=True, db_comment='Hash of source row data, for detecting changes')

    class Meta:
        managed = False
        db_table = 'migrate_map_newsystem_alst'
        db_table_comment = 'Mappings from source identifier value(s) to destination…'


class MigrateMapNewsystemMndx(models.Model):
    source_ids_hash = models.CharField(primary_key=True, max_length=64, db_comment='Hash of source ids. Used as primary key')
    sourceid1 = models.CharField(max_length=255)
    destid1 = models.PositiveIntegerField(blank=True, null=True)
    source_row_status = models.PositiveIntegerField(db_comment='Indicates current status of the source row')
    rollback_action = models.PositiveIntegerField(db_comment='Flag indicating what to do for this item on rollback')
    last_imported = models.PositiveBigIntegerField(db_comment='UNIX timestamp of the last time this row was imported')
    hash = models.CharField(max_length=64, blank=True, null=True, db_comment='Hash of source row data, for detecting changes')

    class Meta:
        managed = False
        db_table = 'migrate_map_newsystem_mndx'
        db_table_comment = 'Mappings from source identifier value(s) to destination…'


class MigrateMapOrigAlst(models.Model):
    source_ids_hash = models.CharField(primary_key=True, max_length=64, db_comment='Hash of source ids. Used as primary key')
    sourceid1 = models.CharField(max_length=255)
    destid1 = models.PositiveIntegerField(blank=True, null=True)
    source_row_status = models.PositiveIntegerField(db_comment='Indicates current status of the source row')
    rollback_action = models.PositiveIntegerField(db_comment='Flag indicating what to do for this item on rollback')
    last_imported = models.PositiveBigIntegerField(db_comment='UNIX timestamp of the last time this row was imported')
    hash = models.CharField(max_length=64, blank=True, null=True, db_comment='Hash of source row data, for detecting changes')

    class Meta:
        managed = False
        db_table = 'migrate_map_orig_alst'
        db_table_comment = 'Mappings from source identifier value(s) to destination…'


class MigrateMapOutstandingAlst(models.Model):
    source_ids_hash = models.CharField(primary_key=True, max_length=64, db_comment='Hash of source ids. Used as primary key')
    sourceid1 = models.CharField(max_length=255)
    destid1 = models.PositiveIntegerField(blank=True, null=True)
    source_row_status = models.PositiveIntegerField(db_comment='Indicates current status of the source row')
    rollback_action = models.PositiveIntegerField(db_comment='Flag indicating what to do for this item on rollback')
    last_imported = models.PositiveBigIntegerField(db_comment='UNIX timestamp of the last time this row was imported')
    hash = models.CharField(max_length=64, blank=True, null=True, db_comment='Hash of source row data, for detecting changes')

    class Meta:
        managed = False
        db_table = 'migrate_map_outstanding_alst'
        db_table_comment = 'Mappings from source identifier value(s) to destination…'


class MigrateMapSplitAlst(models.Model):
    source_ids_hash = models.CharField(primary_key=True, max_length=64, db_comment='Hash of source ids. Used as primary key')
    sourceid1 = models.CharField(max_length=255)
    destid1 = models.PositiveIntegerField(blank=True, null=True)
    source_row_status = models.PositiveIntegerField(db_comment='Indicates current status of the source row')
    rollback_action = models.PositiveIntegerField(db_comment='Flag indicating what to do for this item on rollback')
    last_imported = models.PositiveBigIntegerField(db_comment='UNIX timestamp of the last time this row was imported')
    hash = models.CharField(max_length=64, blank=True, null=True, db_comment='Hash of source row data, for detecting changes')

    class Meta:
        managed = False
        db_table = 'migrate_map_split_alst'
        db_table_comment = 'Mappings from source identifier value(s) to destination…'


class MigrateMapSplitMndx(models.Model):
    source_ids_hash = models.CharField(primary_key=True, max_length=64, db_comment='Hash of source ids. Used as primary key')
    sourceid1 = models.CharField(max_length=255)
    destid1 = models.PositiveIntegerField(blank=True, null=True)
    source_row_status = models.PositiveIntegerField(db_comment='Indicates current status of the source row')
    rollback_action = models.PositiveIntegerField(db_comment='Flag indicating what to do for this item on rollback')
    last_imported = models.PositiveBigIntegerField(db_comment='UNIX timestamp of the last time this row was imported')
    hash = models.CharField(max_length=64, blank=True, null=True, db_comment='Hash of source row data, for detecting changes')

    class Meta:
        managed = False
        db_table = 'migrate_map_split_mndx'
        db_table_comment = 'Mappings from source identifier value(s) to destination…'


class MigrateMessageAlst(models.Model):
    msgid = models.AutoField(primary_key=True)
    source_ids_hash = models.CharField(max_length=64, db_comment='Hash of source ids. Used as primary key')
    level = models.PositiveIntegerField()
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'migrate_message_alst'
        db_table_comment = 'Messages generated during a migration process'


class MigrateMessageAlstDbo(models.Model):
    msgid = models.AutoField(primary_key=True)
    source_ids_hash = models.CharField(max_length=64, db_comment='Hash of source ids. Used as primary key')
    level = models.PositiveIntegerField()
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'migrate_message_alst_dbo'
        db_table_comment = 'Messages generated during a migration process'


class MigrateMessageMndx(models.Model):
    msgid = models.AutoField(primary_key=True)
    source_ids_hash = models.CharField(max_length=64, db_comment='Hash of source ids. Used as primary key')
    level = models.PositiveIntegerField()
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'migrate_message_mndx'
        db_table_comment = 'Messages generated during a migration process'


class MigrateMessageNewsystemAlst(models.Model):
    msgid = models.AutoField(primary_key=True)
    source_ids_hash = models.CharField(max_length=64, db_comment='Hash of source ids. Used as primary key')
    level = models.PositiveIntegerField()
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'migrate_message_newsystem_alst'
        db_table_comment = 'Messages generated during a migration process'


class MigrateMessageNewsystemMndx(models.Model):
    msgid = models.AutoField(primary_key=True)
    source_ids_hash = models.CharField(max_length=64, db_comment='Hash of source ids. Used as primary key')
    level = models.PositiveIntegerField()
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'migrate_message_newsystem_mndx'
        db_table_comment = 'Messages generated during a migration process'


class MigrateMessageOrigAlst(models.Model):
    msgid = models.AutoField(primary_key=True)
    source_ids_hash = models.CharField(max_length=64, db_comment='Hash of source ids. Used as primary key')
    level = models.PositiveIntegerField()
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'migrate_message_orig_alst'
        db_table_comment = 'Messages generated during a migration process'


class MigrateMessageOutstandingAlst(models.Model):
    msgid = models.AutoField(primary_key=True)
    source_ids_hash = models.CharField(max_length=64, db_comment='Hash of source ids. Used as primary key')
    level = models.PositiveIntegerField()
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'migrate_message_outstanding_alst'
        db_table_comment = 'Messages generated during a migration process'


class MigrateMessageSplitAlst(models.Model):
    msgid = models.AutoField(primary_key=True)
    source_ids_hash = models.CharField(max_length=64, db_comment='Hash of source ids. Used as primary key')
    level = models.PositiveIntegerField()
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'migrate_message_split_alst'
        db_table_comment = 'Messages generated during a migration process'


class MigrateMessageSplitMndx(models.Model):
    msgid = models.AutoField(primary_key=True)
    source_ids_hash = models.CharField(max_length=64, db_comment='Hash of source ids. Used as primary key')
    level = models.PositiveIntegerField()
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'migrate_message_split_mndx'
        db_table_comment = 'Messages generated during a migration process'


class Node(models.Model):
    nid = models.AutoField(primary_key=True)
    vid = models.PositiveIntegerField(unique=True, blank=True, null=True)
    type = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The ID of the target entity.')
    uuid = models.CharField(unique=True, max_length=128, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')

    class Meta:
        managed = False
        db_table = 'node'
        db_table_comment = 'The base table for node entities.'


class NodeBody(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    body_value = models.TextField()
    body_summary = models.TextField(blank=True, null=True)
    body_format = models.CharField(max_length=255, db_collation='ascii_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node__body'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field body.'


class NodeFieldArea(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_area_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_area'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_area.'


class NodeFieldCam(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_cam_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_cam'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_cam.'


class NodeFieldCat(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_cat_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node__field_cat'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_cat.'


class NodeFieldCatalogue(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_catalogue_target_id = models.PositiveIntegerField(db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'node__field_catalogue'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_catalogue.'


class NodeFieldComm(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_comm_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_comm'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_comm.'


class NodeFieldCopyrightInformation(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_copyright_information_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_copyright_information'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_copyright_information.'


class NodeFieldDamend(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_damend_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node__field_damend'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_damend.'


class NodeFieldDate(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_date_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node__field_date'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_date.'


class NodeFieldDinput(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_dinput_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node__field_dinput'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_dinput.'


class NodeFieldDisc(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_disc_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node__field_disc'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_disc.'


class NodeFieldFlin(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_flin_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_flin'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_flin.'


class NodeFieldFw(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_fw_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_fw'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_fw.'


class NodeFieldInf(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_inf_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_inf'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_inf.'


class NodeFieldIns(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_ins_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_ins'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_ins.'


class NodeFieldInstruments(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_instruments_target_id = models.PositiveIntegerField(db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'node__field_instruments'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_instruments.'


class NodeFieldNumb(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_numb_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node__field_numb'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_numb.'


class NodeFieldParentDisc(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_parent_disc_target_id = models.PositiveIntegerField(db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'node__field_parent_disc'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_parent_disc.'


class NodeFieldPlac(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_plac_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node__field_plac'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_plac.'


class NodeFieldRef(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_ref_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node__field_ref'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_ref.'


class NodeFieldRl(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_rl_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node__field_rl'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_rl.'


class NodeFieldSumm(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_summ_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_summ'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_summ.'


class NodeFieldTale(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_tale_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_tale'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_tale.'


class NodeFieldTitl(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_titl_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_titl'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_titl.'


class NodeFieldType(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_type_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node__field_type'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_type.'


class NodeFieldTypes(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_types_target_id = models.PositiveIntegerField(db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'node__field_types'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for node field field_types.'


class NodeAccess(models.Model):
    nid = models.PositiveIntegerField(primary_key=True, db_comment='The node.nid this record affects.')  # The composite primary key (nid, gid, realm, langcode) found, that is not supported. The first column is selected.
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci', db_comment='The language.langcode of this node.')
    fallback = models.PositiveIntegerField(db_comment='Boolean indicating whether this record should be used as a fallback if a language condition is not provided.')
    gid = models.PositiveIntegerField(db_comment="The grant ID a user must possess in the specified realm to gain this row's privileges on the node.")
    realm = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The realm in which the user must possess the grant ID. Modules can define one or more realms by implementing hook_node_grants().')
    grant_view = models.PositiveIntegerField(db_comment='Boolean indicating whether a user with the realm/grant pair can view this node.')
    grant_update = models.PositiveIntegerField(db_comment='Boolean indicating whether a user with the realm/grant pair can edit this node.')
    grant_delete = models.PositiveIntegerField(db_comment='Boolean indicating whether a user with the realm/grant pair can delete this node.')

    class Meta:
        managed = False
        db_table = 'node_access'
        unique_together = (('nid', 'gid', 'realm', 'langcode'),)
        db_table_comment = 'Identifies which realm/grant pairs a user must possess in…'


class NodeFieldData(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)  # The composite primary key (nid, langcode) found, that is not supported. The first column is selected.
    vid = models.PositiveIntegerField()
    type = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The ID of the target entity.')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    status = models.IntegerField()
    title = models.CharField(max_length=255)
    uid = models.PositiveIntegerField(db_comment='The ID of the target entity.')
    created = models.IntegerField()
    changed = models.IntegerField()
    promote = models.IntegerField()
    sticky = models.IntegerField()
    default_langcode = models.IntegerField()
    revision_translation_affected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_field_data'
        unique_together = (('nid', 'langcode'),)
        db_table_comment = 'The data table for node entities.'


class NodeFieldRevision(models.Model):
    nid = models.PositiveIntegerField()
    vid = models.PositiveIntegerField(primary_key=True)  # The composite primary key (vid, langcode) found, that is not supported. The first column is selected.
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    status = models.IntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)
    uid = models.PositiveIntegerField(db_comment='The ID of the target entity.')
    created = models.IntegerField(blank=True, null=True)
    changed = models.IntegerField(blank=True, null=True)
    promote = models.IntegerField(blank=True, null=True)
    sticky = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()
    revision_translation_affected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_field_revision'
        unique_together = (('vid', 'langcode'),)
        db_table_comment = 'The revision data table for node entities.'


class NodeRevision(models.Model):
    nid = models.PositiveIntegerField()
    vid = models.AutoField(primary_key=True)
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    revision_uid = models.PositiveIntegerField(blank=True, null=True, db_comment='The ID of the target entity.')
    revision_timestamp = models.IntegerField(blank=True, null=True)
    revision_log = models.TextField(blank=True, null=True)
    revision_default = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_revision'
        db_table_comment = 'The revision table for node entities.'


class NodeRevisionBody(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    body_value = models.TextField()
    body_summary = models.TextField(blank=True, null=True)
    body_format = models.CharField(max_length=255, db_collation='ascii_general_ci', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'node_revision__body'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field body.'


class NodeRevisionFieldArea(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_area_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_area'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_area.'


class NodeRevisionFieldCam(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_cam_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_cam'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_cam.'


class NodeRevisionFieldCat(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_cat_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_revision__field_cat'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_cat.'


class NodeRevisionFieldCatalogue(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_catalogue_target_id = models.PositiveIntegerField(db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'node_revision__field_catalogue'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_catalogue.'


class NodeRevisionFieldComm(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_comm_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_comm'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_comm.'


class NodeRevisionFieldCopyrightInformation(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_copyright_information_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_copyright_information'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_copyright…'


class NodeRevisionFieldDamend(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_damend_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_revision__field_damend'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_damend.'


class NodeRevisionFieldDate(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_date_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_revision__field_date'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_date.'


class NodeRevisionFieldDinput(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_dinput_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_revision__field_dinput'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_dinput.'


class NodeRevisionFieldDisc(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_disc_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_revision__field_disc'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_disc.'


class NodeRevisionFieldFlin(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_flin_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_flin'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_flin.'


class NodeRevisionFieldFw(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_fw_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_fw'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_fw.'


class NodeRevisionFieldInf(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_inf_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_inf'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_inf.'


class NodeRevisionFieldIns(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_ins_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_ins'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_ins.'


class NodeRevisionFieldInstruments(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_instruments_target_id = models.PositiveIntegerField(db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'node_revision__field_instruments'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_instruments.'


class NodeRevisionFieldNumb(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_numb_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_revision__field_numb'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_numb.'


class NodeRevisionFieldParentDisc(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_parent_disc_target_id = models.PositiveIntegerField(db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'node_revision__field_parent_disc'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_parent_disc.'


class NodeRevisionFieldPlac(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_plac_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_revision__field_plac'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_plac.'


class NodeRevisionFieldRef(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_ref_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_revision__field_ref'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_ref.'


class NodeRevisionFieldRl(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_rl_value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_revision__field_rl'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_rl.'


class NodeRevisionFieldSumm(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_summ_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_summ'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_summ.'


class NodeRevisionFieldTale(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_tale_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_tale'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_tale.'


class NodeRevisionFieldTitl(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_titl_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_titl'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_titl.'


class NodeRevisionFieldType(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_type_value = models.TextField()

    class Meta:
        managed = False
        db_table = 'node_revision__field_type'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_type.'


class NodeRevisionFieldTypes(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    field_types_target_id = models.PositiveIntegerField(db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'node_revision__field_types'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for node field field_types.'


class Old5E00A5UrlAlias(models.Model):
    pid = models.AutoField(primary_key=True, db_comment='A unique path alias identifier.')
    source = models.CharField(max_length=255, db_comment='The Drupal path this alias is for. e.g. node/12.')
    alias = models.CharField(max_length=255, db_comment='The alias for this path. e.g. title-of-the-story.')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci', db_comment="The language code this alias is for. if 'und', the alias will be used for unknown languages. Each Drupal path can have an alias for each supported language.")

    class Meta:
        managed = False
        db_table = 'old_5e00a5_url_alias'
        db_table_comment = 'A list of URL aliases for Drupal paths. a user may visit…'


class Old9Caed2MenuLinkContent(models.Model):
    bundle = models.CharField(max_length=32, db_collation='ascii_general_ci')
    uuid = models.CharField(unique=True, max_length=128, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')

    class Meta:
        managed = False
        db_table = 'old_9caed2menu_link_content'
        db_table_comment = 'The base table for menu_link_content entities.'


class Old9Caed2MenuLinkContentData(models.Model):
    id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (id, langcode) found, that is not supported. The first column is selected.
    bundle = models.CharField(max_length=32, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    menu_name = models.CharField(max_length=255, db_collation='ascii_general_ci', blank=True, null=True)
    link_uri = models.CharField(db_column='link__uri', max_length=2048, blank=True, null=True, db_comment='The URI of the link.')  # Field renamed because it contained more than one '_' in a row.
    link_title = models.CharField(db_column='link__title', max_length=255, blank=True, null=True, db_comment='The link text.')  # Field renamed because it contained more than one '_' in a row.
    link_options = models.TextField(db_column='link__options', blank=True, null=True, db_comment='Serialized array of options for the link.')  # Field renamed because it contained more than one '_' in a row.
    external = models.IntegerField(blank=True, null=True)
    rediscover = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    expanded = models.IntegerField(blank=True, null=True)
    parent = models.CharField(max_length=255, blank=True, null=True)
    changed = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'old_9caed2menu_link_content_data'
        unique_together = (('id', 'langcode'),)
        db_table_comment = 'The data table for menu_link_content entities.'


class OldCa0339TaxonomyTermParent(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to, which for an unversioned entity type is the same as the entity id')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    parent_target_id = models.PositiveIntegerField(db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'old_ca0339taxonomy_term__parent'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for taxonomy_term field parent.'


class OldCa0339TaxonomyTermData(models.Model):
    tid = models.AutoField(primary_key=True)
    vid = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The ID of the target entity.')
    uuid = models.CharField(unique=True, max_length=128, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')

    class Meta:
        managed = False
        db_table = 'old_ca0339taxonomy_term_data'
        db_table_comment = 'The base table for taxonomy_term entities.'


class OldCa0339TaxonomyTermFieldData(models.Model):
    tid = models.PositiveIntegerField(primary_key=True)  # The composite primary key (tid, langcode) found, that is not supported. The first column is selected.
    vid = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The ID of the target entity.')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    name = models.CharField(max_length=255)
    description_value = models.TextField(db_column='description__value', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    description_format = models.CharField(db_column='description__format', max_length=255, db_collation='ascii_general_ci', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    weight = models.IntegerField()
    changed = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'old_ca0339taxonomy_term_field_data'
        unique_together = (('tid', 'langcode'),)
        db_table_comment = 'The data table for taxonomy_term entities.'


class PathAlias(models.Model):
    revision_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=128, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    path = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'path_alias'
        db_table_comment = 'The base table for path_alias entities.'


class PathAliasRevision(models.Model):
    id = models.PositiveIntegerField()
    revision_id = models.AutoField(primary_key=True)
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    path = models.CharField(max_length=255, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    revision_default = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'path_alias_revision'
        db_table_comment = 'The revision table for path_alias entities.'


class Queue(models.Model):
    item_id = models.AutoField(primary_key=True, db_comment='Primary Key: Unique item ID.')
    name = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The queue name.')
    data = models.TextField(blank=True, null=True, db_comment='The arbitrary data for the item.')
    expire = models.BigIntegerField(db_comment='Timestamp when the claim lease expires on the item.')
    created = models.BigIntegerField(db_comment='Timestamp when the item was created.')

    class Meta:
        managed = False
        db_table = 'queue'
        db_table_comment = 'Stores items in queues.'


class Router(models.Model):
    name = models.CharField(primary_key=True, max_length=255, db_collation='ascii_general_ci', db_comment='Primary Key: Machine name of this route')
    path = models.CharField(max_length=255, db_comment='The path for this URI')
    pattern_outline = models.CharField(max_length=255, db_comment='The pattern')
    fit = models.IntegerField(db_comment='A numeric representation of how specific the path is.')
    route = models.TextField(blank=True, null=True, db_comment='A serialized Route object')
    number_parts = models.SmallIntegerField(db_comment='Number of parts in this router path.')

    class Meta:
        managed = False
        db_table = 'router'
        db_table_comment = 'Maps paths to various callbacks (access, page and title)'


class SearchApiTask(models.Model):
    type = models.CharField(max_length=50, blank=True, null=True)
    server_id = models.CharField(max_length=50, blank=True, null=True)
    index_id = models.CharField(max_length=50, blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_api_task'
        db_table_comment = 'The base table for search_api_task entities.'


class SearchDataset(models.Model):
    sid = models.PositiveIntegerField(primary_key=True, db_comment='Search item ID, e.g. node ID for nodes.')  # The composite primary key (sid, langcode, type) found, that is not supported. The first column is selected.
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci', db_comment='The languages.langcode of the item variant.')
    type = models.CharField(max_length=64, db_collation='ascii_general_ci', db_comment='Type of item, e.g. node.')
    data = models.TextField(db_comment='List of space-separated words from the item.')
    reindex = models.PositiveIntegerField(db_comment='Set to force node reindexing.')

    class Meta:
        managed = False
        db_table = 'search_dataset'
        unique_together = (('sid', 'langcode', 'type'),)
        db_table_comment = 'Stores items that will be searched.'


class SearchIndex(models.Model):
    word = models.CharField(primary_key=True, max_length=50, db_comment='The search_total.word that is associated with the search item.')  # The composite primary key (word, sid, langcode, type) found, that is not supported. The first column is selected.
    sid = models.PositiveIntegerField(db_comment='The search_dataset.sid of the searchable item to which the word belongs.')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci', db_comment='The languages.langcode of the item variant.')
    type = models.CharField(max_length=64, db_collation='ascii_general_ci', db_comment='The search_dataset.type of the searchable item to which the word belongs.')
    score = models.FloatField(blank=True, null=True, db_comment='The numeric score of the word, higher being more important.')

    class Meta:
        managed = False
        db_table = 'search_index'
        unique_together = (('word', 'sid', 'langcode', 'type'),)
        db_table_comment = 'Stores the search index, associating words, items and…'


class SearchTotal(models.Model):
    word = models.CharField(primary_key=True, max_length=50, db_comment='Primary Key: Unique word in the search index.')
    count = models.FloatField(blank=True, null=True, db_comment="The count of the word in the index using Zipf's law to equalize the probability distribution.")

    class Meta:
        managed = False
        db_table = 'search_total'
        db_table_comment = 'Stores search totals for words.'


class Semaphore(models.Model):
    name = models.CharField(primary_key=True, max_length=255, db_collation='ascii_general_ci', db_comment='Primary Key: Unique name.')
    value = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='A value for the semaphore.')
    expire = models.FloatField(db_comment='A Unix timestamp with microseconds indicating when the semaphore should expire.')

    class Meta:
        managed = False
        db_table = 'semaphore'
        db_table_comment = 'Table for holding semaphores, locks, flags, etc. that…'


class Sequences(models.Model):
    value = models.AutoField(primary_key=True, db_comment='The value of the sequence.')

    class Meta:
        managed = False
        db_table = 'sequences'
        db_table_comment = 'Stores IDs.'


class Sessions(models.Model):
    uid = models.PositiveIntegerField(db_comment='The users.uid corresponding to a session, or 0 for anonymous user.')
    sid = models.CharField(primary_key=True, max_length=128, db_collation='ascii_general_ci', db_comment="A session ID (hashed). The value is generated by Drupal's session handlers.")
    hostname = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The IP address that last used this session ID (sid).')
    timestamp = models.BigIntegerField(db_comment='The Unix timestamp when this session last requested a page. Old records are purged by PHP automatically.')
    session = models.TextField(blank=True, null=True, db_comment='The serialized contents of $_SESSION, an array of name/value pairs that persists across page requests by this session ID. Drupal loads $_SESSION from here at the start of each request and saves it at the end.')

    class Meta:
        managed = False
        db_table = 'sessions'
        db_table_comment = "Drupal's session handlers read and write into the sessions…"


class Shortcut(models.Model):
    shortcut_set = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The ID of the target entity.')
    uuid = models.CharField(unique=True, max_length=128, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')

    class Meta:
        managed = False
        db_table = 'shortcut'
        db_table_comment = 'The base table for shortcut entities.'


class ShortcutFieldData(models.Model):
    id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (id, langcode) found, that is not supported. The first column is selected.
    shortcut_set = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The ID of the target entity.')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    title = models.CharField(max_length=255, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    link_uri = models.CharField(db_column='link__uri', max_length=2048, blank=True, null=True, db_comment='The URI of the link.')  # Field renamed because it contained more than one '_' in a row.
    link_title = models.CharField(db_column='link__title', max_length=255, blank=True, null=True, db_comment='The link text.')  # Field renamed because it contained more than one '_' in a row.
    link_options = models.TextField(db_column='link__options', blank=True, null=True, db_comment='Serialized array of options for the link.')  # Field renamed because it contained more than one '_' in a row.
    default_langcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shortcut_field_data'
        unique_together = (('id', 'langcode'),)
        db_table_comment = 'The data table for shortcut entities.'


class ShortcutSetUsers(models.Model):
    uid = models.PositiveIntegerField(primary_key=True, db_comment='The users.uid for this set.')
    set_name = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The shortcut_set.set_name that will be displayed for this user.')

    class Meta:
        managed = False
        db_table = 'shortcut_set_users'
        db_table_comment = 'Maps users to shortcut sets.'


class TaxonomyIndex(models.Model):
    nid = models.PositiveIntegerField(primary_key=True, db_comment='The node.nid this record tracks.')  # The composite primary key (nid, tid) found, that is not supported. The first column is selected.
    tid = models.PositiveIntegerField(db_comment='The term ID.')
    status = models.IntegerField(db_comment='Boolean indicating whether the node is published (visible to non-administrators).')
    sticky = models.IntegerField(blank=True, null=True, db_comment='Boolean indicating whether the node is sticky.')
    created = models.IntegerField(db_comment='The Unix timestamp when the node was created.')

    class Meta:
        managed = False
        db_table = 'taxonomy_index'
        unique_together = (('nid', 'tid'),)
        db_table_comment = 'Maintains denormalized information about node/term…'


class TaxonomyTermParent(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    parent_target_id = models.PositiveIntegerField(db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'taxonomy_term__parent'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for taxonomy_term field parent.'


class TaxonomyTermData(models.Model):
    tid = models.AutoField(primary_key=True)
    revision_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    vid = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The ID of the target entity.')
    uuid = models.CharField(unique=True, max_length=128, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')

    class Meta:
        managed = False
        db_table = 'taxonomy_term_data'
        db_table_comment = 'The base table for taxonomy_term entities.'


class TaxonomyTermFieldData(models.Model):
    tid = models.PositiveIntegerField(primary_key=True)  # The composite primary key (tid, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField()
    vid = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The ID of the target entity.')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    name = models.CharField(max_length=255)
    description_value = models.TextField(db_column='description__value', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    description_format = models.CharField(db_column='description__format', max_length=255, db_collation='ascii_general_ci', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    weight = models.IntegerField()
    changed = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()
    status = models.IntegerField()
    revision_translation_affected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxonomy_term_field_data'
        unique_together = (('tid', 'langcode'),)
        db_table_comment = 'The data table for taxonomy_term entities.'


class TaxonomyTermFieldRevision(models.Model):
    tid = models.PositiveIntegerField()
    revision_id = models.PositiveIntegerField(primary_key=True)  # The composite primary key (revision_id, langcode) found, that is not supported. The first column is selected.
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    name = models.CharField(max_length=255, blank=True, null=True)
    description_value = models.TextField(db_column='description__value', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    description_format = models.CharField(db_column='description__format', max_length=255, db_collation='ascii_general_ci', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    changed = models.IntegerField(blank=True, null=True)
    default_langcode = models.IntegerField()
    status = models.IntegerField()
    revision_translation_affected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxonomy_term_field_revision'
        unique_together = (('revision_id', 'langcode'),)
        db_table_comment = 'The revision data table for taxonomy_term entities.'


class TaxonomyTermRevision(models.Model):
    tid = models.PositiveIntegerField()
    revision_id = models.AutoField(primary_key=True)
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    revision_default = models.IntegerField(blank=True, null=True)
    revision_user = models.PositiveIntegerField(blank=True, null=True, db_comment='The ID of the target entity.')
    revision_created = models.IntegerField(blank=True, null=True)
    revision_log_message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxonomy_term_revision'
        db_table_comment = 'The revision table for taxonomy_term entities.'


class TaxonomyTermRevisionParent(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, revision_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    parent_target_id = models.PositiveIntegerField(db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'taxonomy_term_revision__parent'
        unique_together = (('entity_id', 'revision_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Revision archive storage for taxonomy_term field parent.'


class UserRoles(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to, which for an unversioned entity type is the same as the entity id')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    roles_target_id = models.CharField(max_length=255, db_collation='ascii_general_ci', db_comment='The ID of the target entity.')

    class Meta:
        managed = False
        db_table = 'user__roles'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for user field roles.'


class UserUserPicture(models.Model):
    bundle = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The field instance bundle to which this row belongs, used when deleting a field instance')
    deleted = models.IntegerField(db_comment='A boolean indicating whether this data item has been deleted')
    entity_id = models.PositiveIntegerField(primary_key=True, db_comment='The entity id this data is attached to')  # The composite primary key (entity_id, deleted, delta, langcode) found, that is not supported. The first column is selected.
    revision_id = models.PositiveIntegerField(db_comment='The entity revision id this data is attached to, which for an unversioned entity type is the same as the entity id')
    langcode = models.CharField(max_length=32, db_collation='ascii_general_ci', db_comment='The language code for this data item.')
    delta = models.PositiveIntegerField(db_comment='The sequence number for this data item, used for multi-value fields')
    user_picture_target_id = models.PositiveIntegerField(db_comment='The ID of the file entity.')
    user_picture_alt = models.CharField(max_length=512, blank=True, null=True, db_comment="Alternative image text, for the image's 'alt' attribute.")
    user_picture_title = models.CharField(max_length=1024, blank=True, null=True, db_comment="Image title text, for the image's 'title' attribute.")
    user_picture_width = models.PositiveIntegerField(blank=True, null=True, db_comment='The width of the image in pixels.')
    user_picture_height = models.PositiveIntegerField(blank=True, null=True, db_comment='The height of the image in pixels.')

    class Meta:
        managed = False
        db_table = 'user__user_picture'
        unique_together = (('entity_id', 'deleted', 'delta', 'langcode'),)
        db_table_comment = 'Data storage for user field user_picture.'


class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=128, db_collation='ascii_general_ci')
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')

    class Meta:
        managed = False
        db_table = 'users'
        db_table_comment = 'The base table for user entities.'


class UsersData(models.Model):
    uid = models.PositiveIntegerField(primary_key=True, db_comment='Primary key: users.uid for user.')  # The composite primary key (uid, module, name) found, that is not supported. The first column is selected.
    module = models.CharField(max_length=50, db_collation='ascii_general_ci', db_comment='The name of the module declaring the variable.')
    name = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='The identifier of the data.')
    value = models.TextField(blank=True, null=True, db_comment='The value.')
    serialized = models.PositiveIntegerField(blank=True, null=True, db_comment='Whether value is serialized.')

    class Meta:
        managed = False
        db_table = 'users_data'
        unique_together = (('uid', 'module', 'name'),)
        db_table_comment = 'Stores module data as key/value pairs per user.'


class UsersFieldData(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)  # The composite primary key (uid, langcode) found, that is not supported. The first column is selected.
    langcode = models.CharField(max_length=12, db_collation='ascii_general_ci')
    preferred_langcode = models.CharField(max_length=12, db_collation='ascii_general_ci', blank=True, null=True)
    preferred_admin_langcode = models.CharField(max_length=12, db_collation='ascii_general_ci', blank=True, null=True)
    name = models.CharField(max_length=60)
    pass_field = models.CharField(db_column='pass', max_length=255, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    mail = models.CharField(max_length=254, blank=True, null=True)
    timezone = models.CharField(max_length=32, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created = models.IntegerField()
    changed = models.IntegerField(blank=True, null=True)
    access = models.IntegerField()
    login = models.IntegerField(blank=True, null=True)
    init = models.CharField(max_length=254, blank=True, null=True)
    default_langcode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_field_data'
        unique_together = (('uid', 'langcode'), ('name', 'langcode'),)
        db_table_comment = 'The data table for user entities.'


class Watchdog(models.Model):
    wid = models.BigAutoField(primary_key=True, db_comment='Primary Key: Unique watchdog event ID.')
    uid = models.PositiveIntegerField(db_comment='The users.uid of the user who triggered the event.')
    type = models.CharField(max_length=64, db_collation='ascii_general_ci', db_comment='Type of log message, for example "user" or "page not found."')
    message = models.TextField(db_comment='Text of log message to be passed into the t() function.')
    variables = models.TextField(db_comment='Serialized array of variables that match the message string and that is passed into the t() function.')
    severity = models.PositiveIntegerField(db_comment='The severity level of the event. ranges from 0 (Emergency) to 7 (Debug)')
    link = models.TextField(blank=True, null=True, db_comment='Link to view the result of the event.')
    location = models.TextField(db_comment='URL of the origin of the event.')
    referer = models.TextField(blank=True, null=True, db_comment='URL of referring page.')
    hostname = models.CharField(max_length=128, db_collation='ascii_general_ci', db_comment='Hostname of the user who triggered the event.')
    timestamp = models.BigIntegerField(db_comment='Unix timestamp of when event occurred.')

    class Meta:
        managed = False
        db_table = 'watchdog'
        db_table_comment = 'Table that contains logs of all system events.'
