from random import randint

# Sumowanie 1..n
# Wyczytaj n i policz sumę liczb od 1 do n pętlą while.

# n = int(input())
# s = 0 
# while n > 0:
#     s += n
#     n -= 1
# print(s)
    
    
# Zgadywanie 1-100
# Komputer losuje liczbę z zakresu 1-100. Użytkownik zgaduje, a komputer podpowiada czy liczba jest za duża czy za mała.


# n = randint(1, 100)
# while True:
#     guess = int(input("Zgadnij liczbę (1-100): "))
#     if guess < n:
#         print("Za mało!")
#     elif guess > n:
#         print("Za dużo!")
#     else:
#         print("Brawo! Zgadłeś!")
#         break


# Dzielenie bez tajemnic
# Wczytaj dwie liczby całkowite a i b. Wypisz a/b,a//b,a%b.Obsłuż dzielenie przez 0.
# a = int(input("a = "))
# b = int(input("b = "))

# if b == 0:
#     print("Dzielenie przez 0!")
# else:
#     print("a/b =", a / b)
#     print("a//b =", a // b)
#     print("a%b =", a % b)
#     print("Sprawdzenie: a = b * (a//b) + (a%b) =", b * (a // b) + (a % b))


# Parzyste vs nieparzyste
# Wyczytuj liczby aż do wpisania 0. Policz ile było liczb parzystych i nieparzystych.

# cz.1
# even_count = 0
# odd_count = 0
# while True:
#     num = int(input("Podaj liczbę (0 - koniec): "))
#     if num == 0:
#         break
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print("Liczby parzyste:", even_count)
# print("Liczby nieparzyste:", odd_count)

# cz.2
# pa = 0
# nie_pa = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     if n % 2 == 0:
#         pa += 1
#     else:
#         nie_pa += 1
# print(f"parzyste: {pa}, nieparzyste: {nie_pa}") 


# Dwie szóstki z rzędu
#symuluj rzuty kostką(1-6) aż wypadną dwie kolejne "6".Wypisz liczbę rzutów.

# cz.1
# import random
# count = 0
# consecutive_sixes = 0
# while consecutive_sixes < 2:
#     roll = random.randint(1, 6)
#     count += 1
#     print(f"Rzut {count}: {roll}")
#     if roll == 6:
#         consecutive_sixes += 1
#     else:
#         consecutive_sixes = 0
# print(f"Wypadły dwie szóstki z rzędu po {count} rzutach.")

# cz.2
# ile = 0 
# r = 0
# while True:
#     los = randint(1,6)
#     if los == 6 and r == 1:
#         ile += 1
#         break
#     elif los != 6:
#         r = 0
#     elif los == 6:
#         r += 1
# print(ile)


#Mini-bankomat
#Saldo startowe 0.W pętli menu: 1) wypłata, 2) wpłata, 3) wyświetl saldo, 4) koniec.Obsłuż błędy (np. wypłata większa niż saldo).



# saldo = 0
# while True:
#     print("1 - wypłata")
#     print("2 - wpłata")
#     print("3 - wyświetl saldo")
#     print("4 - koniec")
#     choice = input("Wybierz opcję: ")
#     if choice == "1":
#         amount = float(input("Podaj kwotę do wypłaty: "))
#         if amount > saldo:
#             print("Niewystarczające środki!")
#         else:
#             saldo -= amount
#             print(f"Wypłacono {amount}. Nowe saldo: {saldo}")
#     elif choice == "2":
#         amount = float(input("Podaj kwotę do wpłaty: "))
#         saldo += amount
#         print(f"Wpłacono {amount}. Nowe saldo: {saldo}")
#     elif choice == "3":
#         print(f"Aktualne saldo: {saldo}")
#     elif choice == "4":
#         print("Koniec programu.")
#         break
#     else:
#         print("Nieprawidłowa opcja, spróbuj ponownie.")


# Średnia z losowań
# Wczytaj 10 liczb 1-50 i wypisz ich średnią oraz ile jest podzielnych przez 5.

# suma = 0
# licznik = 0
# for i in range(10):
#     n = int(input("Podaj liczbę (1-50): "))
#     if 1 <= n <= 50:
#         suma += n
#         if n % 5 == 0:
#             licznik += 1
#     else:
#         print("Liczba poza zakresem!")

# if licznik > 0:
#     print("Średnia:", suma / 10)
#     print("Liczby podzielne przez 5:", licznik)
# else:
#     print("Brak liczb podzielnych przez 5.")


# Wyczytaj k. Losuj liczby 1-100, aż trafisz liczbę podzielną przez k . Zlicz próby.

# import random
# k = int(input("Podaj k: "))
# count = 0
# while True:
#     n = random.randint(1, 100)
#     count += 1
#     print(f"Wylosowano: {n}")
#     if n % k == 0:
#         break
# print(f"Trafiono liczbę podzielną przez {k} po {count} próbach.")


# Liczenie cyfr w liczbie
# Podaj ile cyfr ma liczba dodatnia n bez zamiany na string.

# n = int(input("Podaj liczbę dodatnią: "))
# if n <= 0:
#     print("Liczba nie jest dodatnia!")
# else:
#     count = 0
#     while n > 0:
#         n //= 10
#         count += 1
#     print("Liczba cyfr:", count)

# Silna z kontrolą wejścia
# Policz n! pętlą while. Dla n<0 wypisz błąd.


# n = int(input("Podaj liczbę całkowitą: "))
# if n < 0:
#     print("Błąd: n musi być liczbą całkowitą nieujemną.")
# else:
#     wynik = 1
#     while n > 0:
#         wynik *= n
#         n -= 1
#     print("Silnia:", wynik)  

# Potęga dwójki
# Wczytaj n i sprawdź czy jest potęgą dwójki, dzieląc n przez 2 dopóki n%2==0.

# n = int(input("Podaj liczbę całkowitą: "))
# if n <= 0: 
#     print("Błąd: n musi być liczbą całkowitą dodatnią.")
# else:
#     while n % 2 == 0:
#         n //= 2
#     if n == 1:
#         print("Liczba jest potęgą dwójki.")
#     else:
#         print("Liczba nie jest potęgą dwójki.")


# Potęga osiem 
# Napisz program sprawdzający czy n jest potęgą 8 oraz ile razy (używając logarytmów rozszerzonej matematyki) dzieląc n przez 8 dopóki n%8==0. 

# import math
# n = int(input("Podaj liczbę całkowitą: "))
# if n <= 0:
#     print("Błąd: n musi być liczbą całkowitą dodatnią.")
# else:
#     count = 0
#     while n % 8 == 0:
#         n //= 8
#         count += 1
#     if n == 1:
#         print("Liczba jest potęgą ósemki.")
#         print("Liczba podzielona przez 8:", count)
#     else:
#         print("Liczba nie jest potęgą ósemki.") 
#     print("Liczba podzielona przez 8:", count)
#     print("Sprawdzenie logarytmiczne:", math.log(n, 8) if n > 0 else "N/A")
