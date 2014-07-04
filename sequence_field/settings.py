# Sequence Field Settings

from django.conf import settings
from sequence_field import constants


SEQUENCE_FIELD_DEFAULT_VALUE = getattr(
    settings,
    'SEQUENCE_FIELD_DEFAULT_VALUE',
    constants.SEQUENCE_DEFAULT_VALUE
)

SEQUENCE_FIELD_ADMIN = getattr(
    settings,
    'SEQUENCE_FIELD_ADMIN',
    constants.SEQUENCE_FIELD_ADMIN
)

SEQUENCE_FIELD_DEFAULT_TEMPLATE = getattr(
    settings,
    'SEQUENCE_FIELD_DEFAULT_TEMPLATE',
    constants.SEQUENCE_FIELD_DEFAULT_TEMPLATE
)

SEQUENCE_FIELD_DEFAULT_PATTERN = getattr(
    settings,
    'SEQUENCE_FIELD_DEFAULT_PATTERN',
    constants.SEQUENCE_FIELD_DEFAULT_PATTERN
)

SEQUENCE_FIELD_DEFAULT_EXPANDERS = getattr(
    settings,
    'SEQUENCE_FIELD_DEFAULT_EXPANDERS',
    constants.SEQUENCE_FIELD_DEFAULT_EXPANDERS
)
