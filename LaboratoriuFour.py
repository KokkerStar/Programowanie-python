#Zadanie 1 
def trojkat(wysokosc, znak="*"):
    for i in range(1, wysokosc + 1):
        print(i * znak)
trojkat(10)

#Zadanie 2
def ocena(punkty):
    if punkty < 0 or punkty > 100:
        return "Nieprawidłowa liczba punktów"
    if punkty <= 40:
        return "Ocena 2.0"
    if punkty <= 55:
        return "Ocena 3.0"
    if punkty <= 70:
        return "Ocena 3.5"
    if punkty <= 80:
        return "Ocena 4.0"
    if punkty <= 90:
        return "Ocena 4.5"
    return "Ocena 5.0"
print(ocena(60))

#Zadanie 3 
def ciag(n, a1 = 1, r = 1):
    lista = []
    for i in range(n):
        lista.append(a1+i*r)
    return lista
print(ciag(5))
print(ciag(5,1,2))
print(ciag(5,2,2))
print(ciag(4,10,-3))

#Zadanie 4
sprzedane = 0
def latte():
    global sprzedane
    print("Podano latte")
    sprzedane += 1
def expresso():
    global sprzedane
    print("Podano expresso")
    sprzedane += 1
def podsumowanie():
    print(f"Sprzedane kawy: {sprzedane}")
latte()
expresso()
podsumowanie()

#Zadanie 5 
def sprawdz_haslo(haslo):
    def zawiera(znaki):
        for znak in znaki:
            if znak in haslo:
                return True
        return False
    poprawne = True
    if len(haslo) < 8:
        print("Hasło musi zawierać min 8 znaków")
        poprawne = False
    if not zawiera("QWERTYUIOPASDFGHJKLZXCVBNM"):
        print("Hasło musi zawierać dużą literę")
        poprawne = False
    if not zawiera("1234567890"):
        print("Hasło musi zawierać cyfrę")
        poprawne = False
    if not zawiera("!@#$%^&*"):
        print("Hasło musi zawierać znak specjalny")
        poprawne = False
    if poprawne:
        return "Hasło jest poprawne"
    return "Hasło nie spełnia wymagań"
print(sprawdz_haslo("Malykotbi90ay&"))

#Zadanie 6 
def zamowienie(*kawy, **uwagi):
    print("Kawy:", ", ".join(kawy) if kawy else "brak")
    if uwagi:
        print("Uwagi:")
        for nazwa, wartosc in uwagi.items():
            print(f"- {nazwa}: {wartosc}")
zamowienie("Czarna", "Biała", "Espresso",mleko="owsiane", cukier="bez cukru")

#Zadanie 7

def statystyki(lista):
    if not lista:
        raise ValueError("Lista nie może być pusta")
    minimum = lista[0]
    maksimum = lista[0]
    suma = 0
    for liczba in lista:
        if liczba < minimum:
            minimum = liczba
        if liczba > maksimum:
            maksimum = liczba
        suma += liczba
    srednia = suma / len(lista)
    return maksimum, minimum, srednia
najmniejsza, najwieksza, srednia = statystyki([4, -2, 10, 7])
print(f"Najmniejsza: {najmniejsza}, największa: {najwieksza}, średnia: {srednia}")

    