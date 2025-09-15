# Triangle information calculator
import math

def _is_valid_triangle(a, b, c):
	"""
	Sprawdza, czy z boków o długościach a, b, c można zbudować trójkąt.
	Zwraca True jeśli tak, False w przeciwnym wypadku.
	"""
	return a + b > c and a + c > b and b + c > a

def _triangle_perimeter(a, b, c):
	"""
	Oblicza obwód trójkąta o bokach a, b, c.
	"""
	return a + b + c

def _triangle_area(a, b, c):
	"""
	Oblicza pole trójkąta o bokach a, b, c za pomocą wzoru Herona.
	"""
	s = (a + b + c) / 2
	return math.sqrt(s * (s - a) * (s - b) * (s - c))

def _triangle_type(a, b, c):
	"""
	Określa typ trójkąta na podstawie długości boków.
	Zwraca: 'równoboczny', 'równoramienny' lub 'różnoboczny'.
	"""
	if a == b == c:
		return "równoboczny"
	elif a == b or b == c or a == c:
		return "równoramienny"
	else:
		return "różnoboczny"

def main():
	"""
	Główna funkcja programu. Pobiera dane od użytkownika, oblicza i wyświetla informacje o trójkącie.
	"""
	print("Kalkulator trójkąta - podaj długości boków:")

	try:
		a = float(input("Podaj długość boku a: "))
		b = float(input("Podaj długość boku b: "))
		c = float(input("Podaj długość boku c: "))
	except ValueError:
		print("Błąd: Wprowadź poprawne liczby.")
		return

	if a <= 0 or b <= 0 or c <= 0:
		print("Błąd: Wszystkie długości boków muszą być większe od zera.")
		return

	if not _is_valid_triangle(a, b, c):
		print("Podane długości nie tworzą trójkąta.")
		return

	obwod = _triangle_perimeter(a, b, c)
	pole = _triangle_area(a, b, c)
	typ = _triangle_type(a, b, c)

	print(f"Obwód trójkąta: {obwod}")
	print(f"Pole trójkąta: {pole}")
	print(f"Typ trójkąta: {typ}")

if __name__ == "__main__":
	main()

