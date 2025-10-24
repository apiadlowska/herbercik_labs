from random import randint

# # 1. Generuj listę 10 liczb losowych z przedziału 1 do 100.
# def generuj_losowe(n: int, min_val: int, max_val: int) -> list[int]:
#     """Generuje listę n losowych liczb całkowitych z podanego przedziału [min_val, max_val]."""
#     return [randint(min_val, max_val) for _ in range(n)]

# lista_10_liczb = generuj_losowe(10, 1, 100)
# print("1. Lista 10 liczb [1-100]:")
# print(lista_10_liczb)



# # 2. Generuj listę 20 liczb losowych z przedziału 100 do 200. Parzystych niepodzielnych przez 5.
# def generuj_specjalne_liczby(n: int, min_val: int, max_val: int) -> list[int]:
#     """Generuje n unikalnych losowych liczb parzystych niepodzielnych przez 5 z danego zakresu."""
#     specjalne_liczby = []
    
#     # Najpierw generujemy wszystkie możliwe liczby spełniające warunki
#     # Zakres jest stosunkowo mały, więc to jest wydajne.
#     wszystkie_spelnione = [
#         i for i in range(min_val, max_val + 1) 
#         if i % 2 == 0 and i % 5 != 0
#     ]
    
#     # Sprawdzamy, czy w ogóle jest wystarczająca liczba elementów
#     if len(wszystkie_spelnione) < n:
#         raise ValueError(f"W zakresie [{min_val}, {max_val}] jest tylko {len(wszystkie_spelnione)} liczb spełniających warunki. Żądano {n}.")

#     # Używamy random.sample, aby wybrać n elementów bez powtórzeń (bardziej efektywne niż losowanie w pętli while)
#     from random import sample
#     return sample(wszystkie_spelnione, n)

# try:
#     lista_specjalna = generuj_specjalne_liczby(20, 100, 200)
#     print("\n2. Lista 20 liczb parzystych [100-200] i niepodzielnych przez 5:")
#     print(lista_specjalna)
# except ValueError as e:
#     print(f"\n Błąd: {e}")
    


# # 3. Napisz program do którego możemy wprowadzić dowolne zdanie. Niech nasz program wyświetli: Ile mamy d,v,b,n,k.
# def zlicz_litery(zdanie: str, litery_do_zliczenia: str = 'dvbnk') -> dict[str, int]:
#     """Zlicza wystąpienia określonych liter w zdaniu, ignorując wielkość liter."""
#     zdanie_male = zdanie.lower()
#     wynik = {litera: 0 for litera in litery_do_zliczenia}
    
#     # Zliczanie przy użyciu pętli for (konieczne w tym przypadku)
#     for litera in zdanie_male:
#         if litera in wynik:
#             wynik[litera] += 1
            
#     return wynik

# zdanie_uzytkownika = input("\n3. Wprowadź dowolne zdanie: ")
# zliczenia = zlicz_litery(zdanie_uzytkownika)

# print("Zliczenie liter (d, v, b, n, k):")
# for litera, ilosc in zliczenia.items():
#     print(f"  Litera '{litera}': {ilosc}")


from random import randint
# Lista bazowa dla zadań 5-11
LISTA_BAZOWA = [randint(-50, 50) for _ in range(100)]
print("\n4. Lista bazowa (100 liczb od -50 do 50):")
print(LISTA_BAZOWA)

# 5. Napisz program który z przyjmuje jako argument powyższą listę i zwróci mi ile jest liczb mniejszych od 0.
def zlicz_ujemne(lista: list[int]) -> int:
    """Zlicza elementy w liście mniejsze od zera."""
    # sum(1 for ...) to optymalny sposób na zliczanie spełnionych warunków
    return sum(1 for liczba in lista if liczba < 0)

ilosc_ujemnych = zlicz_ujemne(LISTA_BAZOWA)
print(f"\n5. Liczba elementów mniejszych od 0: {ilosc_ujemnych}")


# 6. Napisz program który z przyjmuje jako argument powyższą listę i zwrócić mi ile jest większych lub równych 0.
def zlicz_nieujemne(lista: list[int]) -> int:
    """Zlicza elementy w liście większe lub równe zeru."""
    return sum(1 for liczba in lista if liczba >= 0)

ilosc_nieujemnych = zlicz_nieujemne(LISTA_BAZOWA)
print(f"6. Liczba elementów większych lub równych 0: {ilosc_nieujemnych}")


# 7. Napisz program który z przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów parzystych.
def suma_parzystych(lista: list[int]) -> int:
    """Zwraca sumę wszystkich parzystych elementów w liście."""
    # Użycie generatora w sum() jest wydajniejsze niż tworzenie pośredniej listy
    return sum(liczba for liczba in lista if liczba % 2 == 0)

