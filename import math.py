import math

def get_positive_float(prompt):
    """Pobiera od użytkownika dodatnią liczbę zmiennoprzecinkową."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Podaj wartość większą od 0.")
            else:
                return value
        except ValueError:
            print("Błąd: podaj prawidłową liczbę.")

def menu_plaskie():
    while True:
        print("""
=== FIGURY PŁASKIE ===
a - Koło
b - Kwadrat
c - Prostokąt
d - Trójkąt (Heron)
e - Trójkąt równoboczny
f - Trapez
g - Równoległobok
h - Romb
q - Powrót do menu głównego
""")
        fig = input("Wybierz figurę: ").lower()
        if fig == "q":
            break
        try:
            if fig == "a":
                r = get_positive_float("Promień r = ")
                pole = math.pi * r**2
                obw = 2 * math.pi * r
                print(f"Pole koła = {round(pole, 2)}")
                print(f"Obwód koła = {round(obw, 2)}")

            elif fig == "b":
                a = get_positive_float("Bok a = ")
                pole = a**2
                obw = 4 * a
                przekatna = a * math.sqrt(2)
                print(f"Pole kwadratu = {round(pole, 2)}")
                print(f"Obwód kwadratu = {round(obw, 2)}")
                print(f"Przekątna kwadratu = {round(przekatna, 2)}")

            elif fig == "c":
                a = get_positive_float("Bok a = ")
                b = get_positive_float("Bok b = ")
                pole = a * b
                obw = 2 * (a + b)
                print(f"Pole prostokąta = {round(pole, 2)}")
                print(f"Obwód prostokąta = {round(obw, 2)}")

            elif fig == "d":
                a = get_positive_float("Bok a = ")
                b = get_positive_float("Bok b = ")
                c = get_positive_float("Bok c = ")
                if a + b > c and a + c > b and b + c > a:
                    obw = a + b + c
                    s = obw / 2
                    pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
                    print(f"Obwód trójkąta = {round(obw, 2)}")
                    print(f"Pole trójkąta = {round(pole, 2)}")
                else:
                    print("Z tych boków nie da się zbudować trójkąta.")

            elif fig == "e":
                a = get_positive_float("Bok a = ")
                pole = (a**2 * math.sqrt(3)) / 4
                obw = 3 * a
                h = (a * math.sqrt(3)) / 2
                print(f"Pole trójkąta równobocznego = {round(pole, 2)}")
                print(f"Obwód trójkąta równobocznego = {round(obw, 2)}")
                print(f"Wysokość trójkąta równobocznego = {round(h, 2)}")

            elif fig == "f":
                a = get_positive_float("Podstawa a = ")
                b = get_positive_float("Podstawa b = ")
                h = get_positive_float("Wysokość h = ")
                c = get_positive_float("Bok c = ")
                d = get_positive_float("Bok d = ")
                pole = ((a + b) * h) / 2
                obw = a + b + c + d
                print(f"Pole trapezu = {round(pole, 2)}")
                print(f"Obwód trapezu = {round(obw, 2)}")

            elif fig == "g":
                a = get_positive_float("Bok a = ")
                b = get_positive_float("Bok b = ")
                h = get_positive_float("Wysokość h do boku a = ")
                pole = a * h
                obw = 2 * (a + b)
                print(f"Pole równoległoboku = {round(pole, 2)}")
                print(f"Obwód równoległoboku = {round(obw, 2)}")

            elif fig == "h":
                print("Jak chcesz policzyć pole rombu?")
                print("1 - P = a * h (bok i wysokość)")
                print("2 - P = (e * f) / 2 (przekątne)")
                wybor = input("1 / 2 ? ")
                if wybor == "1":
                    a = get_positive_float("Bok a = ")
                    h = get_positive_float("Wysokość h = ")
                    pole = a * h
                    obw = 4 * a
                    print(f"Pole rombu = {round(pole, 2)}")
                    print(f"Obwód rombu = {round(obw, 2)}")
                elif wybor == "2":
                    a = get_positive_float("Bok a = ")
                    e = get_positive_float("Przekątna e = ")
                    f = get_positive_float("Przekątna f = ")
                    pole = (e * f) / 2
                    obw = 4 * a
                    print(f"Pole rombu = {round(pole, 2)}")
                    print(f"Obwód rombu = {round(obw, 2)}")
                else:
                    print("Nie ma takiej opcji.")
            else:
                print("Nie ma takiej figury.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")

def menu_bryly():
    while True:
        print("""
