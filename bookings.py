import mongoengine
class Booking(mongoengine.EmbeddedDocument):
    guest_owner_id = mongoengine.ObjectIdField()
    guest_dog_id = mongoengine.ObjectIdField()
    booked_date = mongoengine.DateTimeField()
    check_in_date = mongoengine.DateTimeField(required = True)
    check_out_date = mongoengine.DateTimeField(required = True)
    review = mongoengine.StringField()
    rating = mongoengine.IntField()