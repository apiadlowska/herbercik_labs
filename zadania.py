# Zadania z lekcji - pełna wersja (bez skracania)
# Autor: mychamasterdie-netizen
# Uruchom: python zadania_pełne.py
#
# Ten plik zawiera kompletne, rozbudowane rozwiązania wszystkich zadań które przesłałeś/aś:
# - Zadania wprowadzające (każde w pełnej interaktywnej wersji)
# - Zadania do domu (pełna interaktywna realizacja 10 punktów)
# - Dodatkowe zadanka do trenowania (if/while itp.)
# - Sekcja "While - dalszy trening" z pełnymi rozwiązaniami
# - Przykładowe użycie i testy na końcu (możesz je wyłączyć/usunąć)
#
# Kod jest celowo wyraźnie skomentowany, zawiera walidację wejścia i zachowuje
# oryginalne komunikaty (np. "podałeś złe liczby Nobie!"), które pojawiały się w treści zadań.

import math
import random
import sys
from typing import List, Optional, Tuple, Any

# ----------------------------
# Pomocniczne funkcje wejścia
# ----------------------------

def read_int(prompt: str, allow_empty: bool = False) -> Optional[int]:
    """
    Wczytuje liczbę całkowitą z wejścia.
    Jeśli allow_empty=True i użytkownik wpisze pusty ciąg -> zwraca None.
    W przeciwnym razie pyta ponownie do skutku.
    """
    while True:
        s = input(prompt)
        if allow_empty and s.strip() == "":
            return None
        try:
            return int(s)
        except ValueError:
            print("To nie jest poprawna liczba całkowita. Spróbuj jeszcze raz.")

def read_float(prompt: str, allow_empty: bool = False) -> Optional[float]:
    """
    Wczytuje liczbę zmiennoprzecinkową z wejścia.
    Jeśli allow_empty=True i użytkownik wpisze pusty ciąg -> zwraca None.
    """
    while True:
        s = input(prompt)
        if allow_empty and s.strip() == "":
            return None
        try:
            return float(s)
        except ValueError:
            print("To nie jest poprawna liczba. Spróbuj jeszcze raz.")

def read_int_in_range(prompt: str, low: int, high: int) -> int:
    """Wczytuje liczbę całkowitą w przedziale [low, high]."""
    while True:
        v = read_int(prompt)
        if v is None:
            continue
        if low <= v <= high:
            return v
        print(f"Podaj liczbę w zakresie {low}..{high}.")

# ----------------------------
# Zadania wprowadzające
# ----------------------------

def perhaps_bot():
    """
    Program, który na każde zadane pytanie odpowiada "perhaps".
    Interaktywnie: użytkownik zadaje pytania, pusty wpis kończy.
    """
    print("Bot odpowiada 'perhaps'. Wpisz pusty wiersz aby zakończyć.")
    try:
        while True:
            q = input("Zadaj pytanie: ")
            if q == "":
                print("Koniec działania perhaps_bot.")
                break
            print("perhaps")
    except KeyboardInterrupt:
        print("\nPrzerwano.")

def divisible_by_9_up_to_interactive():
    """
    Interaktywny program: wyświetli wszystkie liczby podzielne przez 9 do wartości podanej przez użytkownika.
    Zakres: od 0 do n (jeśli n >= 0), od n do 0 jeśli n < 0.
    """
    n = read_int("Podaj wartość n (do której szukamy liczb podzielnych przez 9): ")
    if n is None:
        print("Błąd wejścia.")
        return
    if n >= 0:
        rng = range(0, n + 1)
    else:
        rng = range(n, 1)
    result = [i for i in rng if i % 9 == 0]
    print("Liczby podzielne przez 9:", result)

def not_divisible_by_3_up_to_interactive():
    """
    Interaktywny program: wyświetli wszystkie liczby, które NIE są podzielne przez 3 do wartości n.
    """
    n = read_int("Podaj wartość n (do której szukamy liczb niepodzielnych przez 3): ")
    if n is None:
        print("Błąd wejścia.")
        return
    if n >= 0:
        rng = range(0, n + 1)
    else:
        rng = range(n, 1)
    result = [i for i in rng if i % 3 != 0]
    print("Liczby NIEpodzielne przez 3:", result)

