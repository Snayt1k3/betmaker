import enum


class EventStatus(enum.Enum):
    UNFINISHED = "unfinished"
    WIN_FIRST_TEAM = "win_first_team"
    WIN_SECOND_TEAM = "win_second_team"
