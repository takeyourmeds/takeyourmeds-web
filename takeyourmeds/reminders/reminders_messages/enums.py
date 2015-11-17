import enum

class StateEnum(enum.IntEnum):
    twilio_disabled = 10
    failed          = 20
    sending         = 30
    sent            = 40
    delivered       = 50
    unknown         = 60
