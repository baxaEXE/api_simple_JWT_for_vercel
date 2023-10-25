from django.contrib.admin import *
from apps.guest.models import Guest

@register(Guest)

class GuestAdmin(ModelAdmin):
    list_display = ('first_name','last_name','email','phone_number')
    list_display_links =  ('first_name','last_name','email','phone_number')

