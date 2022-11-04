import pymongo
import certifi

con_str = "mongodb+srv://blake:fsdi110@cluster0.lawusce.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("Ergononics")
me = {
    "first_name": "Blake",
    "last_name": "Spears",
}


def hello():
    print("Hello there!")
