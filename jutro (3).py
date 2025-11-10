# --- KALKULATOR POLA I OBWODU FIGUR ---
while True:
    print("\n--- Nowe obliczenia ---")
    print("Wybierz figurę, której pole i obwód chcesz obliczyć:")
    print("1. Koło")
    print("2. Kwadrat")
    print("3. Prostokąt")
    print("4. Trójkąt")

    wybor = input("Wpisz numer figury (1/2/3/4): ")

    # --- KOŁO ---
    if wybor == '1':
        try:
            promien = float(input("Podaj promień koła: "))
            pi = 3.14  # Uproszczona wartość liczby pi
            pole = pi * promien * promien
            obwod = 2 * pi * promien
            
            print("--- Wyniki ---")
            print("Pole koła wynosi:", pole)
            print("Obwód koła wynosi:", obwod)
        except ValueError:
            print("Nieprawidłowe dane. Podaj liczbę.")

    # --- KWADRAT ---
    elif wybor == '2':
        try:
            bok = float(input("Podaj długość boku kwadratu: "))
            pole = bok * bok
            obwod = 4 * bok
            
            print("--- Wyniki ---")
            print("Pole kwadratu wynosi:", pole)
            print("Obwód kwadratu wynosi:", obwod)
        except ValueError:
            print("Nieprawidłowe dane. Podaj liczbę.")

    # --- PROSTOKĄT ---
    elif wybor == '3':
        try:
            bok1 = float(input("Podaj długość pierwszego boku prostokąta: "))
            bok2 = float(input("Podaj długość drugiego boku prostokąta: "))
            pole = bok1 * bok2
            obwod = 2 * (bok1 + bok2)
            
            print("--- Wyniki ---")
            print("Pole prostokąta wynosi:", pole)
            print("Obwód prostokąta wynosi:", obwod)
        except ValueError:
            print("Nieprawidłowe dane. Podaj liczby.")

    # --- TRÓJKĄT (z pętlą do walidacji) ---
    elif wybor == '4':
        mozna_zbudowac_trojkat = False
        while not mozna_zbudowac_trojkat:
            try:
                bok_a = float(input("Podaj długość boku A: "))
                bok_b = float(input("Podaj długość boku B: "))
                bok_c = float(input("Podaj długość boku C: "))
                
                if bok_a + bok_b > bok_c and bok_a + bok_c > bok_b and bok_b + bok_c > bok_a:
                    mozna_zbudowac_trojkat = True
                    
                    obwod = bok_a + bok_b + bok_c
                    s = obwod / 2
                    pole = (s * (s - bok_a) * (s - bok_b) * (s - bok_c)) ** 0.5
                    
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
                    print("Z podanych długości nie da się zbudować trójkąta. Spróbuj ponownie.")
            except ValueError:
                print("Nieprawidłowe dane. Podaj liczby. Spróbuj ponownie.")

    # --- BŁĄD WPISYWANIA ---
    else:
        print("Nieprawidłowy wybór. Wpisz numer od 1 do 4.")
    
    # Pytanie o kontynuację
    odpowiedz = input("\nCzy chcesz wykonać kolejne obliczenia? (tak/nie): ").lower()
    if odpowiedz != 'tak':
        print("Dziękuję za skorzystanie z kalkulatora. Do widzenia!")
        break # Zakończenie pętli głównej i programu