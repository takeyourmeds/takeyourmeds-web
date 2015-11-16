import enum

class StateEnum(enum.IntEnum):
    sending     = 10
    sent        = 20
    delivered   = 30
    failed      = 40
    unknown     = 50
