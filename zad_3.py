class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str) -> None:
        self.area: float = area
        self.rooms: int = rooms
        self.price: float = price
        self.address: str = address

    def __str__(self) -> str:
        return f"{self.area} metrów kwadratowych, {self.rooms} pokoje, cena {self.price} zł, adres: {self.address}"


class House(Property):
    def __init__(
        self, area: float, rooms: int, price: float, address: str, plot: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.plot: int = plot

    def __str__(self) -> str:
        return f"Dom: {super().__str__()}, działka {self.plot} metrów kwadratowych"


class Flat(Property):
    def __init__(
        self, area: float, rooms: int, price: float, address: str, floor: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.floor: int = floor

    def __str__(self) -> str:
        return f"Mieszkanie: {super().__str__()}, piętro {self.floor}"


if __name__ == "__main__":
    house = House(150, 5, 950000, "ul. Leśna 4, Wrocław", 800)
    flat = Flat(55, 3, 520000, "ul. Leśna 4, Kraków", 3)

    print(house)
    print(flat)
