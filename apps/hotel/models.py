from django.db.models import * 

class Hotel(Model):
    name = CharField(max_length=128)
    address = CharField(max_length=128)
    city = CharField(max_length=128)
    country = CharField(max_length=128)
    rating = PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'
    