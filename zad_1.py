class Student:
    def __init__(self, name: str, marks: list[int]):
        self.name: str = name
        self.marks: list[int] = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50


if __name__ == "__main__":
    patryk = Student("patryk", [1, 1, 1, 198])
    patryk2 = Student("patryk", [1, 1, 1, 197])

    print(patryk.is_passed())
    print(patryk2.is_passed())
