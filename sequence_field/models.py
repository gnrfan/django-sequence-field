# -*- coding: utf-8 -*-

from django.db import models
from sequence_field import strings
from sequence_field import constants

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
