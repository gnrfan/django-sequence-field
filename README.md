Django Sequence Field
=====================

A Django field for creating templated sequenced strings.

Usage:

Importing and using the SequenceField class:

```python
from sequence_field.fields import SequenceField

# Create your models here.

class TestModel(models.Model):

    sequence = SequenceField(
        key='test.sequence.1',
        template='%Y%m%d%(code)s%NNNNN',
        params={'code':'ABC'},
        auto=True
    )
 
```

When creating new objects, the sequence is generated automatically 
based on the template:


```python
from my_app.models import TestModel

obj = TestModel()
obj.save()

print obj.sequence # 20140703ABC00001

obj = TestModel()
obj.save()

print obj.sequence # 20140703ABC00002
```

An accompaning ```Sequence``` model is used by this app to store the
current value for each key. When a new key is declared in a field a 
new ```Sequence``` instance is created and saved on the fly.

If you need to customize the creation of each sequence value passing 
different parameters you'll have to do it at the model level with 
code like this:

```python
from sequence_field.models import Sequence
print Sequence.next(
  'test.sequence.1', template='%Y%m%d%(code)s%NNNNN', params={'code':'XYZ'}
) # 20140703XYZ00003
```

Templates can also be stored in the database so you don't have to pass them
all the time. If a template is provided the first time a key is used it gets
automatically stored.

```python
>>> from sequence_field.models import Sequence
>>> Sequence.next('test.sequence.20', template='%m%d%Y-%NNNNNNNNNNN')
'07042014-00000000001'
>>> Sequence.next('test.sequence.20')
'07042014-00000000002'
```

You can use the provided Expander classes or build your own. 
As an example see the code for the ```TimeExpander``` class the uses
Python's ```strftime``` function to perform time-related expansions:

```python
class TimeExpander(BaseExpander):                                               
                                                                                
    def expand(self, template=None, count=None, params={}, value=None):         
        import time                                                             
        (template, count, params, value) = self.setvars(                        
            template, count, params, value                                      
        )                                                                       
        return time.strftime(value)
```

The default expanders are: (taken from the ```constants.py``` file)

```python
SEQUENCE_FIELD_DEFAULT_EXPANDERS = (                                            
    'sequence_field.expanders.NumericExpander',                                 
    'sequence_field.expanders.TimeExpander',                                    
    'sequence_field.expanders.ParameterExpander',                               
) 
```

At your Django project's ```settings.py``` file you can customize this 
variables: (default values are shown)

```python
SEQUENCE_FIELD_DEFAULT_VALUE # 1

SEQUENCE_FIELD_ADMIN # True

SEQUENCE_FIELD_DEFAULT_TEMPLATE # '%N'

SEQUENCE_FIELD_DEFAULT_PATTERN #  r'(\d+)'

SEQUENCE_FIELD_DEFAULT_EXPANDERS # Already mentioned in the previous section.
```

Installation from Github
========================

```pip install https://github.com/gnrfan/django-sequence-field/zipball/master```

(c) 2014 Antonio Ognio <antonio@ognio.com>
