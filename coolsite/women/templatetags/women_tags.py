from django import template
from women.models import *
from women.views import menu

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filters=None):
    if not filters:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filters)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {"cats": cats, "cat_selected": cat_selected}


@register.simple_tag(name='showmenu')
def show_menu():
    return menu

