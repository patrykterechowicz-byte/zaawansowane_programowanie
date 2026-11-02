from datetime import date

from models import Student, Library, Employee, Order, Book


if __name__ == "__main__":
    library_1 = Library(
        "Wroclaw",
        "Ulica 1",
        "00-001",
        "8-16",
        "123",
    )
    library_2 = Library(
        "Krakow",
        "Ulica 2",
        "00-002",
        "8-16",
        "456",
    )

    book_1 = Book(
        library_1,
        date(2026, 1, 1),
        "Walter",
        "Rudin",
        342,
    )
    book_2 = Book(
        library_1,
        date(2026, 5, 2),
        "Grigorij",
        "Fihtenholtz",
        312,
    )
    book_3 = Book(
        library_2,
        date(2027, 2, 3),
        "Franciszek",
        "Leja",
        350,
    )
    book_4 = Book(
        library_2,
        date(2026, 4, 3),
        "Wacław",
        "Sierpiński",
        402,
    )
    book_5 = Book(
        library_1,
        date(2026, 2, 5),
        "Michael",
        "Spivak",
        680,
    )

    employee_1 = Employee(
        "Jan",
        "Kowalski",
        date(2026, 1, 1),
        date(2026, 1, 1),
        "Wroclaw",
        "Ulica 3",
        "00-003",
        "111",
    )
    employee_2 = Employee(
        "Adam",
        "Nowak",
        date(2026, 1, 1),
        date(2026, 1, 1),
        "Krakow",
        "Ulica 4",
        "00-004",
        "222",
    )
    employee_3 = Employee(
        "Ewa",
        "Kowalska",
        date(2026, 1, 1),
        date(2026, 1, 1),
        "Wroclaw",
        "Ulica 5",
        "00-005",
        "333",
    )

    student_1 = Student("Student1", [70, 85, 90])
    student_2 = Student("Student2", [30, 45, 50])
    student_3 = Student("Student3", [60, 55, 65])

    order_1 = Order(
        employee_1,
        student_1,
        [book_1, book_2, book_5],
        date(2026, 1, 1),
    )
    order_2 = Order(
        employee_2,
        student_3,
        [book_3, book_4],
        date(2026, 1, 1),
    )

    print(order_1)
    print()
    print(order_2)
