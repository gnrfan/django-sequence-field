# Sequence Field constants

SEQUENCE_KEY_LENGTH = 128

SEQUENCE_TEMPLATE_LENGTH = 128

SEQUENCE_DEFAULT_VALUE = 1

SEQUENCE_FIELD_ADMIN = True

SEQUENCE_FIELD_DEFAULT_PATTERN = r'(\d+)'

SEQUENCE_FIELD_DEFAULT_TEMPLATE = '%N'

SEQUENCE_FIELD_DEFAULT_EXPANDERS = (
    'sequence_field.expanders.NumericExpander',
    'sequence_field.expanders.TimeExpander',
    'sequence_field.expanders.ParameterExpander',
)
