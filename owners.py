class Owner:
    registered_date = None
    name = None 
    email = None 

    dog_ids = []
    doghouse_ids = []
    meta = {
        'db_alias' : 'core',
        "collection" : 'owners',
    }