import enum

class StateEnum(enum.IntEnum):
    in_progress = 0
    success     = 10
    error       = 20

class SourceEnum(enum.IntEnum):
    manual      = 10
    schedule    = 20
