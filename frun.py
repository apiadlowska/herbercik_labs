import math

# 1. Wyświetl liczby od 1 do 10.
print("1. Liczby od 1 do 10:")
print(*range(1, 11))

# 2. Oblicz sumę liczb od 1 do 100.
suma_100 = sum(range(1, 101))
print(f"\n2. Suma liczb od 1 do 100: {suma_100}")

# 3. Wyświetl wszystkie parzyste liczby od 1 do 50.
print("\n3. Parzyste liczby od 1 do 50:")
print(*range(2, 51, 2))

# 4. Oblicz iloczyn liczb od 1 do 5.
iloczyn_5 = math.prod(range(1, 6))
print(f"\n4. Iloczyn liczb od 1 do 5 (5!): {iloczyn_5}")

# 5. Wyświetl odwróconą wersję napisu "Hello World!".
odwrocony = "Hello World!"[::-1]
print(f"\n5. Odwrócony napis 'Hello World!': {odwrocony}")

# 6. Wyświetl wszystkie litery z podanego słowa.
print("\n6. Litery słowa 'Python':")
print(*(list("Python")), sep='\n')

# 7. Oblicz sumę elementów listy liczb.
LISTA_LICZB = [1, 2, 3, 4, 5]
suma_listy = sum(LISTA_LICZB)
print(f"\n7. Suma elementów listy {LISTA_LICZB}: {suma_listy}")

# 8. Wyświetl wszystkie liczby od 20 do 30, które są podzielne przez 3.
podzielne_przez_3 = [i for i in range(20, 31) if i % 3 == 0]
print(f"\n8. Liczby [20-30] podzielne przez 3: {podzielne_przez_3}")


# 9. Znajdź największą liczbę w liście.
najwieksza = max(LISTA_LICZB)
print(f"\n9. Największa liczba w liście: {najwieksza}")


# 10. Wyświetl wszystkie liczby od 1 do 100, które są podzielne jednocześnie przez 3 i 5.
podzielne_przez_15 = [i for i in range(1, 101) if i % 15 == 0]
print(f"\n10. Liczby [1-100] podzielne przez 3 i 5: {podzielne_przez_15}")

# 11. Oblicz średnią arytmetyczną z listy liczb.
srednia = sum(LISTA_LICZB) / len(LISTA_LICZB)
print(f"\n11. Średnia arytmetyczna listy: {srednia:.2f}")


# 12. Wyświetl wszystkie litery z podanego zdania, pomijając spacje.
zdanie = "To jest testowe zdanie"
litery_bez_spacji = "".join(znak for znak in zdanie if znak != ' ')
print(f"\n12. Litery ze zdania (bez spacji): {litery_bez_spacji}")


# 13. Oblicz silnię liczby podanej przez użytkownika.
print("\n13. Obliczanie silni:")
try:
    n = int(input("Podaj liczbę całkowitą nieujemną (np. 7): "))
    
    if n < 0:
        print("⚠️ Silnia jest zdefiniowana tylko dla liczb nieujemnych.")
    else:
        # math.factorial jest najczystszą implementacją
        silnia = math.factorial(n)
        print(f"Silnia z {n} ({n}!): {silnia}")
        
except ValueError:
    print("⚠️ Błąd wejścia: Wprowadzono nieprawidłową liczbę całkowitą.")
    
    
    # 14. Wyświetl tabliczkę mnożenia (od 1 do 20).
def wyswietl_tabliczke_mnozenia(n: int = 20):
    """Wyświetla tabliczkę mnożenia n x n z wyrównaniem kolumn."""
    print(f"\n14. Tabliczka mnożenia {n}x{n}:")
    
    # Nagłówek (numery kolumn)
    print("   " + "".join(f"{i:4}" for i in range(1, n + 1)))
    print(" " + "-" * (4 * n + 3))
    
    for i in range(1, n + 1):
        # Wiersz z wynikiem i*j
        wiersz = "".join(f"{i * j:4}" for j in range(1, n + 1))
        # Numer wiersza
        print(f"{i:2}| {wiersz}")

wyswietl_tabliczke_mnozenia(20)



# 15. Sprawdź, czy podane słowo jest palindromem.
def jest_palindromem(slowo: str) -> bool:
    """Sprawdza, czy słowo jest palindromem, ignorując wielkość liter."""
    slowo = slowo.lower().replace(" ", "") # Usuń spacje i małe litery dla lepszej weryfikacji
    return slowo == slowo[::-1]

slowo_sprawdzane = "Kobyła ma mały bok" 
czy_pal = jest_palindromem(slowo_sprawdzane)

print(f"\n15. Czy słowo '{slowo_sprawdzane}' jest palindromem? {'Tak' if czy_pal else 'Nie'}")


# 16. Zamień wszystkie litery w podanym napisie na wielkie litery.
napis = "małe i DuŻe litery"
napis_wielkie = napis.upper()
print(f"\n16. Napis wielkimi literami: {napis_wielkie}")


# 17. Wyświetl liczby od 1 do 10 w odwrotnej kolejności.
print("\n17. Liczby od 1 do 10 w odwrotnej kolejności:")
print(*range(10, 0, -1))
