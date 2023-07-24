from src.calculadora_bases import conversao_bases


def main():
    calculator = conversao_bases()
    try:
        calculator.get_values()
        calculator.to_base_x()
    except:
        raise ValueError ("erro")


if __name__ == "__main__":
    main()