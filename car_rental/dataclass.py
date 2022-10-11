import random
import string
from dataclasses import dataclass, field
from datetime import date
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


class FuelType(Enum):
    GASOLINE = auto()
    ALCOHOL = auto()
    FLEX = auto()
    DIESEL = auto()
    ELECTRICAL = auto()


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    type_fuel: FuelType
    rented: bool = False
    reserved = date.today()
    accessories: list[Accessory] = field(default_factory=list)
    plate: str = field(
        default_factory=mercosul_plate_generator,
        init=False,
    )

    def __post_init__(self):
        if self.brand == "Ferrari":
            self.type_fuel = FuelType.ELECTRICAL

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
        accessories=[Accessory.AC, Accessory.VE],
        type_fuel=FuelType.FLEX,
    )

    ferrari = Vehicle(
        brand="Ferrari",
        model="812",
        color="Vermelho",
        type_fuel=FuelType.GASOLINE,
    )

    print(golf.brand)
    print(golf.model)
    print(golf.color)

    golf.generate_reserve(date.today())


if __name__ == "__main__":
    main()
