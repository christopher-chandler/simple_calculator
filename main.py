# Standard
import argparse


def addieren(x, y):
    return x + y


def subtrahieren(x, y):
    return x - y


def multiplizieren(x, y):
    return x * y


def dividieren(x, y):
    if y == 0:
        raise ValueError("Division durch Null ist nicht möglich")
    return x / y


def main():
    # Erstelle den Parser
    parser = argparse.ArgumentParser(
        description="Grundlegende arithmetische Operationen durchführen"
    )

    # Füge die Argumente hinzu
    parser.add_argument("zahl1", type=float, help="Die erste Zahl")
    parser.add_argument("zahl2", type=float, help="Die zweite Zahl")
    parser.add_argument(
        "operation",
        type=str,
        choices=["addieren", "subtrahieren", "multiplizieren", "dividieren"],
        help="Die durchzuführende Operation: addieren, subtrahieren, multiplizieren oder dividieren",
    )

    # Analysiere die Argumente
    args = parser.parse_args()

    # Führe die Operation durch
    if args.operation == "addieren":
        ergebnis = addieren(args.zahl1, args.zahl2)
    elif args.operation == "subtrahieren":
        ergebnis = subtrahieren(args.zahl1, args.zahl2)
    elif args.operation == "multiplizieren":
        ergebnis = multiplizieren(args.zahl1, args.zahl2)
    elif args.operation == "dividieren":
        ergebnis = dividieren(args.zahl1, args.zahl2)

    # Drucke das Ergebnis
    print(
        f"Das Ergebnis der Operation {args.operation} von {args.zahl1} und {args.zahl2} ist {ergebnis}"
    )


if __name__ == "__main__":
    main()
