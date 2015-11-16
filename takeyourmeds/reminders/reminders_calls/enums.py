import enum

class StateEnum(enum.IntEnum):
    dialing     = 10
    answered    = 20
    busy        = 30
    no_answer   = 40
    failed      = 50
    unknown     = 60
