from django import template

register = template.Library()

@register.filter
def get_attr(obj, attr_path):
    try:
        for part in attr_path.split('__'):
            obj = getattr(obj, part)
            if callable(obj):
                obj = obj()
        return obj
    except Exception:
        return ''