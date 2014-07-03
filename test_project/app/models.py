from django.db import models
from sequence_field.fields import SequenceField
from app import strings

# Create your models here.

class TestModel(models.Model):

    sequence = SequenceField(
        verbose_name=strings.TESTMODEL_SEQUENCE,
        key='test.sequence.2',
        template='%Y%m%d%(code)s%NNNNN',
        params={'code':'ABC'},
        auto=True
    )

    created = models.DateTimeField(
        verbose_name=strings.TESTMODEL_CREATED,
        auto_now_add=True
    )

    updated = models.DateTimeField(
        verbose_name=strings.TESTMODEL_UPDATED,
        auto_now=True
    )

    class Meta:
        verbose_name = strings.TESTMODEL_MODEL_NAME
        verbose_name_plural = strings.TESTMODEL_MODEL_NAME_PLURAL

    def __unicode__(self):
        return self.sequence
