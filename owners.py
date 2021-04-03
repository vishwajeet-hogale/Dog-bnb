import mongoengine 
import datetime
class Owner(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default = datetime.datetime.now)
    name = mongoengine.StringField(required = True)
    email = mongoengine.StringField(required = True)
    password = mongoengine.StringField(required = True)
    dog_ids = mongoengine.ListField()
    doghouse_ids = mongoengine.ListField()
    meta = {
        'db_alias' : 'core',
        "collection" : 'owners',
    }