def powers_of_two_interactive():
    """
    Interaktywny program: wyświetla n potęg liczby 2 (2^0 ... 2^(n-1)).
    """
    n = read_int("Podaj ile potęg liczby 2 wyświetlić (n): ")
    if n is None or n <= 0:
        print("n musi być liczbą całkowitą większą od 0.")
        return
    res = [2**i for i in range(n)]
    print("Potęgi 2:", res)

def sum_divisible_by_5_up_to_interactive():
    """
    Interaktywny program: zsumuje wszystkie liczby podzielne przez 5 do wartości n.
    """
    n = read_int("Podaj wartość n (do której sumujemy liczby podzielne przez 5): ")
    if n is None:
        print("Błąd wejścia.")
        return
    if n >= 0:
        rng = range(0, n + 1)
    else:
        rng = range(n, 1)
    s = sum(i for i in rng if i % 5 == 0)
    print("Suma liczb podzielnych przez 5 do n:", s)

def love_programming_interactive():
    """
    Interaktywny program: wyświetli 'Kocham programować!' n razy.
    """
    n = read_int("Ile razy wyświetlić 'Kocham programować!'? Podaj n: ")
    if n is None or n <= 0:
        print("n musi być > 0.")
        return
    for _ in range(n):
        print("Kocham programować!")

def is_prime_interactive():
    """
    Interaktywne sprawdzenie czy liczba x jest liczbą pierwszą.
    """
    x = read_int("Podaj liczbę do sprawdzenia (czy jest pierwsza): ")
    if x is None:
        print("Błąd wejścia.")
        return
    if is_prime(x):
        print(f"{x} jest liczbą pierwszą.")
    else:
        print(f"{x} nie jest liczbą pierwszą.")

def is_prime(x: int) -> bool:
    """
    Sprawdza czy x jest liczbą pierwszą.
    Metoda efektywna: test do sqrt(x), pomija liczby <2 i parzyste.
    """
    if not isinstance(x, int):
        try:
            x = int(x)
        except Exception:
            return False
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    r = int(math.isqrt(x))
    i = 3
    while i <= r:
        if x % i == 0:
            return False
        i += 2
    return True

def input_list_x_interactive():
    """
    Stworzy listę zawierającą x liczb wprowadzonych przez użytkownika od (1 do 200).
    """
    x = read_int("Ile liczb chcesz wprowadzić? (x): ")
    if x is None or x <= 0:
        print("Nieprawidłowa liczba elementów.")
        return
    lst = []
    i = 0
    while i < x:
        try:
            val = int(input(f"Podaj liczbę {i+1}/{x} (z zakresu 1..200): "))
            if 1 <= val <= 200:
                lst.append(val)
                i += 1
            else:
                print("Liczba poza zakresem 1..200. Spróbuj ponownie.")
        except ValueError:
            print("To nie jest liczba całkowita.")
    print("Otrzymana lista:", lst)
    return lst

def filter_even_50_70_interactive():
    """
    Na podstawie otrzymanej listy stwórz nową listę gdzie znajdują się:
    Liczby parzyste większe od 50 ale mniejsze od 70.
    Wyświetl je w konsoli z informacją ile zawierają elementów.
    """
    raw = input("Podaj listę liczb oddzielonych spacjami (ENTER = przykład): ")
    if raw.strip() == "":
        lst = [10, 51, 52, 60, 69, 70, 88]
    else:
        try:
            lst = [int(s) for s in raw.split()]
        except ValueError:
            print("Błędne dane. Używam przykładowej listy.")
            lst = [10, 51, 52, 60, 69, 70, 88]
    filtered = [x for x in lst if isinstance(x, int) and x % 2 == 0 and 50 < x < 70]
    print("Znalezione liczby parzyste >50 i <70:", filtered)
    print("Ilość elementów:", len(filtered))
    return filtered

def grades_average_interactive():
    """
    Wprowadza x ocen (1 do 6) a następnie obliczy średnią arytmetyczną.
    Jeśli ktoś wprowadzi liczby inne niż 1 i 6 niech program wyświetli komunikat:
    'podałeś złe liczby Nobie!'
    """
    x = read_int("Ile ocen chcesz wprowadzić? (x): ")
    if x is None or x <= 0:
        print("Nieprawidłowa liczba ocen.")
        return
    grades = []
    for i in range(x):
        try:
            g = int(input(f"Ocena {i+1}/{x} (1..6): "))
        except ValueError:
            print("To nie jest liczba całkowita. Kończę.")
            return
        if g < 1 or g > 6:
            print("podałeś złe liczby Nobie!")
            return
        grades.append(g)
    avg = sum(grades) / len(grades) if grades else 0.0
    print("Oceny:", grades)
    print("Średnia arytmetyczna ocen:", avg)
    return avg

