import enum

class StateEnum(enum.IntEnum):
    failed          = 20
    sending         = 30
    sent            = 40
    delivered       = 50
    unknown         = 60
