from datetime import date

from zad1 import Student


class Library:
    def __init__(
        self,
        city: str,
        street: str,
        zip_code: str,
        open_hours: str,
        phone: str,
    ) -> None:
        self.city: str = city
        self.street: str = street
        self.zip_code: str = zip_code
        self.open_hours: str = open_hours
        self.phone: str = phone

    def __str__(self) -> str:
        return (
            f"Biblioteka: {self.street}"
            + f", {self.zip_code} {self.city}"
            + f", tel. {self.phone}"
            + f", godziny otwarcia: {self.open_hours}"
        )


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: date,
        birth_date: date,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.hire_date: date = hire_date
        self.birth_date: date = birth_date
        self.city: str = city
        self.street: str = street
        self.zip_code: str = zip_code
        self.phone: str = phone

    def __str__(self) -> str:
        return (
            f"Pracownik {self.first_name} {self.last_name} "
            f"(ur. {self.birth_date}, zatrudniony {self.hire_date}), "
            f"{self.street}, {self.zip_code} {self.city}, tel. {self.phone}"
        )


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: date,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ) -> None:
        self.library: Library = library
        self.publication_date: date = publication_date
        self.author_name: str = author_name
        self.author_surname: str = author_surname
        self.number_of_pages: int = number_of_pages

    def __str__(self) -> str:
        return (
            f"Książka autorstwa {self.author_name} {self.author_surname}, "
            f"wydana {self.publication_date}, "
            f"{self.number_of_pages} stron, {self.library}"
        )


class Order:
    def __init__(
        self,
        employee: Employee,
        student: Student,
        books: list[Book],
        order_date: date,
    ) -> None:
        self.employee: Employee = employee
        self.student: Student = student
        self.books: list[Book] = books
        self.order_date: date = order_date

    def __str__(self) -> str:
        books = "\n".join(f"  - {book}" for book in self.books)
        return (
            f"Zamówienie z dnia {self.order_date}\n"
            f" {self.employee}\n"
            f" {self.student}\n"
            f" Książki:\n{books}"
        )


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
