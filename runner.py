from dataclasses import dataclass
from school import School
from student import Student

@dataclass
class SchoolMenu:
    school: School

    _menu_options = [
        "List All Students",
        "View Individual Student <student_id>",
        "Add a Student",
        "Remove a Student <student_id>",
        "Quit",
    ]

    def __post_init__(self):
        self.display_menu()

    def display_menu(self):
        while True:
            clear_screen()

            print(self.school.name)
            print("-" * len(self.school.name))
            print("Welcome, Richard. Your access level is Principal")
            print("\tWhat would you like to do?")
            print("\tOptions")
            for i, option in enumerate(self._menu_options, 1):
                print(f"\t{i} {option}")

            match get_answer("\n--> ", int, lambda answer: 1 <= answer <= 5):
                case 1:
                    for student in self.school.students:
                        print(student)
                case 2:
                    print("This option has not been implemented yet!")
                case 3:
                    self.school.students.append(
                        Student(
                            name=get_answer("What is the student's name? -> "),
                            age=get_answer("What is the student's age? -> "),
                            password=get_answer("What is the student's password? -> "),
                            role=get_answer("What is the student's role ? -> "),
                            school_id=get_answer("What is the student's school_id ? -> "),
                        )
                    )
                case 4:
                    print("This option has not been implemented yet!")
                case 5:
                    print("Goodbye!")
                    return
                case _:
                    print("You messed up!")

            input("\nPress enter to continue...")


def main():
    SchoolMenu(School('Ridgemont High'))

if __name__ == "__main__":
    main()