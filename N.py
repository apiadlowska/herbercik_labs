python
def tekst_na_binarny(tekst):
    binarny = []
    for znak in tekst:
        ascii_kod = ord(znak)             # Zamień znak na kod ASCII
        binarna_wersja = format(ascii_kod, '08b')  # Zamień kod ASCII na binarny (8 bitów)
        binarny.append(binarna_wersja)
    return ' '.join(binarny)

def main():
    print("Podaj słowo do zakodowania w systemie binarnym (ASCII):")
    slowo = input("➤ ")

    if not slowo:
        print("Nie podano żadnego słowa. Spróbuj ponownie.")
        return

    print("\nZamieniam słowo na kod binarny...")
    wynik = tekst_na_binarny(slowo)

    print("\nWynik w kodzie binarnym (8-bit ASCII):")
    print(wynik)

if _name_ == "_main_":
    main()
