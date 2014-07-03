# -*- coding: utf-8 -*-

from django.db import models
from sequence_field import utils
from sequence_field import strings
from sequence_field import constants
from sequence_field import settings as sequence_field_settings

# Sequence Field

class Sequence(models.Model):

    key = models.CharField(
        verbose_name=strings.SEQUENCE_KEY,
        max_length=constants.SEQUENCE_KEY_LENGTH,
        unique=True
    )

    value = models.PositiveIntegerField(
        verbose_name=strings.SEQUENCE_VALUE,
        default=constants.SEQUENCE_DEFAULT_VALUE
    )

    created = models.DateTimeField(
        verbose_name=strings.SEQUENCE_CREATED,
        auto_now_add=True
    )

    updated = models.DateTimeField(
        verbose_name=strings.SEQUENCE_UPDATED,
        auto_now=True
    )

    class Meta:
        verbose_name = strings.SEQUENCE_MODEL_NAME
        verbose_name_plural = strings.SEQUENCE_MODEL_NAME_PLURAL

    def __unicode__(self):
        return self.key

    def increment(self, commit=True):
        self.value += 1
        if commit:
            self.save()

    def next_value(self, template=None, params=None, 
                   expanders=None, commit=True):
        
        default_template = \
            sequence_field_settings.SEQUENCE_FIELD_DEFAULT_TEMPLATE

        default_expanders = \
            sequence_field_settings.SEQUENCE_FIELD_DEFAULT_EXPANDERS

        count = self.value
        template = template if template is not None else default_template
        params = params if params is not None else {}
        expanders = expanders if expanders is not None else default_expanders
        if commit:
            self.increment()
        return utils.expand(template, count, params, expanders=expanders)

    @classmethod
    def next(cls, key, template=None, params=None, 
            expanders=None, commit=True):
        seq = Sequence.objects.get(key=key)
        return seq.next_value(template, params, expanders, commit)
