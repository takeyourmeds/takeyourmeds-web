import enum

class StateEnum(enum.IntEnum):
    failed      =  0
    sending     = 10
    sent        = 20
    delivered   = 30
    unknown     = 40
