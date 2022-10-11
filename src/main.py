import random
import string
from datetime import datetime
from enum import Enum, auto


def gerador_placa() -> str:

    letra1_3 = "".join(random.choices(string.ascii_uppercase, k=3))
    digito4 = "".join(random.choices(string.digits, k=1))
    letter5 = "".join(random.choices(string.ascii_uppercase, k=1))
    digit6_7 = "".join(random.choices(string.digits, k=2))

    return f"{letra1_3}{digito4}{letter5}{digit6_7}"


class Acessorio(Enum):
    AC = auto()
    VE = auto()
    DH = auto()
    P4 = auto()


class Combustivel(Enum):
    GASOLINA = auto()
    DIESEL = auto()
    ALCOOL = auto()
    ELETRICO = auto()


class Veiculo:
    def __init__(
        self,
        marca: str,
        modelo: str,
        cor: str,
        placa: str,
        acessorios: list[Acessorio],
        tipo_comb: Combustivel,
    ) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.acessorios = acessorios
        self.tipo_comb = tipo_comb

    def gerar_reserva(self, date: datetime) -> None:
        print(f"Veiculo reservado para {date}")


def main() -> None:

    golf = Veiculo(
        marca="Wolksvagem",
        modelo="Golf 210",
        cor="Azul",
        placa=gerador_placa(),
        acessorios=[Acessorio.AC, Acessorio.VE],
        tipo_comb=Combustivel.GASOLINA,
    )

    ferrari = Veiculo(
        marca="ferrari",
        modelo="812",
        cor="Vermelho",
        placa=gerador_placa(),
        acessorios=[Acessorio.AC, Acessorio.VE],
        tipo_comb=Combustivel.GASOLINA,
    )

    print(golf.marca)
    print(golf.modelo)
    print(golf.cor)
    print(golf.cor)

    golf.reserve(datetime(2022, 5, 1))


if __name__ == "__main__":
    main()
