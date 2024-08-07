from django import template
from datetime import datetime

register = template.Library()

@register.filter
def format_datetime(value, date_format='%B %d, %Y'):
    try:
        dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
        return dt.strftime(date_format)
    except (ValueError, TypeError):
        return value  # If the value is not a valid datetime string, return it as is
