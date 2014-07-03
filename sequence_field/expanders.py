# -*- coding: utf-8 -*-

# Sequence Field Expanders

import re

class BaseExpander(object):

    def __init__(self, template=None, count=None, params={}, value=None):
        self.template = template
        self.count = count
        self.params = params
        self.value = value

    def setvars(self, template=None, count=None, params={}, value=None):
        # Parameters take precedence over attributes
        template = template if template is not None else self.template
        count = count if count is not None else self.count
        params = params if len(params)>0 else self.params
        value = value if value is not None else self.value
        # Copy current value from template
        if value is None or len(value) == 0:
            value = template
        return (template, count, params, value, )

    def expand(self, template=None, count=None, params={}, value=None):
        # Do nothing, just return the value
        (template, count, params, value) = self.setvars(
            template, count, params, value
        )
        return value


class NumericExpander(BaseExpander):

    regexp = r'^(.*)(?P<numeric_placeholder>%N+)(.*)$'

    def __init__(self, template=None, count=None, params={}, value=None):
        super(NumericExpander, self).__init__(template, count, params, value)
        self.format = '%d'

    def set_format_from_numeric_placeholder(self, numeric_placeholder):
        format = '%%0%dd' % len(numeric_placeholder.replace('%', ''))
        self.format = format

    def expand_count(self, count=None):
        if count is None:
            count = self.count
        return self.format % count

    def get_numeric_placeholder_from_groupdict(self, groupdict):
        if 'numeric_placeholder' in groupdict:
            return groupdict['numeric_placeholder']
        else:
            return ''

    def get_numeric_placeholder(self, template=None):
        if template is None:
            template = self.template
        match = re.match(self.regexp, template)
        if match is not None:
            return self.get_numeric_placeholder_from_groupdict(
                match.groupdict()
            )
        else:
            return None

    def expand_with_expanded_count(self, expanded_count, value=None):
        if value is None:
            value = self.value
        parts = [
            re.sub(self.regexp, r'\1', value),
            expanded_count,
            re.sub(self.regexp, r'\3', value)
        ]
        return ''.join(parts)

    def expand(self, template=None, count=None, params={}, value=None):
        (template, count, params, value) = self.setvars(
            template, count, params, value
        )
        numeric_placeholder = self.get_numeric_placeholder()
        self.set_format_from_numeric_placeholder(numeric_placeholder)
        expanded_count = self.expand_count()
        value = self.expand_with_expanded_count(expanded_count, value)
        return value


class ParameterExpander(BaseExpander):

    def expand(self, template=None, count=None, params={}, value=None):
        (template, count, params, value) = self.setvars(
            template, count, params, value
        )
        return value % params


class TimeExpander(BaseExpander):

    def expand(self, template=None, count=None, params={}, value=None):
        import time
        (template, count, params, value) = self.setvars(
            template, count, params, value
        )
        return time.strftime(value)
