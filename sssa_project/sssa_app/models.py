from django.db import models

# Create your models here.
# Tables need to transfer: node_field_comm where , node__field_type, node__field_fw
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

    def __str__(self):
        return self.nid

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