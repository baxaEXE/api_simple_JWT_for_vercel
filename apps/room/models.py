from django.db.models import *
from apps.hotel.models import Hotel

class Room(Model):
    hotel = ForeignKey(Hotel,on_delete=CASCADE)
    number = IntegerField()
    capacity = PositiveIntegerField(blank=True,null=True)
    price_per_night = PositiveIntegerField(blank=True,null=True)
     
    def __str__(self):
        return f'{self.hotel}'
    