def generate_random_list_interactive():
    """
    Wygeneruj listę losowych liczb o n wielkości z zakresu od 1 do 100.
    """
    n = read_int("Ile losowych liczb wygenerować? (n): ")
    if n is None or n <= 0:
        print("n musi być > 0.")
        return []
    lst = [random.randint(1, 100) for _ in range(n)]
    print("Wygenerowana lista:", lst)
    return lst

def harmonic_mean_interactive():
    """
    Oblicz średnią harmoniczną z podanej listy (interaktywnie).
    """
    raw = input("Podaj listę liczb oddzielonych spacjami (np. '1 2 4') lub ENTER aby użyć przykładowej: ")
    if raw.strip() == "":
        lst = [1, 2, 4]
    else:
        try:
            lst = [float(s) for s in raw.split()]
        except ValueError:
            print("Błędne dane wejściowe.")
            return
    if not lst:
        print("Pusta lista.")
        return
    if any(x == 0 for x in lst):
        print("Lista zawiera 0 - średnia harmoniczna nieokreślona.")
        return
    try:
        hm = len(lst) / sum(1.0 / x for x in lst)
    except TypeError:
        print("Lista musi zawierać liczby.")
        return
    print("Średnia harmoniczna:", hm)
    return hm

# ----------------------------
# Wbudowane metody list - demonstracja
# ----------------------------

def demo_list_methods():
    """
    Krótka demonstracja najczęściej używanych metod list,
    zgodnie z przytoczoną listą w zadaniach.
    """
    print("--- Demo metod list ---")
    lista = [1, 2, 3]
    print("start:", lista)
    lista.append(4)
    print("append(4):", lista)
    lista2 = [5, 6]
    lista.extend(lista2)
    print("extend([5,6]):", lista)
    lista.insert(2, 99)
    print("insert(2,99):", lista)
    lista.remove(99)
    print("remove(99):", lista)
    x = lista.pop(2)
    print("pop(2) zwraca:", x, "lista teraz:", lista)
    idx = lista.index(5)
    print("index(5):", idx)
    count_5 = lista.count(5)
    print("count(5):", count_5)
    lista.sort()
    print("sort():", lista)
    lista.reverse()
    print("reverse():", lista)
    lista_copy = lista.copy()
    print("copy():", lista_copy)
    lista.clear()
    print("clear():", lista)
    print("--- Koniec demo metod list ---")

# ----------------------------
# Zadania do domu (interaktywnie)
# ----------------------------

def zadania_do_domu_interactive():
    """
    Realizacja kompletnego zadania domowego (10 punktów) interaktywnie:
    1. Utwórz pustą listę 'numbers'.
    2. Poproś użytkownika o podanie 5 liczb i dodaj je do listy.
    3. Oblicz sumę, max, min, średnią, ilość parzystych, duplicates, usuń powtórzenia, squares.
    """
    print("Zadanie do domu: wprowadź 5 liczb.")
    numbers: List[float] = []
    i = 0
    while i < 5:
        v = read_float(f"Podaj liczbę {i+1}/5: ")
        if v is None:
            print("Błąd wejścia.")
            continue
        numbers.append(v)
        i += 1
    print("numbers =", numbers)

    # 3. Suma
    suma = sum(numbers)
    print("3. Suma liczb w 'numbers':", suma)

    # 4. Największa
    my_max = numbers[0]
    i = 0
    while i < len(numbers):
        if my_max < numbers[i]:
            my_max = numbers[i]
        i += 1
    print("4. Największa liczba:", my_max)

    # 5. Najmniejsza
    my_min = numbers[0]
    i = 0
    while i < len(numbers):
        if my_min > numbers[i]:
            my_min = numbers[i]
        i += 1
    print("5. Najmniejsza liczba:", my_min)

    # 6. Średnia arytmetyczna - krok po kroku
    my_sum = 0
    i = 0
    while i < len(numbers):
        my_sum += numbers[i]
        i += 1
    avg = my_sum / len(numbers) if numbers else 0
    print("6. Średnia arytmetyczna:", avg)

    # 7. Ilość liczb parzystych (po rzutowaniu na int, by trzymać się treści przykładu)
    i = 0
    parzyste = 0
    while i < len(numbers):
        if int(numbers[i]) % 2 == 0:
            parzyste += 1
        i += 1
    print("7. Ilość liczb parzystych (po rzutowaniu na int):", parzyste)

    # 8. duplicates (powtarzające się elementy)
    # Przykład: użyjemy pierwotnej listy numbers i count()
    duplicates = []
    i = 0
    while i < len(numbers):
        if numbers.count(numbers[i]) > 1 and numbers[i] not in duplicates:
            duplicates.append(numbers[i])
        i += 1
    print("8. Powtarzające się elementy (duplicates):", duplicates)

    # 9. Usuń wszystkie powtarzające się elementy (utrzymaj kolejność)
    new_list: List[float] = []
    i = 0
    while i < len(numbers):
        if numbers[i] not in new_list:
            new_list.append(numbers[i])
        i += 1
    print("9. Lista bez powtórzeń:", new_list)

    # 10. Kwadraty liczb - squares
    squares = []
    i = 0
    while i < len(numbers):
        squares.append(numbers[i] ** 2)
        i += 1
    print("10. Kwadraty liczb (squares):", squares)

    return {
        "numbers": numbers,
        "sum": suma,
        "max": my_max,
        "min": my_min,
        "mean": avg,
        "even_count": parzyste,
        "duplicates": duplicates,
        "unique": new_list,
        "squares": squares
    }

