from csv import DictReader
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: str
    password: str
    role: str
    school_id: str

    @staticmethod
    def all_students():  # -> list[Student]
        with open("data/students.csv") as f:
            return [Student(**row) for row in DictReader(f)]