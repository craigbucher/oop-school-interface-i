from csv import DictReader
from dataclasses import dataclass

@dataclass
class Staff:
    name: str
    age: str
    password: str
    role: str
    employee_id: str

    @staticmethod
    def all_staff():  # -> list[Staff]
        with open("data/staff.csv") as f:
            return [Staff(**row) for row in DictReader(f)]