# ----------------------------
# Dodatkowe zadanka do trenowania (if/while)
# ----------------------------

def extra_exercises():
    """
    Zawiera rozwiązania dodatkowych zadań do trenowania (pozycje 1-9 z dodatków).
    Każde zadanie interaktywne.
    """
    # 1.
    liczba = read_float("1) Podaj liczbę (sprawdzę czy dodatnia/ujemna/równa 0): ")
    if liczba is not None:
        if liczba > 0:
            print("Liczba jest dodatnia.")
        elif liczba < 0:
            print("Liczba jest ujemna.")
        else:
            print("Liczba jest równa zero.")
    # 2.
    wiek = read_int("2) Podaj swój wiek: ")
    if wiek is not None:
        if wiek >= 18:
            print("Jesteś pełnoletni.")
        else:
            print("Jesteś niepełnoletni.")
    # 3.
    n1 = read_float("3) Podaj pierwszą liczbę: ")
    n2 = read_float("   Podaj drugą liczbę: ")
    if n1 is not None and n2 is not None:
        if n1 > n2:
            print("Pierwsza liczba jest większa od drugiej.")
        elif n1 < n2:
            print("Druga liczba jest większa od pierwszej.")
        else:
            print("Obie liczby są równe.")
    # 4.
    lst = [1, 2, 3, 4, 5]
    val = read_int("4) Podaj liczbę do sprawdzenia, czy jest w liście [1,2,3,4,5]: ")
    if val is not None:
        if val in lst:
            print("Liczba znajduje się w liście.")
        else:
            print("Liczba nie znajduje się w liście.")
    # 5.
    ocena = read_int("5) Podaj ocenę szkolną: ")
    if ocena is not None:
        if ocena >= 4:
            print("Zaliczone.")
        else:
            print("Niezaliczone.")
    # 6.
    rok = read_int("6) Podaj rok: ")
    if rok is not None:
        if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
            print(f"{rok} jest rokiem przestępnym.")
        else:
            print(f"{rok} nie jest rokiem przestępnym.")
    # 7.
    liczba2 = read_int("7) Podaj liczbę do sprawdzenia parzystości: ")
    if liczba2 is not None:
        if liczba2 % 2 == 0:
            print("Liczba jest parzysta.")
        else:
            print("Liczba jest nieparzysta.")
    # 8.
    a = read_float("8) Podaj długość pierwszego boku trójkąta: ")
    b = read_float("   Podaj długość drugiego boku trójkąta: ")
    c = read_float("   Podaj długość trzeciego boku trójkąta: ")
    if a is not None and b is not None and c is not None:
        if a + b > c and b + c > a and c + a > b:
            print("Można zbudować trójkąt.")
        else:
            print("Nie można zbudować trójkąta.")
    # 9.
    liczba3 = read_int("9) Podaj liczbę żeby sprawdzić czy jest podzielna przez 3 i 5: ")
    if liczba3 is not None:
        if liczba3 % 3 == 0 and liczba3 % 5 == 0:
            print("Liczba jest podzielna przez 3 i 5.")
        else:
            print("Liczba nie jest podzielna przez 3 i 5.")

