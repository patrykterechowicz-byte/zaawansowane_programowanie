def prepare(name: str, surname: str) -> str:
    return f"Czesc {name} {surname}"


if __name__ == "__main__":
    greeting = prepare("Patryk", "Terechowicz")
    print(greeting)
