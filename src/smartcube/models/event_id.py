class EventId:
    CHANGE = 0
    SHAKING = 1
    SIDE_1 = 2
    SIDE_2 = 3
    SIDE_3 = 4
    SIDE_4 = 5
    SIDE_5 = 6
    SIDE_6 = 7

    @classmethod
    def get(cls, key: str):
        return key.upper().replace("-", "_")

    @classmethod
    def isEvent(cls, key: str):
        return hasattr(cls, cls.get(key))