# ----------------------------
# Dalszy trening - While (zadania do domu)
# ----------------------------

SAMPLE_NUMBERS = [1,2,3,4,6,3,1,1,3,4,5,6,7,7,-10,-20,100]

def while_reverse_print(numbers: List[Any] = SAMPLE_NUMBERS):
    """
    Wyświetl wszystkie liczby z listy "numbers" w odwrotnej kolejności.
    Realizacja przy użyciu pętli while.
    """
    print("Wyświetlanie listy w odwrotnej kolejności (while):")
    i = -1
    while i >= -len(numbers):
        print(numbers[i])
        i -= 1

def while_check_in_list(numbers: List[Any] = SAMPLE_NUMBERS):
    """
    Poproś użytkownika o podanie liczby. Sprawdź, czy liczba ta znajduje się w liście "numbers".
    """
    inp = read_int("Podaj liczbę do sprawdzenia czy jest w SAMPLE_NUMBERS: ")
    if inp is None:
        return
    if inp in numbers:
        print("Tak")
    else:
        print("Nie")

def while_first_index(numbers: List[Any] = SAMPLE_NUMBERS):
    """
    Wyświetl indeks pierwszego wystąpienia danej liczby w liście "numbers".
    """
    inp = read_int("Podaj liczbę, znajdę jej pierwszy indeks: ")
    if inp is None:
        return
    i = 0
    found = False
    while i < len(numbers):
        if numbers[i] == inp:
            print("Indeks pierwszego wystąpienia:", i)
            found = True
            break
        i += 1
    if not found:
        print("Brak elementu w liście.")

def while_count_greater_than_10(numbers: List[Any] = SAMPLE_NUMBERS):
    """
    Znajdź ilość liczb większych niż 10 w liście "numbers".
    """
    ile = 0
    i = 0
    while i < len(numbers):
        if numbers[i] > 10:
            ile += 1
        i += 1
    print("Ilość liczb większych niż 10:", ile)
    return ile

def while_sort_desc(numbers: List[Any] = SAMPLE_NUMBERS):
    """
    Posortuj listę "numbers" w kolejności malejącej (pokaż wynik).
    """
    s = sorted(numbers, reverse=True)
    print("Posortowana malejąco:", s)
    return s

def while_second_largest(numbers: List[Any] = SAMPLE_NUMBERS):
    """
    Znajdź drugą największą liczbę w liście "numbers".
    Implementacja ze złożonością O(n) i zachowaniem unikatów.
    """
    print("Szukanie dwóch największych wartości (while).")
    max1 = float('-inf')
    max2 = float('-inf')
    i = 0
    while i < len(numbers):
        val = numbers[i]
        if val > max1:
            max2 = max1
            max1 = val
        elif val > max2 and val != max1:
            max2 = val
        i += 1
    if max2 == float('-inf'):
        print("Brak drugiej największej (za mało unikatowych wartości).")
        return None
    print("Druga największa liczba:", max2)
    return max2

def while_doubled_numbers(numbers: List[Any] = SAMPLE_NUMBERS):
    """
    Stwórz nową listę 'doubled_numbers' zawierającą podwojoną wartość każdej liczby z listy 'numbers'.
    """
    doubled = []
    i = 0
    while i < len(numbers):
        doubled.append(numbers[i] * 2)
        i += 1
    print("Doubled numbers:", doubled)
    return doubled

def while_count_occurrences(numbers: List[Any] = SAMPLE_NUMBERS):
    """
    Zlicz ilość wystąpień danej liczby w liście 'numbers' (używając while).
    """
    try:
        inp = float(input("Podaj liczbę (float/int) do zliczenia wystąpień: "))
    except ValueError:
        print("Błędne wejście.")
        return
    i = 0
    ile = 0
    while i < len(numbers):
        if numbers[i] == inp:
            ile += 1
        i += 1
    print(f"Ilość wystąpień {inp}:", ile)
    return ile

def while_print_with_indices(numbers: List[Any] = SAMPLE_NUMBERS):
    """
    Wyświetl wszystkie liczby z listy 'numbers' z ich indeksami (while).
    """
    i = 0
    while i < len(numbers):
        print(f"{i} {numbers[i]}")
        i += 1

# ----------------------------
# Przykładowe uruchomienie wszystkich zadań (duży blok)
# ----------------------------

