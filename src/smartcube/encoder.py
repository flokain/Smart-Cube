from smartcube.models.base_model_ import Model

def JSONEncodeModel( o):
    
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
