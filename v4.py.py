# --- KALKULATOR POLA I OBWODU FIGUR ---

print("Wybierz figurę, której pole i obwód chcesz obliczyć:")
print("1. Koło")
print("2. Kwadrat")
print("3. Prostokąt")
print("4. Trójkąt")

wybor = input("Wpisz numer figury (1/2/3/4): ")

# --- KOŁO ---
if wybor == '1':
    # Pytamy użytkownika o promień
    promien = float(input("Podaj promień koła: "))
    
    # Obliczamy pole
    pi = 3.14  # Uproszczona wartość liczby pi
    pole = pi * promien * promien
    
    # Obliczamy obwód
    obwod = 2 * pi * promien
    
    print("--- Wyniki ---")
    print("Pole koła wynosi:", pole)
    print("Obwód koła wynosi:", obwod)

# --- KWADRAT ---
elif wybor == '2':
    # Pytamy użytkownika o długość boku
    bok = float(input("Podaj długość boku kwadratu: "))
    
    # Obliczamy pole
    pole = bok * bok
    
    # Obliczamy obwód
    obwod = 4 * bok
    
    print("--- Wyniki ---")
    print("Pole kwadratu wynosi:", pole)
    print("Obwód kwadratu wynosi:", obwod)

# --- PROSTOKĄT ---
elif wybor == '3':
    # Pytamy o boki
    bok1 = float(input("Podaj długość pierwszego boku prostokąta: "))
    bok2 = float(input("Podaj długość drugiego boku prostokąta: "))
    
    # Obliczamy pole
    pole = bok1 * bok2
    
    # Obliczamy obwód
    obwod = 2 * (bok1 + bok2)
    
    print("--- Wyniki ---")
    print("Pole prostokąta wynosi:", pole)
    print("Obwód prostokąta wynosi:", obwod)

# --- TRÓJKĄT (z pętlą do walidacji) ---
elif wybor == '4':
    # Zmienna sterująca pętlą
    mozna_zbudowac_trojkat = False
    
    # Pętla będzie się wykonywać dopóki nie uda się zbudować trójkąta
    while not mozna_zbudowac_trojkat:
        # Pytamy o boki trójkąta
        try:
            bok_a = float(input("Podaj długość boku A: "))
            bok_b = float(input("Podaj długość boku B: "))
            bok_c = float(input("Podaj długość boku C: "))
            
            # Warunek trójkąta: suma długości dwóch krótszych boków musi być większa niż długość boku najdłuższego
            if bok_a + bok_b > bok_c and bok_a + bok_c > bok_b and bok_b + bok_c > bok_a:
                # Jeśli warunek jest spełniony, ustawiamy zmienną na True, co zakończy pętlę
                mozna_zbudowac_trojkat = True
                
                # Obliczamy obwód
                obwod = bok_a + bok_b + bok_c

                # Obliczamy pole trójkąta (wzór Herona)
                s = obwod / 2  # Półobwód
                pole = (s * (s - bok_a) * (s - bok_b) * (s - bok_c)) ** 0.5
                
                # Określenie rodzaju trójkąta (na podstawie boków)
                if bok_a == bok_b and bok_b == bok_c:
                    rodzaj = "równoboczny"
                elif bok_a == bok_b or bok_a == bok_c or bok_b == bok_c:
                    rodzaj = "równoramienny"
                else:
                    rodzaj = "różnoboczny"

                print("--- Wyniki ---")
                print("Obwód trójkąta wynosi:", obwod)
                print("Pole trójkąta wynosi:", pole)
                print("Jest to trójkąt:", rodzaj)
            else:
                # Jeśli warunek nie jest spełniony, informujemy użytkownika i pętla zaczyna się od nowa
                print("Z podanych długości nie da się zbudować trójkąta. Spróbuj ponownie.")
        except ValueError:
            # Obsługa błędu, jeśli użytkownik wpisze tekst zamiast liczby
            print("Nieprawidłowe dane. Podaj liczby. Spróbuj ponownie.")

# --- BŁĄD WPISYWANIA ---
else:
    print("Nieprawidłowy wybór. Uruchom program ponownie i wpisz numer od 1 do 4.")