def run_all_demos():
    """
    Funkcja demonstracyjna: uruchamia KAŻDE zadanie w sekwencji z przykładowymi danymi.
    To jest 'pełne' uruchomienie — nie skracane, pokazuje wszystkie funkcje.
    """
    print("\n\n=== DEMO: perhaps_bot (jedno pytanie) ===")
    print("Pytanie: 'Jak leci?'\nOdpowiedź:", perhaps_bot_once_example("Jak leci?"))

    print("\n=== DEMO: divisible_by_9_up_to (0..50) ===")
    print(divisible_by_9_up_to(50))

    print("\n=== DEMO: not_divisible_by_3_up_to (0..10) ===")
    print(not_divisible_by_3_up_to(10))

    print("\n=== DEMO: powers_of_two (n=10) ===")
    print(powers_of_two(10))

    print("\n=== DEMO: sum_divisible_by_5_up_to (n=50) ===")
    print(sum_divisible_by_5_up_to(50))

    print("\n=== DEMO: love_programming (n=5) ===")
    for line in love_programming(5):
        print(line)

    print("\n=== DEMO: is_prime tests ===")
    for v in [1,2,3,4,13,25,97,100]:
        print(v, "->", is_prime(v))

    print("\n=== DEMO: input_list_x_from_iterable ===")
    print(input_list_x_from_iterable(['10','20','300','150','abc','50'], 4))

    print("\n=== DEMO: filter_even_50_70 ===")
    print(filter_even_50_70([10,51,52,60,69,70,88]))

    print("\n=== DEMO: grades_average_from_iterable ===")
    print(grades_average_from_iterable([5,4,6,3,4], 5))
    print(grades_average_from_iterable([5,9,4], 3))

    print("\n=== DEMO: random_list (n=7) ===")
    print(random_list(7))

    print("\n=== DEMO: harmonic_mean ===")
    print(harmonic_mean([1,2,4]))

    print("\n=== DEMO: zadania_do_domu - example call (non-interactive):")
    sample = zadania_do_domu_example([1,1,2,3,4])
    print(sample)

    print("\n=== DEMO: while tasks on SAMPLE_NUMBERS ===")
    while_reverse_print()
    while_check_in_list()
    while_first_index()
    while_count_greater_than_10()
    while_sort_desc()
    while_second_largest()
    while_doubled_numbers()
    while_count_occurrences()
    while_print_with_indices()

# Dodatkowe funkcje "beznadzwyczajne" używane w demo (nie-interaktywne wersje)
def perhaps_bot_once_example(question: str) -> str:
    """Zwraca 'perhaps' dla jednego pytania (używane w demo)."""
    _ = question
    return "perhaps"

def divisible_by_9_up_to(n: int) -> List[int]:
    """Zwraca listę liczb podzielnych przez 9 do wartości n (włącznie)."""
    if n >= 0:
        rng = range(0, n + 1)
    else:
        rng = range(n, 1)
    return [i for i in rng if i % 9 == 0]

def not_divisible_by_3_up_to(n: int) -> List[int]:
    """Zwraca listę liczb niepodzielnych przez 3 do n."""
    if n >= 0:
        rng = range(0, n + 1)
    else:
        rng = range(n, 1)
    return [i for i in rng if i % 3 != 0]

def powers_of_two(n: int) -> List[int]:
    """Zwraca listę n potęg liczby 2."""
    if n <= 0:
        return []
    return [2**i for i in range(n)]

def sum_divisible_by_5_up_to(n: int) -> int:
    """Sumuje liczby podzielne przez 5 do n."""
    if n >= 0:
        rng = range(0, n + 1)
    else:
        rng = range(n, 1)
    return sum(i for i in rng if i % 5 == 0)

def love_programming(n: int) -> List[str]:
    """Zwraca listę z n razy frazą 'Kocham programować!'"""
    return ["Kocham programować!"] * max(0, n)

def input_list_x_from_iterable(iterable, x: int, low=1, high=200) -> List[int]:
    """
    Buduje listę x liczb pobranych z iterable (np. listy wejściowej zamiast input),
    filtrując zakres low..high.
    """
    lst = []
    for val in iterable:
        if len(lst) >= x:
            break
        try:
            v = int(val)
        except (ValueError, TypeError):
            continue
        if low <= v <= high:
            lst.append(v)
    return lst

def filter_even_50_70(lst: List[int]) -> List[int]:
    """Z listy zwraca liczby parzyste >50 i <70."""
    return [x for x in lst if isinstance(x, int) and x % 2 == 0 and 50 < x < 70]

