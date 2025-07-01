from django import template
from django.forms import DateField, DateInput

register = template.Library()
    
@register.filter
def get_item(dictionary, key):
    try:
        return dictionary.get(key, '')
    except Exception:
        return ''
    
@register.filter(name='add_class')
def add_class(field, css_class="form-control"):
    widget_type = field.field.widget.__class__.__name__.lower()
    attrs = {}

    # Special handling for date fields - change the widget type
    if isinstance(field.field, DateField):
        field.field.widget = DateInput(attrs={
            'class': 'form-control form-control-user',
            'type': 'date'
        })
        return field.as_widget()
    elif 'select' in widget_type:
        attrs['class'] = 'form-select'
    elif 'textarea' in widget_type:
        attrs['class'] = 'form-control'
    elif 'dateinput' in widget_type or 'splitdatetimewidget' in widget_type:
        # Asegura que sea date picker nativo
        attrs['class'] = 'form-control form-control-user'
        attrs['type'] = 'date'
    else:
        attrs['class'] = 'form-control form-control-user'

    return field.as_widget(attrs=attrs)

