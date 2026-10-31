from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    otdel: str
    zp: int

    @classmethod
    def load(cls, file_string):
        name, otdel, zp = file_string.split(";")
        return cls(name, otdel, int(zp))

    @staticmethod
    def calculate_bonus(zp, otdel):
        if otdel == "Продажи":
            return zp * 0.10
        else:
            return zp * 0.05