from django import template

register = template.Library()

@register.filter
def status_score(status):
    score_mapping = {
        'pending': 1,
        'info_received': 2,
        'in_transit': 3,
        'out_for_delivery': 4,
        'delivered': 5
    }
    return score_mapping.get(status, 0)  # Default to 0 if status is not found
