# Dog bnb is a web app that enables users to find a house for their pet when they go out on a vacation

## The following was used to help make this app : 
    * Flask
    * Mongo DB

## Steps involved to make this are as follows : 
    1) Register the connection : 
        * Added connection using mongoengine which is a ODM (Just liek ORM)
        * Added meta attribute to owner,dog and doghouse classes.
          Basically used to add the collections to our database
        * Using mongoengine to supply attributes to all the classes which are collections in mongodb
    2) Creating users 
        * 