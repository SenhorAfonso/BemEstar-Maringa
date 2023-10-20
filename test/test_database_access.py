
from general_utils import DataBaseAccess, MongoClient

class Test_DatabaseAccess:

    access = DataBaseAccess()

    def test_databaseObject(self):

        assert isinstance(self.access, DataBaseAccess)

    def test_mongoObject(self):
        client = self.access.startConnection()

        assert isinstance(client, MongoClient)