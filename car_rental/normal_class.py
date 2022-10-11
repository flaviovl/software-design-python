import random
import string
from datetime import date, datetime
from enum import Enum, auto


def mercosul_plate_generator() -> str:

    three_letters = "".join(random.choices(string.ascii_uppercase, k=3))
    one_digit = "".join(random.choices(string.digits, k=1))
    one_letter = "".join(random.choices(string.ascii_uppercase, k=1))
    two_digits = "".join(random.choices(string.digits, k=2))

    return f"{three_letters}{one_digit}{one_letter}{two_digits}"


class Accessory(Enum):
    AC = auto()
    VE = auto()
    DH = auto()
    P4 = auto()


class TypeFuel(Enum):
    GASOLINE = auto()
    ALCOHOL = auto()
    FLEX = auto()
    DIESEL = auto()
    ELECTRICAL = auto()


class Vehicle:
    def __init__(
        self,
        brand: str,
        model: str,
        color: str,
        plate: str,
        accessories: list[Accessory],
        type_fuel: TypeFuel,
        rented: bool = False,
    ) -> None:
        self.brand = brand
        self.model = model
        self.color = color
        self.plate = plate
        self.accessories = accessories
        self.type_fuel = type_fuel
        self.reserved = date.today()
        self.rented = rented

    def generate_reserve(self, reserve_date: date) -> None:
        if self.rented:
            print("Veiculo alugado!")
        else:
            print(f"Veiculo reservado para {reserve_date}")
            self.reserved = reserve_date


def main() -> None:

    golf = Vehicle(
        brand="Wolksvagem",
        model="Golf 210",
        color="Azul",
        plate=mercosul_plate_generator(),
        accessories=[Accessory.AC, Accessory.VE],
        type_fuel=TypeFuel.FLEX,
    )

    ferrari = Vehicle(
        brand="Ferrari",
        model="812",
        color="Vermelho",
        plate=mercosul_plate_generator(),
        accessories=[Accessory.AC, Accessory.VE],
        type_fuel=TypeFuel.GASOLINE,
    )

    print(golf.brand)
    print(golf.model)
    print(golf.color)

    golf.generate_reserve(date.today())


if __name__ == "__main__":
    main()
