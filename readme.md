# Dog bnb is a web app that enables users to find a house for their pet when they go out on a vacation

## The following was used to help make this app : 
 * Flask - Python Framework
 * Mongo DB - MongoEngine

## Functionalities involved to make this are as follows : 
1) Register the connection : 
    - Added connection using mongoengine which is a ODM (Just liek ORM)
    - Added meta attribute to owner,dog and doghouse classes.
    Basically used to add the collections to our database
    - Using mongoengine to supply attributes to all the classes which are collections in mongodb
2) Creating users 
    - Registration of users (Signup) 
3) Login functionality 
    - Using flask session
4) Registration of doghouses 
    - Every owner of a doghouse can be a host and guest of a dog
5) Making dog houses available on the market so that bookings can be made
    - Every doghouse has a certain amount of period during which it can be rented out to other interested customers
    - Every owner can be a user and host of the service provided on this platform
    - So any owner can register a doghouse and open it up for bookings
6) Booking a doghouse as a guest 
    - All the doghouses that are available is showed to a user 
    - A booking can be made accordingly according to the user's preference \
7) Adding your dog onto the platform
    - Every user can add his/her dog onto the platform 
    - Can view all the dogs on the platform as well
8) Booking a doghouse as a guest 
    - Work in progress
## Steps to run this after clonning the repo 
* pip install -r requirements.txt
* python app.py 
