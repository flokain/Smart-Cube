from smartcube.models.base_model_ import Model
import btree
import ujson as json


def JSONEncodeModel(o):

    if isinstance(o, Model):
        dikt = {}
        for attr, _ in o.swagger_types.items():
            value = getattr(o, attr)
            if value is None:
                continue
            attr = o.attribute_map[attr]
            dikt[attr] = value
        return dikt
    else:
        raise TypeError("object is not based on smartcube Model")


def save(self, key: str):
    try:
        file = open(self.database, "r+b")
    except OSError:
        file = open(self.database, "w+b")

    db = btree.open(file)
    db[key.encode()] = json.dumps(JSONEncodeModel(self)).encode()
    db.flush()
    db.close()
    file.close()


setattr(Model, 'save', save)
