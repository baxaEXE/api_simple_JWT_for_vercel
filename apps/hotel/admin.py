from django.contrib.admin import *
from .models import Hotel
@register(Hotel)

class HotelAdmin(ModelAdmin):
    list_display = ('name','address','city','country','rating')
    list_display_links = ('name','address','city','country','rating')


