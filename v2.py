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

# --- TRÓJKĄT ---
elif wybor == '4':
    # Pytamy o boki trójkąta
    bok_a = float(input("Podaj długość boku A: "))
    bok_b = float(input("Podaj długość boku B: "))
    bok_c = float(input("Podaj długość boku C: "))

    # Obliczamy obwód
    obwod = bok_a + bok_b + bok_c

    # Sprawdzamy, czy można zbudować trójkąt
    if bok_a + bok_b > bok_c and bok_a + bok_c > bok_b and bok_b + bok_c > bok_a:
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
        print("Z podanych długości nie da się zbudować trójkąta.")

# --- BŁĄD WPISYWANIA ---
else:
    print("Nieprawidłowy wybór. Uruchom program ponownie i wpisz numer od 1 do 4.")