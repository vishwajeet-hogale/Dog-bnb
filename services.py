from owners import Owner
def create_account(name:str,email:str,password : str) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email
    owner.password = password
    owner.save()

def find_account_by_email(email) -> Owner:
    owner = Owner.objects(email = email).first()
    return owner
def find_account_by_username_password(username,password) -> Owner:
    owner = Owner.objects(name=username,password = password).first()
    print(owner)
    return owner