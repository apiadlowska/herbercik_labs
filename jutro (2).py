import math

def okresl_typ_trojkata(a, b, c):
    """Określa rodzaj trójkąta na podstawie długości jego boków."""
    if a + b <= c or a + c <= b or b + c <= a:
        return "Nie da się zbudować trójkąta z podanych boków."

    # Określenie rodzaju na podstawie boków
    if a == b and b == c:
        typ_bokow = "równoboczny"
    elif a == b or a == c or b == c:
        typ_bokow = "równoramienny"
    else:
        typ_bokow = "różnoboczny"

    # Sortowanie boków, żeby łatwiej określić typ kątów (c^2 vs a^2 + b^2)
    boki = sorted([a, b, c])
    a_sq, b_sq, c_sq = boki[0]**2, boki[1]**2, boki[2]**2

    # Określenie rodzaju na podstawie kątów (twierdzenie Pitagorasa)
    if abs(c_sq - (a_sq + b_sq)) < 1e-9: # Sprawdzanie z tolerancją dla liczb zmiennoprzecinkowych
        typ_katow = "prostokątny"
    elif c_sq > a_sq + b_sq:
        typ_katow = "rozwartokątny"
    else:
        typ_katow = "ostrokatny"

    return f"{typ_bokow} i {typ_katow}"

def oblicz_pole_i_obwod_trojkata(a, b, c):
    """
    Oblicza pole  i obwód trójkąta.
    Zwraca krotkę (pole, obwod).
    """
    if a + b <= c or a + c <= b or b + c <= a:
        return None, None # Zwraca None, jeśli nie da się zbudować trójkąta

    # Obwód
    obwod = a + b + c

    # Pole 
    s = obwod / 2
    pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return pole, obwod

print("Witaj w kalkulatorze trójkąta!")

try:
    a = float(input("Podaj długość pierwszego boku (a): "))
    b = float(input("Podaj długość drugiego boku (b): "))
    c = float(input("Podaj długość trzeciego boku (c): "))

    pole, obwod = oblicz_pole_i_obwod_trojkata(a, b, c)

    if pole is None:
        print("Z podanych długości boków nie da się zbudować trójkąta. Suma dwóch krótszych boków musi być większa niż najdłuższy bok.")
    else:
        typ_trojkata = okresl_typ_trojkata(a, b, c)
        print(f"\nObwód trójkąta wynosi: {obwod:.2f}")
        print(f"Pole powierzchni trójkąta wynosi: {pole:.2f}")
        print(f"Jest to trójkąt {typ_trojkata}.")

except ValueError:
    print("Nieprawidłowe dane. Upewnij się, że podajesz liczby.")