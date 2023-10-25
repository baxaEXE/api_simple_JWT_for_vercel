from django.contrib.admin import *
from .models import Booking

@register(Booking)

class BookingAdmin(ModelAdmin):
    list_display = ('room','guest','check_in_date','check_out_date','is_paid')
    list_display_links = ('room','guest','check_in_date','check_out_date','is_paid')
