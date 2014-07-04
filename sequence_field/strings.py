# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

# Sequence Field

SEQUENCE_KEY = _(u'Key')
SEQUENCE_VALUE = _(u'Value')
SEQUENCE_TEMPLATE = _(u'Template')
SEQUENCE_CREATED = _(u'Created at')
SEQUENCE_UPDATED = _(u'Updated at')

SEQUENCE_MODEL_NAME = _(u'Sequence')
SEQUENCE_MODEL_NAME_PLURAL = _(u'Sequences')

SEQUENCE_FIELD_DESCRIPTION = _(u'Templated sequence object')

# Errors

SEQUENCE_FIELD_PATTERN_MISMATCH = _(
    u'The value does not match the specified pattern'
)

SEQUENCE_FIELD_MISSING_KEY = _(
    u'The key parameter is mandatory and is missing'
)

SEQUENCE_FIELD_KEY_MISMATCH = _(
    u'The key \'%(key)s\' does not match any of the existing '
    u'sequence model objects'
)
