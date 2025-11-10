import math

# Tutaj będziemy przechowywać historię wszystkich obliczeń.
# To taka nasza "pamięć" programu, żebyśmy nie musieli niczego notować.
historia = []

def dodaj_do_historii(tekst):
    """Prosta funkcja, która dopisuje wynik do naszej listy historii."""
    historia.append(tekst)

def wyswietl_historie():
    """Wyświetla wszystko, co zapisaliśmy w historii."""
    print("\n=== HISTORIA OBLICZEŃ ===")
    if not historia:
        print("Jeszcze nic nie liczyliśmy. Historia jest pusta.")
    else:
        for i, wpis in enumerate(historia, 1):
            print(f"{i}. {wpis}")
    input("\nNaciśnij Enter, aby wrócić do menu...")

def wyczysc_historie():
    """Kasuje całą historię. Zaczynamy od nowa."""
    historia.clear()
    print("Historia została wyczyszczona.")
    input("Naciśnij Enter, aby wrócić do menu...")

def wczytaj_liczbe(prompt):
    """Pobiera od użytkownika liczbę, ale sprawdza, czy to na pewno liczba i czy jest większa od zera."""
    while True:
        try:
            liczba = float(input(prompt))
            if liczba <= 0:
                print("Proszę, podaj liczbę dodatnią.")
                continue
            return liczba
        except ValueError:
            print("Błąd: To nie jest liczba. Spróbuj jeszcze raz.")

def kalkulator_geometrii():
    """To jest serce programu. Stąd wszystko się zaczyna."""
    print("=== KALKULATOR GEOMETRII 📐 ===")
    
    while True:
        # Pokaż dostępne opcje
        print("\n=== MENU GŁÓWNE ===")
        print("1. Figury płaskie")
        print("2. Bryły")
        print("3. Historia obliczeń")
        print("4. Wyczyść historię")
        print("q. Wyjście")
        
        wybor = input("Wybierz opcję: ").lower()

        if wybor == '1':
            menu_figur_plaskich()
        elif wybor == '2':
            menu_bryl()
        elif wybor == '3':
            wyswietl_historie()
        elif wybor == '4':
            wyczysc_historie()
        elif wybor == 'q':
            print("Do widzenia!")
            break
        else:
            print("Nie ma takiej opcji. Spróbuj ponownie.")

def menu_figur_plaskich():
    """Menu do obliczania figur 2D."""
    print("""
=== FIGURY PŁASKIE ===
a - Koło
b - Kwadrat
c - Prostokąt
d - Trójkąt
e - Równoległobok
f - Trapez
""")
    figura = input("Wybierz figurę: ").lower()
    
    try:
        if figura == "a":
            # Koło
            r = wczytaj_liczbe("Podaj promień (r): ")
            pole = math.pi * r**2
            obwod = 2 * math.pi * r
            print(f"Pole koła = {pole:.2f}")
            print(f"Obwód koła = {obwod:.2f}")
            dodaj_do_historii(f"Koło: r={r}, Pole={pole:.2f}, Obwód={obwod:.2f}")
        
        elif figura == "b":
            # Kwadrat
            a = wczytaj_liczbe("Podaj bok (a): ")
            pole = a**2
            obwod = 4 * a
            przekatna = a * math.sqrt(2)
            print(f"Pole kwadratu = {pole:.2f}")
            print(f"Obwód kwadratu = {obwod:.2f}")
            print(f"Przekątna kwadratu = {przekatna:.2f}")
            dodaj_do_historii(f"Kwadrat: a={a}, Pole={pole:.2f}, Obwód={obwod:.2f}")
            
        elif figura == "c":
            # Prostokąt
            a = wczytaj_liczbe("Podaj bok (a): ")
            b = wczytaj_liczbe("Podaj bok (b): ")
            pole = a * b
            obwod = 2 * (a + b)
            print(f"Pole prostokąta = {pole:.2f}")
            print(f"Obwód prostokąta = {obwod:.2f}")
            dodaj_do_historii(f"Prostokąt: a={a}, b={b}, Pole={pole:.2f}, Obwód={obwod:.2f}")
            
        elif figura == "d":
            # Trójkąt (wzór Herona)
            a = wczytaj_liczbe("Podaj bok (a): ")
            b = wczytaj_liczbe("Podaj bok (b): ")
            c = wczytaj_liczbe("Podaj bok (c): ")
            if a + b > c and a + c > b and b + c > a:
                # Sprawdzamy, czy da się w ogóle zbudować trójkąt
                s = (a + b + c) / 2 # To jest połowa obwodu, potrzebna do wzoru Herona
                pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
                obwod = a + b + c
                print(f"Pole trójkąta = {pole:.2f}")
                print(f"Obwód trójkąta = {obwod:.2f}")
                dodaj_do_historii(f"Trójkąt: a={a}, b={b}, c={c}, Pole={pole:.2f}, Obwód={obwod:.2f}")
            else:
                print("Z tych boków nie da się zbudować trójkąta. Spróbuj ponownie.")
        
        elif figura == "e":
            # Równoległobok
            a = wczytaj_liczbe("Podaj bok (a): ")
            h = wczytaj_liczbe("Podaj wysokość (h) do boku a: ")
            b = wczytaj_liczbe("Podaj drugi bok (b): ")
            pole = a * h
            obwod = 2 * (a + b)
            print(f"Pole równoległoboku = {pole:.2f}")
            print(f"Obwód równoległoboku = {obwod:.2f}")
            dodaj_do_historii(f"Równoległobok: a={a}, h={h}, b={b}, Pole={pole:.2f}, Obwód={obwod:.2f}")
            
        elif figura == "f":
            # Trapez
            a = wczytaj_liczbe("Podaj dłuższą podstawę (a): ")
            b = wczytaj_liczbe("Podaj krótszą podstawę (b): ")
            h = wczytaj_liczbe("Podaj wysokość (h): ")
            c = wczytaj_liczbe("Podaj bok (c): ")
            d = wczytaj_liczbe("Podaj bok (d): ")
            pole = ((a + b) * h) / 2
            obwod = a + b + c + d
            print(f"Pole trapezu = {pole:.2f}")
            print(f"Obwód trapezu = {obwod:.2f}")
            dodaj_do_historii(f"Trapez: a={a}, b={b}, h={h}, c={c}, d={d}, Pole={pole:.2f}, Obwód={obwod:.2f}")
            
        else:
            print("Nie ma takiej figury. Spróbuj ponownie.")
            
    except Exception as e:
        # Obsługa nieprzewidzianych błędów
        print(f"Wystąpił nieoczekiwany błąd: {e}")
    finally:
        input("\nNaciśnij Enter, aby wrócić do menu...")
        
