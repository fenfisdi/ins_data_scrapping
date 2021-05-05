from mongoengine import connect

class MongoEngine:
    def __init__(self, host : str) -> None:
        self.mongo_uri = host

    def get_connection(self):
        return connect(host=self.mongo_uri)
