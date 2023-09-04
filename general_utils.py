
class DataBaseAccess():

    def __init__(self):
        self.__uri = "mongodb+srv://kds:WN0vteFwla4JRww3@cluster0.zomuhsm.mongodb.net/?retryWrites=true&w=majority"

    def startConnnection(self):
        from pymongo.mongo_client import MongoClient
        from pymongo.server_api import ServerApi

        client = MongoClient(self.__uri, server_api=ServerApi('1'))

        return client