def grades_average_from_iterable(iterable, x: int) -> Tuple[Optional[float], Optional[str]]:
    """
    Pobiera x ocen z iterable, sprawdza czy wszystkie w 1..6.
    Jeśli któraś spoza zakresu -> zwraca (None, komunikat błędu).
    """
    grades = []
    for val in iterable:
        if len(grades) >= x:
            break
        try:
            g = int(val)
        except (ValueError, TypeError):
            return None, "To nie jest liczba całkowita."
        if g < 1 or g > 6:
            return None, "podałeś złe liczby Nobie!"
        grades.append(g)
    if len(grades) < x:
        return None, "Za mało ocen."
    avg = sum(grades) / x
    return avg, None

def random_list(n: int, low=1, high=100) -> List[int]:
    """Generuje losową listę długości n w zakresie [low, high]."""
    if n <= 0:
        return []
    return [random.randint(low, high) for _ in range(n)]

def harmonic_mean(lst: List[float]) -> Optional[float]:
    """Oblicza średnią harmoniczną listy (zabezpieczona przed zerami)."""
    if not lst:
        return None
    try:
        if any(x == 0 for x in lst):
            return None
        return len(lst) / sum(1.0 / x for x in lst)
    except TypeError:
        return None

# Funkcja pomocnicza dla przykładowej nie-interaktywnej realizacji zadania domowego
def zadania_do_domu_example(numbers: List[float]) -> dict:
    """
    Realizacja zadań domowych bez interakcji - przyjmujemy listę numbers.
    Zwraca słownik z wynikami (sum, max, min, mean, even_count, duplicates, unique, squares)
    """
    if len(numbers) == 0:
        return {}
    # suma
    suma = 0
    i = 0
    while i < len(numbers):
        suma += numbers[i]
        i += 1
    # max
    my_max = numbers[0]
    i = 0
    while i < len(numbers):
        if my_max < numbers[i]:
            my_max = numbers[i]
        i += 1
    # min
    my_min = numbers[0]
    i = 0
    while i < len(numbers):
        if my_min > numbers[i]:
            my_min = numbers[i]
        i += 1
    # średnia
    mean = suma / len(numbers)
    # parzyste (po rzutowaniu int)
    i = 0
    parzyste = 0
    while i < len(numbers):
        if int(numbers[i]) % 2 == 0:
            parzyste += 1
        i += 1
    # duplicates
    duplicates = []
    i = 0
    while i < len(numbers):
        if numbers.count(numbers[i]) > 1 and numbers[i] not in duplicates:
            duplicates.append(numbers[i])
        i += 1
    # unique
    unique = []
    i = 0
    while i < len(numbers):
        if numbers[i] not in unique:
            unique.append(numbers[i])
        i += 1
    # squares
    squares = []
    i = 0
    while i < len(numbers):
        squares.append(numbers[i]**2)
        i += 1
    return {
        "numbers": numbers,
        "sum": suma,
        "max": my_max,
        "min": my_min,
        "mean": mean,
        "even_count": parzyste,
        "duplicates": duplicates,
        "unique": unique,
        "squares": squares
    }

# ----------------------------
# Główne menu (pełne, interaktywne) - użytkownik może uruchomić dowolne zadanie
# ----------------------------

def main_menu():
    """
    Główne, pełne menu uruchamiające wszystkie zadania interaktywnie.
    Menu nie jest skracane — zawiera każdą opcję z materiału.
    """
    while True:
        print("\n====== GŁÓWNE MENU ZADAŃ (PEŁNE) ======")
        print("1. Zadania wprowadzające (lista opcji)")
        print("2. Demo metod list")
        print("3. Zadania do domu (interaktywnie)")
        print("4. Dodatkowe zadanka do trenowania (if/while)")
        print("5. Dalszy trening - While (lista operacji)")
        print("6. Uruchom pełne demo wszystkich zadań (non-interactive przykłady)")
        print("0. Wyjście")
        choice = read_int("Wybierz opcję: ")
        if choice is None:
            continue
        if choice == 0:
            print("Koniec. Do widzenia.")
            break
        elif choice == 1:
            intro_submenu()
        elif choice == 2:
            demo_list_methods()
        elif choice == 3:
            zadania_do_domu_interactive()
        elif choice == 4:
            extra_exercises()
        elif choice == 5:
            while_submenu()
        elif choice == 6:
            run_all_demos()
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

