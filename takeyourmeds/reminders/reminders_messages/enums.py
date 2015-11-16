import enum

class StateEnum(enum.IntEnum):
    in_progress = 10
    sent        = 20
    delivered   = 30
    failed      = 40
