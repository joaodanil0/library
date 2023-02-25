from django import template


register = template.Library()

@register.filter
def show_borrow_duration(start_date, end_date):
    return (end_date - start_date).days