from django import template
from django.utils.safestring import mark_safe
from apps.permissions import models as permissions_models
register = template.Library()

@register.simple_tag
def role_group(user):
    return user.roles.values("title")[0]["title"]

@register.simple_tag
def role_id(role_title):
    return permissions_models.Role.objects.filter(title=role_title).values('id')[0]['id']

@register.simple_tag
def get_menu_caption(group_id):
    caption = permissions_models.Menu.objects.filter(id=int(group_id)).values('caption')[0]['caption']
    return caption

@register.simple_tag
def change_input_value(obj):
    print(obj)
    return 1111
