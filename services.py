from owners import Owner
from doghouse import doghouse
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


