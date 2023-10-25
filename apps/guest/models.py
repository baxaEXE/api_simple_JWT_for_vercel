from django.db.models import *


class Guest(Model):
    first_name = CharField(max_length=256)
    last_name = CharField(max_length=128)
    email = CharField(max_length=128)
    phone_number = IntegerField()

    def __str__(self):
        return f'{self.first_name}'
    


