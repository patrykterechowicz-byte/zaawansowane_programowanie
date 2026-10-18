def is_even(p: int) -> bool:
    return p % 2 == 0


if __name__ == "__main__":
    n = 3921
    even = is_even(n)

    if even:
        print(f"Liczba {n} jest parzysta")
    else:
        print(f"Liczba {n} jest nieparzysta")