def menu_bryl():
    """Menu do obliczania brył."""
    print("""
=== BRYŁY ===
a - Sześcian
b - Prostopadłościan
c - Walec
d - Kula
e - Stożek
""")
    bryla = input("Wybierz bryłę: ").lower()
    
    try:
        if bryla == "a":
            # Sześcian
            a = wczytaj_liczbe("Podaj bok (a): ")
            pole_powierzchni = 6 * a**2
            objetosc = a**3
            print(f"Pole powierzchni sześcianu = {pole_powierzchni:.2f}")
            print(f"Objętość sześcianu = {objetosc:.2f}")
            dodaj_do_historii(f"Sześcian: a={a}, Pole={pole_powierzchni:.2f}, Objętość={objetosc:.2f}")

        elif bryla == "b":
            # Prostopadłościan
            a = wczytaj_liczbe("Podaj bok (a): ")
            b = wczytaj_liczbe("Podaj bok (b): ")
            c = wczytaj_liczbe("Podaj bok (c): ")
            pole_powierzchni = 2 * (a * b + a * c + b * c)
            objetosc = a * b * c
            print(f"Pole powierzchni prostopadłościanu = {pole_powierzchni:.2f}")
            print(f"Objętość prostopadłościanu = {objetosc:.2f}")
            dodaj_do_historii(f"Prostopadłościan: a={a}, b={b}, c={c}, Pole={pole_powierzchni:.2f}, Objętość={objetosc:.2f}")

        elif bryla == "c":
            # Walec
            r = wczytaj_liczbe("Podaj promień podstawy (r): ")
            h = wczytaj_liczbe("Podaj wysokość (h): ")
            pole_powierzchni = 2 * math.pi * r * (r + h)
            objetosc = math.pi * r**2 * h
            print(f"Pole powierzchni walca = {pole_powierzchni:.2f}")
            print(f"Objętość walca = {objetosc:.2f}")
            dodaj_do_historii(f"Walec: r={r}, h={h}, Pole={pole_powierzchni:.2f}, Objętość={objetosc:.2f}")

        elif bryla == "d":
            # Kula
            r = wczytaj_liczbe("Podaj promień (r): ")
            pole_powierzchni = 4 * math.pi * r**2
            objetosc = (4/3) * math.pi * r**3
            print(f"Pole powierzchni kuli = {pole_powierzchni:.2f}")
            print(f"Objętość kuli = {objetosc:.2f}")
            dodaj_do_historii(f"Kula: r={r}, Pole={pole_powierzchni:.2f}, Objętość={objetosc:.2f}")

        elif bryla == "e":
            # Stożek
            r = wczytaj_liczbe("Podaj promień podstawy (r): ")
            h = wczytaj_liczbe("Podaj wysokość (h): ")
            # Długość tworzącej "l" obliczamy z twierdzenia Pitagorasa
            l = math.sqrt(r**2 + h**2)
            pole_powierzchni = math.pi * r * (r + l)
            objetosc = (1/3) * math.pi * r**2 * h
            print(f"Tworząca (l) = {l:.2f}")
            print(f"Pole powierzchni stożka = {pole_powierzchni:.2f}")
            print(f"Objętość stożka = {objetosc:.2f}")
            dodaj_do_historii(f"Stożek: r={r}, h={h}, l={l:.2f}, Pole={pole_powierzchni:.2f}, Objętość={objetosc:.2f}")

        else:
            print("Nie ma takiej bryły. Spróbuj ponownie.")
    
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
    finally:
        input("\nNaciśnij Enter, aby wrócić do menu...")

# To jest linijka, która uruchamia program, kiedy plik jest otwierany.
if __name__ == "__main__":
    kalkulator_geometrii()
