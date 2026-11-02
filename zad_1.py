from models import Student

if __name__ == "__main__":
    good_student = Student("Patryk", [70, 85, 90])
    bad_student = Student("NiePatryk", [30, 45, 50])

    print(
        good_student,
        "->",
        good_student.is_passed(),
    )
    print(
        bad_student,
        "->",
        bad_student.is_passed(),
    )