def intro_submenu():
    """
    Podmenu dla zadań wprowadzających — pełna lista zadań i uruchamialnymi funkcjami.
    """
    while True:
        print("\n--- Zadania wprowadzające ---")
        print("1. perhaps (bot odpowiada 'perhaps')")
        print("2. Wyświetl liczby podzielne przez 9 do n")
        print("3. Wyświetl liczby NIE podzielne przez 3 do n")
        print("4. Wyświetl n potęg liczby 2")
        print("5. Suma liczb podzielnych przez 5 do n")
        print("6. Wyświetl n razy 'Kocham programować!'")
        print("7. Sprawdź czy liczba jest pierwsza")
        print("8. Stwórz listę x liczb (1..200)")
        print("9. Filtruj parzyste >50 i <70 z listy")
        print("10. Wprowadź oceny 1..6 i policz średnią (komunikat błędu jeśli poza 1..6)")
        print("11. Wygeneruj losową listę n elementów (1..100)")
        print("12. Oblicz średnią harmoniczną listy")
        print("0. Powrót")
        c = read_int("Wybierz opcję: ")
        if c is None:
            continue
        if c == 0:
            return
        elif c == 1:
            perhaps_bot()
        elif c == 2:
            divisible_by_9_up_to_interactive()
        elif c == 3:
            not_divisible_by_3_up_to_interactive()
        elif c == 4:
            powers_of_two_interactive()
        elif c == 5:
            sum_divisible_by_5_up_to_interactive()
        elif c == 6:
            love_programming_interactive()
        elif c == 7:
            is_prime_interactive()
        elif c == 8:
            input_list_x_interactive()
        elif c == 9:
            filter_even_50_70_interactive()
        elif c == 10:
            grades_average_interactive()
        elif c == 11:
            generate_random_list_interactive()
        elif c == 12:
            harmonic_mean_interactive()
        else:
            print("Nieznana opcja.")

def while_submenu():
    """
    Podmenu dla zadań 'While - dalszy trening' — wszystkie zadania z tej sekcji.
    """
    numbers = SAMPLE_NUMBERS.copy()
    while True:
        print("\n--- While: dalszy trening ---")
        print("Aktualna lista (SAMPLE_NUMBERS):", numbers)
        print("1. Wyświetl wszystkie liczby w odwrotnej kolejności")
        print("2. Sprawdź czy podana liczba znajduje się w liście")
        print("3. Wyświetl indeks pierwszego wystąpienia")
        print("4. Znajdź ilość liczb większych niż 10")
        print("5. Posortuj listę malejąco (pokaż wynik)")
        print("6. Znajdź drugą największą liczbę")
        print("7. Stwórz listę doubled_numbers (wartości *2)")
        print("8. Zlicz ilość wystąpień danej liczby")
        print("9. Wyświetl wszystkie liczby z indeksami")
        print("10. Zmień listę (wczytaj nowe wartości)")
        print("0. Powrót")
        c = read_int("Wybierz opcję: ")
        if c is None:
            continue
        if c == 0:
            return
        elif c == 1:
            while_reverse_print(numbers)
        elif c == 2:
            while_check_in_list(numbers)
        elif c == 3:
            while_first_index(numbers)
        elif c == 4:
            while_count_greater_than_10(numbers)
        elif c == 5:
            numbers = while_sort_desc(numbers)
        elif c == 6:
            while_second_largest(numbers)
        elif c == 7:
            while_doubled_numbers(numbers)
        elif c == 8:
            while_count_occurrences(numbers)
        elif c == 9:
            while_print_with_indices(numbers)
        elif c == 10:
            raw = input("Podaj wartości listy rozdzielone spacjami: ")
            try:
                numbers = [float(s) for s in raw.split()]
                print("Nowa lista ustawiona.")
            except ValueError:
                print("Błędne dane. Lista nie została zmieniona.")
        else:
            print("Nieznana opcja.")

# ----------------------------
# Uruchomienie (jeśli skrypt wywołany bezpośrednio)
# ----------------------------

if __name__ == "__main__":
    try:
        # Użytkownik powiedział "nie skracaj", więc uruchamiamy pełne menu,
        # dając możliwość uruchomienia każdego zadania w pełnej wersji.
        main_menu()
    except KeyboardInterrupt:
        print("\nPrzerwano działanie programu. Do widzenia.")
        sys.exit(0)
