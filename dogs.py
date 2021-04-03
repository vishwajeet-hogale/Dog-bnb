import mongoengine
import datetime
class Dogs(mongoengine.Document):
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    species = mongoengine.StringField(required = True)
    Age = mongoengine.IntField(required = True)
    name = mongoengine.StringField(required = True) 
    is_dangerous = mongoengine.BooleanField(required = True)
    meta = {
        'db_alias' : 'core',
        "collection" : 'dogs',
    }