suma_p = suma_parzystych(LISTA_BAZOWA)
print(f"7. Suma elementów parzystych: {suma_p}")


# 8. Napisz program która z przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów nieparzystych.
def suma_nieparzystych(lista: list[int]) -> int:
    """Zwraca sumę wszystkich nieparzystych elementów w liście."""
    return sum(liczba for liczba in lista if liczba % 2 != 0)

suma_np = suma_nieparzystych(LISTA_BAZOWA)
print(f"8. Suma elementów nieparzystych: {suma_np}")

# 9. Napisz program który przyjmuje jako argument powyższą listę i zwrócić mi sumę wszystkich elementów podzielnych przez 5 i 7.
def suma_podzielnych_przez_35(lista: list[int]) -> int:
    """Zwraca sumę elementów podzielnych jednocześnie przez 5 i 7 (czyli przez 35)."""
    return sum(liczba for liczba in lista if liczba % 35 == 0)

suma_35 = suma_podzielnych_przez_35(LISTA_BAZOWA)
print(f"9. Suma elementów podzielnych przez 5 i 7 (czyli 35): {suma_35}")

# 10. Napisz program która z przyjmuje jako argument powyższą listę poprosi o podanie liczby 
# przez użytkownika i powie ile takich liczb występuje na tej liście.
def zlicz_wystapienia(lista: list[int], szukana: int) -> int:
    """Zlicza wystąpienia danej liczby w liście."""
    return lista.count(szukana)

try:
    szukana_przez_uzytkownika = int(input("\n10. Podaj liczbę, której wystąpienia chcesz policzyć w liście: "))
    ilosc_wyst = zlicz_wystapienia(LISTA_BAZOWA, szukana_przez_uzytkownika)
    print(f"Liczba {szukana_przez_uzytkownika} występuje {ilosc_wyst} razy w liście.")
except ValueError:
    print("⚠️ Błąd wejścia: Wprowadź liczbę całkowitą.")
    
    
    # 11. Zwrócić lisy w których będę zawrte idexy pod którymi występują największe wartości i najmniejsze wartości.
def znajdz_indeksy_ekstremow(lista: list[int]) -> tuple[list[int], list[int]]:
    """
    Znajduje wszystkie indeksy, pod którymi występują największe i najmniejsze wartości w liście.
    Zwraca krotkę (indeksy_min, indeksy_max).
    """
    if not lista:
        return [], []
        
    najmniejsza = min(lista)
    najwieksza = max(lista)
    
    indeksy_min = []
    indeksy_max = []
    # def znajdz_indeksy_min_max(lista):
    najmniejsza = min(lista)
    najwieksza = max(lista)
    indeksy_min = []
    indeksy_max = []

    # Użycie enumerate w pętli for
    for indeks, wartosc in enumerate(lista):
        if wartosc == najmniejsza:
            indeksy_min.append(indeks)
        if wartosc == najwieksza:
            indeksy_max.append(indeks)
    return indeksy_min, indeksy_max


indeksy_min, indeksy_max = znajdz_indeksy_ekstremow(LISTA_BAZOWA)

print("\n11. Indeksy wartości ekstremalnych:")
print(f"  Najmniejsza wartość ({min(LISTA_BAZOWA) if LISTA_BAZOWA else 'N/A'}) występuje pod indeksami: {indeksy_min}")
print(f"  Największa wartość ({max(LISTA_BAZOWA) if LISTA_BAZOWA else 'N/A'}) występuje pod indeksami: {indeksy_max}")

# 12. Napisz program która wygeneruje listę o n wielkości i “zasięgu” podanego przez użytkownika.
def dynamiczna_lista(wielkosc: int, min_zakres: int, max_zakres: int) -> list[int]:
    """Generuje listę o zadanej wielkości z liczbami z podanego zakresu."""
    if wielkosc <= 0:
        raise ValueError("Wielkość listy musi być dodatnia.")
    if min_zakres > max_zakres:
        min_zakres, max_zakres = max_zakres, min_zakres # Zamiana, jeśli użytkownik poda w złej kolejności
    
    return [randint(min_zakres, max_zakres) for _ in range(wielkosc)]

try:
    wielkosc = int(input("\n12. Podaj wielkość (N) listy do wygenerowania: "))
    min_zakres = int(input("    Podaj dolny zakres losowania (np. 1): "))
    max_zakres = int(input("    Podaj górny zakres losowania (np. 100): "))
    
    nowa_lista = dynamiczna_lista(wielkosc, min_zakres, max_zakres)
    print(f"Wygenerowana lista (N={wielkosc}, zakres=[{min_zakres}, {max_zakres}]):")
    print(nowa_lista)
except ValueError as e:
    print(f" Błąd wejścia: {e}. Wprowadź poprawne liczby całkowite.")
