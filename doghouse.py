class doghouse:
    registered_date = None
    name = None
    price = None
    allow_dangerous_dogs = None
    has_toys = None
    is_carpeted = None
    square_meters = None

    booking_list = []

    meta = {
        'db_alias' : 'core',
        "collection" : 'doghouses',
    }