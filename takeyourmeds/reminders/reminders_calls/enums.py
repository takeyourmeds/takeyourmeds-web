import enum

class StateEnum(enum.IntEnum):
    failed          =  0
    dialing         = 10
    answered        = 20
    busy            = 30
    no_answer       = 40
    unknown         = 50
