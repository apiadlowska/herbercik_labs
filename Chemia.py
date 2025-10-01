import random

# pytania z odpowiedziami
pytania = [
    {
        "pytanie": "Która liczba atomowa odpowiada tlenowi?",
        "odpowiedzi": ["6", "7", "8", "16"],
        "poprawna": "8"
    },
    {
        "pytanie": "Które cząstki znajdują się w jądrze atomowym?",
        "odpowiedzi": ["Protony i neutrony", "Elektrony", "Protony i elektrony", "Tylko neutrony"],
        "poprawna": "Protony i neutrony"
    },
    {
        "pytanie": "Izotopy różnią się liczbą...",
        "odpowiedzi": ["Protonów", "Neutronów", "Elektronów", "Powłok"],
        "poprawna": "Neutronów"
    },
    {
        "pytanie": "Masa cząsteczkowa wody H2O wynosi około:",
        "odpowiedzi": ["16", "18", "20", "44"],
        "poprawna": "18"
    },
    {
        "pytanie": "Atom sodu Na ma Z=11. Ile elektronów ma jon Na+?",
        "odpowiedzi": ["11", "12", "10", "9"],
        "poprawna": "10"
    }
]

def quiz():
    punkty = 0
    losowe_pytania = random.sample(pytania, len(pytania))  # losowa kolejność
    
    for p in losowe_pytania:
        print("\n" + p["pytanie"])
        for i, odp in enumerate(p["odpowiedzi"], start=1):
            print(f"{i}. {odp}")
        
        wybor = input("Wybierz odpowiedź (1-4): ")
        
        if wybor.isdigit() and 1 <= int(wybor) <= 4:
            if p["odpowiedzi"][int(wybor)-1] == p["poprawna"]:
                print("✅ Dobrze!")
                punkty += 1
            else:
                print(f"❌ Źle! Poprawna odpowiedź to: {p['poprawna']}")
        else:
            print("⚠️ Nieprawidłowy wybór.")
    
    print(f"\nTwój wynik: {punkty}/{len(pytania)} punktów.")

# uruchomienie quizu
if __name__ == "__main__":
    print("🔬 Quiz z chemii: Budowa atomu i podstawy")
    quiz()
