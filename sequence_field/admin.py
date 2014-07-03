from django.contrib import admin
from sequence_field.models import Sequence
from sequence_field import settings as sequence_field_settings

# Sequence Field

class SequenceAdmin(admin.ModelAdmin):

    list_display = (
        'id', 'key', 'value', 'created', 'updated'
    )

    readonly_fields = ('created', 'updated', )

    ordering = ('key', )


if sequence_field_settings.SEQUENCE_FIELD_ADMIN:
    admin.site.register(Sequence, SequenceAdmin)

