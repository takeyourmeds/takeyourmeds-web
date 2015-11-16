import enum

class StateEnum(enum.IntEnum):
    in_progress = 10
    answered    = 20
    no_answer   = 30
    failed      = 40
