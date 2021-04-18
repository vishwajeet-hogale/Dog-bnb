from owners import Owner
from doghouse import doghouse
from bookings import Booking
from dogs import Dogs
import datetime
def create_account(name:str,email:str,password : str) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email
    owner.password = password
    owner.save()

def find_account_by_email(email) -> Owner:
    owner = Owner.objects(email = email).first()
    return owner
def find_account_by_username(username) -> Owner:
    owner = Owner.objects(name = username).first()
    return owner
def find_account_by_username_password(username,password) -> Owner:
    owner = Owner.objects(name=username,password = password).first()
    print(owner)
    return owner

def create_doghouse(dit:dict) -> doghouse:
    dh = doghouse()
    dh.email = dit["email"]
    # dh.dogname = dit["dogname"]
    dh.price = float(dit["price"])
    dh.square_meters = float(dit["meters"])
    if dit["has_toys"] == "Yes":
        dh.has_toys = True
    else:
        dh.has_toys = False
    if dit["allow_dangerous_dogs"] == "Yes":
        dh.allow_dangerous_dogs = True
    else:
        dh.allow_dangerous_dogs = False
    if dit["is_carpeted"] == "Yes":
        dh.is_carpeted = True
    else:
        dh.is_carpeted = False
    
    dh.save()
    return dh

def save_doghouse_user(sess,dh)->Owner:
    a = find_account_by_username(sess)
    a.doghouse_ids.append(dh.id)
    a.save()
    return a
def find_doghouses_for_user(owner:Owner) -> list[doghouse]:
    query = doghouse.objects(id__in = owner.doghouse_ids) 
    dhs = list(query)
    return dhs
# def find_doghouses_for_user_session(sesh:str) -> list[doghouse]:
#     query = doghouse.objects(name=)

def find_doghouses_for_user(owner:Owner)->list[doghouse]:
    query = doghouse.objects(id__in = owner.doghouse_ids)
    doghouses = list(query)
    return doghouses

def add_available_date(selected_doghouse:doghouse,start_date:datetime.datetime,days:str)-> doghouse:
    booking = Booking()
    booking.check_in_date = start_date
    booking.check_out_date = start_date + datetime.timedelta(days=int(days))
    doghous = doghouse.objects(id = selected_doghouse.id).first()
    doghous.booking_list.append(booking)
    doghous.save()
    return doghouse

def add_dog(username:str,name:str,age:int,is_dangerous:bool,species:str)->Dogs:
    dog = Dogs()
    dog.name = name
    dog.Age = age
    dog.species = species
    dog.is_dangerous = is_dangerous
    dog.save()
    owner = find_account_by_username(username)
    owner.dog_ids.append(dog.id)
    owner.save()
    return dog

