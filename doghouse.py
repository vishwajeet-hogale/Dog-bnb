import mongoengine
import datetime
from bookings import Booking
class doghouse:
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required = True) 
    price = mongoengine.FloatField(required = True)
    allow_dangerous_dogs = mongoengine.BooleanField(required = True)
    has_toys = mongoengine.BooleanField(required = True)
    is_carpeted = mongoengine.BooleanField(required = True)
    square_meters = mongoengine.FloatField(required = True)

    booking_list = mongoengine.EmbeddedDocumentListField(Booking)

    meta = {
        'db_alias' : 'core',
        "collection" : 'doghouses',
    }