
from pymongo.mongo_client import MongoClient

class DataBaseAccess():

    def __init__(self):
        self.__uri = "mongodb+srv://kds:WN0vteFwla4JRww3@cluster0.zomuhsm.mongodb.net/?retryWrites=true&w=majority"

    def startConnection(self):
        
        from pymongo.server_api import ServerApi
        from pymongo.errors import OperationFailure 

        try:
            client = MongoClient(self.__uri, server_api=ServerApi('1'))
            client['bem_estar_maringa'].command('ping')
        except OperationFailure:
            return 500
        else:
            return client

"""
conn = DataBaseAccess().startConnection()

db = conn['bem_estar_maringa']
coll = db['users']

for element in coll.find():
    print(element)
"""