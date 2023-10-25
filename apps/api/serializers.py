from rest_framework.serializers import *
from apps.booking.models import Booking
from apps.hotel.models import Hotel
from apps.guest.models import Guest
from apps.room.models import Room


class HotelSerializer(ModelSerializer):
    
    class Meta:
        model = Hotel
        fields = '__all__'



class RoomSerializer(ModelSerializer):
    
    class Meta:
        model = Room
        fields = '__all__'


class GuestSerializer(ModelSerializer):
    
    class Meta:
        model = Guest
        fields = '__all__'


class BookingSerializer(ModelSerializer):
    
    class Meta:
        model = Booking
        fields = '__all__'
    