=== BRYŁY ===
a - Sześcian
b - Prostopadłościan
c - Walec
d - Kula
e - Stożek
f - Graniastosłup
g - Ostrosłup
q - Powrót do menu głównego
""")
        bryla = input("Wybierz bryłę: ").lower()
        if bryla == "q":
            break
        try:
            if bryla == "a":
                a = get_positive_float("Bok a = ")
                pole = 6 * a**2
                objetosc = a**3
                print(f"Pole powierzchni sześcianu = {round(pole, 2)}")
                print(f"Objętość sześcianu = {round(objetosc, 2)}")

            elif bryla == "b":
                a = get_positive_float("Bok a = ")
                b = get_positive_float("Bok b = ")
                c = get_positive_float("Bok c = ")
                pole = 2 * (a*b + a*c + b*c)
                objetosc = a*b*c
                print(f"Pole powierzchni prostopadłościanu = {round(pole, 2)}")
                print(f"Objętość prostopadłościanu = {round(objetosc, 2)}")

            elif bryla == "c":
                r = get_positive_float("Promień r = ")
                h = get_positive_float("Wysokość h = ")
                pole = 2 * math.pi * r * (r + h)
                objetosc = math.pi * r**2 * h
                print(f"Pole powierzchni walca = {round(pole, 2)}")
                print(f"Objętość walca = {round(objetosc, 2)}")

            elif bryla == "d":
                r = get_positive_float("Promień r = ")
                pole = 4 * math.pi * r**2
                objetosc = (4/3) * math.pi * r**3
                print(f"Pole powierzchni kuli = {round(pole, 2)}")
                print(f"Objętość kuli = {round(objetosc, 2)}")

            elif bryla == "e":
                r = get_positive_float("Promień r = ")
                h = get_positive_float("Wysokość h = ")
                l = math.sqrt(r**2 + h**2)  # tworząca
                pole = math.pi * r * (r + l)
                objetosc = (1/3) * math.pi * r**2 * h
                print(f"Tworząca l (obliczona) = {round(l, 2)}")
                print(f"Pole powierzchni stożka = {round(pole, 2)}")
                print(f"Objętość stożka = {round(objetosc, 2)}")

            elif bryla == "f":  # Graniastosłup
                print("Jak podasz dane graniastosłupa?")
                print("1 - podaj Pp (pole podstawy), Pb (pole ścian bocznych) i H")
                print("2 - podaj Pp, obwód podstawy i H (wyliczę Pb = obw * H)")
                m = input("1 / 2 ? ")
                if m == "1":
                    Pp = get_positive_float("Pp (pole podstawy) = ")
                    Pb = get_positive_float("Pb (pole ścian bocznych) = ")
                    H = get_positive_float("Wysokość H = ")
                elif m == "2":
                    Pp = get_positive_float("Pp (pole podstawy) = ")
                    obw = get_positive_float("Obwód podstawy = ")
                    H = get_positive_float("Wysokość H = ")
                    Pb = obw * H
                    print(f"Obliczone Pb (pole ścian bocznych) = {round(Pb, 2)}")
                else:
                    print("Nie ma takiej opcji.")
                    continue
                pole = 2 * Pp + Pb
                objetosc = Pp * H
                print(f"Pole powierzchni graniastosłupa = {round(pole, 2)}")
                print(f"Objętość graniastosłupa = {round(objetosc, 2)}")

            elif bryla == "g":  # Ostrosłup
                print("Jak podasz dane ostrosłupa?")
                print("1 - podaj Pp (pole podstawy), Pb (pole ścian bocznych) i H")
                print("2 - podaj Pp, obwód podstawy i tworzącą l (wyliczę Pb = 0.5 * obw * l)")
                m = input("1 / 2 ? ")
                if m == "1":
                    Pp = get_positive_float("Pp (pole podstawy) = ")
                    Pb = get_positive_float("Pb (pole ścian bocznych) = ")
                    H = get_positive_float("Wysokość H = ")
                elif m == "2":
                    Pp = get_positive_float("Pp (pole podstawy) = ")
                    obw = get_positive_float("Obwód podstawy = ")
                    l = get_positive_float("Tworząca l = ")
                    H = get_positive_float("Wysokość H = ")
                    Pb = 0.5 * obw * l
                    print(f"Obliczone Pb (pole ścian bocznych) = {round(Pb, 2)}")
                else:
                    print("Nie ma takiej opcji.")
                    continue
                pole = Pp + Pb
                objetosc = (1/3) * Pp * H
                print(f"Pole powierzchni ostrosłupa = {round(pole, 2)}")
                print(f"Objętość ostrosłupa = {round(objetosc, 2)}")

            else:
                print("Nie ma takiej bryły.")
        except Exception as e:
            print(f"Wystąpił błąd: {e}")

def main():
    while True:
        print("""
=== KALKULATOR GEOMETRII ===
a - Figury płaskie
b - Bryły
q - Wyjście
""")
        main_choice = input("Wybór: ").lower()
        if main_choice == "a":
            menu_plaskie()
        elif main_choice == "b":
            menu_bryly()
        elif main_choice == "q":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowa opcja.")

if __name__ == "__main__":
    main()
