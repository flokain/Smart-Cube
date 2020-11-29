import btree
import ujson as json


class Database:
    """
       this is a wrapper around btree
       it save object arcording to the specification of the openApi
       with a key equal to the path of the resource in the rest api
    """

    def __init__(self):
        pass

    def connect(self):
        try:
            self.file = open("smartcubedb", "r+b")
        except OSError:
            self.file = open("smartcubedb", "w+b")
        self.db = btree.open(self.file)

    def disconnect(self):
        self.db.close()
        self.file.close()

    def get_by_id(self, key, database="smartcubedb"):

        self.connect()
        value = self.db[key.encode()].decode()
        self.disconnect()
        return self.from_dict(json.loads(value))

    @classmethod
    def dump(cls, database="smartcubedb"):
        try:
            file = open(database, "r+b")
        except OSError:
            file = open(database, "w+b")
        db = btree.open(file)

        with open("/data/dump.json", "rw") as dump:
            dump.truncate(0)
            dump.write("{")
            for key, value in db:
                dump.write(key.decode())
                dump.write(":")
                dump.write(value.decode())
                dump.write(",")
            dump.write("}")

        db.close()
        file.close()
