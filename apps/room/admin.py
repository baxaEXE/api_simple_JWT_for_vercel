from django.contrib.admin import *
from .models import Room

@register(Room)

class RoomAdmin(ModelAdmin):
    list_display = ('hotel','number','capacity','price_per_night')
    list_display_links = ('hotel','number','capacity','price_per_night')
    