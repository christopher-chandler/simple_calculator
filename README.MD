Natürlich, hier ist ein einfaches README für das Programm:

---

# Einfacher Taschenrechner

Dies ist ein einfaches Python-Programm, das grundlegende arithmetische Operationen durchführt. Es verwendet die `argparse`-Bibliothek, um die Eingabe von der Befehlszeile zu verarbeiten.

## Voraussetzungen

- Python 3.x

## Verwendung

1. Öffnen Sie ein Terminal oder eine Eingabeaufforderung.
2. Navigieren Sie zum Verzeichnis, in dem sich die Datei `rechner.py` befindet.
3. Geben Sie den Befehl ein, gefolgt von zwei Zahlen und der gewünschten Operation:

   ```
   python rechner.py zahl1 zahl2 operation
   ```

   Dabei stehen `zahl1` und `zahl2` für die beiden Zahlen, zwischen denen die Operation durchgeführt werden soll, und `operation` für die gewünschte Operation. Mögliche Operationen sind:

   - `addieren`: Addition der beiden Zahlen.
   - `subtrahieren`: Subtraktion der zweiten Zahl von der ersten.
   - `multiplizieren`: Multiplikation der beiden Zahlen.
   - `dividieren`: Division der ersten Zahl durch die zweite.

## Beispiel

- Um 3 und 5 zu addieren:

  ```
  python rechner.py 3 5 addieren
  ```

  Erwartete Ausgabe: `Das Ergebnis der Operation addieren von 3.0 und 5.0 ist 8.0`

- Um 10 und 4 zu subtrahieren:

  ```
  python rechner.py 10 4 subtrahieren
  ```

  Erwartete Ausgabe: `Das Ergebnis der Operation subtrahieren von 10.0 und 4.0 ist 6.0`

- Um 6 und 7 zu multiplizieren:

  ```
  python rechner.py 6 7 multiplizieren
  ```

  Erwartete Ausgabe: `Das Ergebnis der Operation multiplizieren von 6.0 und 7.0 ist 42.0`

- Um 20 durch 4 zu dividieren:

  ```
  python rechner.py 20 4 dividieren
  ```

  Erwartete Ausgabe: `Das Ergebnis der Operation dividieren von 20.0 und 4.0 ist 5.0`
 