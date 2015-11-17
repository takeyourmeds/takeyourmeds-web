import enum

class StateEnum(enum.IntEnum):
    twilio_disabled = 10
    failed          = 20
    dialing         = 30
    answered        = 40
    busy            = 50
    no_answer       = 60
    unknown         = 70
