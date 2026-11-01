class Student:
    def __init__(self, name: str, marks: list[float]) -> None:
        self.name: str = name
        self.marks: list[float] = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50

    def __str__(self) -> str:
        return f'Student {self.name} (oceny: {self.marks})'


if __name__ == '__main__':
    good_student = Student('Patryk', [70, 85, 90])
    bad_student = Student('NiePatryk', [30, 45, 50])

    print(good_student, '->', good_student.is_passed())
    print(bad_student, '->', bad_student.is_passed())
