from dataclasses import dataclass


@dataclass(slots=True)
class NewUser:
    username: str
