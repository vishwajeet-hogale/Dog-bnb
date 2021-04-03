import mongoengine

def global_init():
    # mongoengine.register_connection(alias='core',name = "Dog_bnb")  
    mongoengine.connect(host = "mongodb+srv://vishwajeet:Mjklop@cluster0.pkcgw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",alias='core',name = "Dog_bnb")
    