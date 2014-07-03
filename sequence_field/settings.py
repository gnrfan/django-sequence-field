# Sequence Field Settings

from django.conf import settings
from sequence_field import constants

SEQUENCE_FIELD_ADMIN = getattr(
    settings,
    'SEQUENCE_FIELD_ADMIN',
    constants.SEQUENCE_FIELD_ADMIN
)
