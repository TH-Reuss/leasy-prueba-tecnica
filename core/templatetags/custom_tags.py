from django import template
from django.forms import DateField, DateInput, Select

register = template.Library()
    
@register.filter
def get_item(dictionary, key):
    try:
        return dictionary.get(key, '')
    except Exception:
        return ''
    
@register.filter(name='add_class')
def add_class(field, css_class=None):
    """
    Filter to add proper bootstrap classes to a form field.
    Also handles rendering of DateField as <input type="date">.
    """
    widget = field.field.widget
    
    # Determine base class
    if isinstance(widget, Select):
        base_class = 'form-select'
    else:
        base_class = 'form-control form-control-user'
        
    if css_class:
        final_class = f'{base_class} {css_class}'
    else:
        final_class = base_class
        
    attrs = {'class': final_class}

    if isinstance(field.field, DateField):
        date_widget = DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        return field.as_widget(widget=date_widget, attrs=attrs)
        
    return field.as_widget(attrs=attrs)

