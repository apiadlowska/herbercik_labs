class IdealPerson:
    def __init__(self, name, gender, traits):
        self.name = name
        self.gender = gender
        self.traits = traits  # słownik cech i ocen

    def introduce(self, lang):
        # Wyświetlanie tylko imienia i cech
        if lang == "PL":
            print(f"\n{self.name}:")
            for trait, value in self.traits.items():
                print(f"{trait.capitalize()}: {value}/10 ({value*10:.0f}%)")
        else:
            print(f"\n{self.name}:")
            for trait, value in self.traits.items():
                print(f"{trait.capitalize()}: {value}/10 ({value*10:.0f}%)")

    def how_ideal(self, lang):
        total = sum(self.traits.values())
        max_total = len(self.traits) * 10
        percent = (total / max_total) * 100
        if lang == "PL":
            print(f"\nŁączna doskonałość: {percent:.2f}%")
        else:
            print(f"\nTotal idealness: {percent:.2f}%")

    @staticmethod
    def ask_traits(lang):
        if lang == "PL":
            name = input("Jak masz na imię?")
            gender = input("Wybierz płeć (K/M/Inna): ")
            if gender.lower() in ["k"]:
                print("Odpowiadaj o jej cechach.")
            else:
                print("Odpowiadaj o jego cechach.")
            traits = {}
            traits["humor"] = int(input("Poczucie humoru (1-10): "))
            traits["inteligencja"] = int(input("Inteligencja (1-10): "))
            traits["troskliwość"] = int(input("Troskliwość (1-10): "))
            traits["wygląd"] = int(input("Wygląd (1-10): "))
            traits["empatia"] = int(input("Empatia (1-10): "))
            traits["pasje"] = int(input("Pasje/zaradność (1-10): "))
            traits["uprzejmość"] = int(input("Uprzejmość (1-10): "))
        else:
            name = input("what is your name? ")
            gender = input("Choose gender (F/M/Other): ")
            if gender.lower() in ["f", "female"]:
                print("Answer about her traits.")
            else:
                print("Answer about his traits.")
            traits = {}
            traits["humor"] = int(input("Humor (1-10): "))
            traits["intelligence"] = int(input("Intelligence (1-10): "))
            traits["caring"] = int(input("Caring (1-10): "))
            traits["looks"] = int(input("Looks (1-10): "))
            traits["empathy"] = int(input("Empathy (1-10): "))
            traits["hobbies"] = int(input("Hobbies/skills (1-10): "))
            traits["kindness"] = int(input("Kindness (1-10): "))
        return IdealPerson(name, gender, traits)

# Wybór języka
lang = input("Wybierz język / Choose language (PL/EN): ").upper()
while lang not in ["PL", "EN"]:
    lang = input("Proszę wybrać poprawny język / Please choose a valid language (PL/EN): ").upper()

# Tworzenie osoby
person = IdealPerson.ask_traits(lang)
person.introduce(lang)
person.how_ideal(lang)
