import enum

class TypeEnum(enum.IntEnum):
    call    = 10
    message = 20

class SourceEnum(enum.IntEnum):
    cron        = 10
    manual      = 20
