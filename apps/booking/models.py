from django.db.models import *
from apps.room.models import Room

class Booking(Model):
    room = ForeignKey(Room,on_delete=CASCADE)
    guest = CharField(max_length=128)
    check_in_date = DateField()
    check_out_date = DateField()
    is_paid = BooleanField(default=False)

    def __str__(self):
        return f'{self.guest}'
    



