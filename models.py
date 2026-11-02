from datetime import date


class Student:
    def __init__(
        self,
        name: str,
        marks: list[float],
    ) -> None:
        self.name: str = name
        self.marks: list[float] = marks

    def is_passed(self) -> bool:
        return sum(self.marks) / len(self.marks) > 50

    def __str__(self) -> str:
        return f"Student {self.name} (oceny: {self.marks})"


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
