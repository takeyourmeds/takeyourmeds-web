import enum

class StateEnum(enum.IntEnum):
    sending     = 10
    sent        = 20
    failed      = 30
    unknown     = 40
