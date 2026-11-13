#Zadanie 1 
name = input("Podaj nazwę produktu ")
price = float(input("Podaj cenę produktu "))
volume = int(input("Podaj liczbę sztuk "))
discount = input("Podaj kod promocyjny ")
fee = 0.5
final_price = price * volume + volume * fee
print(25*"=")
print(
    f"Produkt:  {name}",
    f"Sztuk: {volume}",
    f"Kod: {discount}",
    f"Cena do zapłaty: {final_price:.2f} zł",
    sep="|"
)
print(25*"=")

#Zadanie 2 
def koszt_wysylki(waga, ekspres=False):
    def cena_podstawowa():
        if waga <= 1:
            return 10 
        if waga <= 5:
            return 18 
        if waga <= 20:
            return 30 
        if waga > 20:
            return 50 
    koszt = cena_podstawowa()
    if ekspres:
        koszt = koszt + 15
    return koszt

print(koszt_wysylki(20, True))

#Zadanie 3
licznik = 0
def weryfikuj_pin(pin):
    global licznik
    licznik += 1
    def zawiera(znaki):
        for znak in znaki:
            if znak in pin:
                return True
        return False
    problems = []
    if len(pin) != 4:
        problems.append("Pin musi mie dokadnie 4 znaki")
    if not zawiera("0123456789"):
        problems.append("Brak cyfry")
    if zawiera("abc"):
        problems.append("Pin zawiera niedozwolone litery")
    return problems
print(weryfikuj_pin("1234"))    
print("Liczba prob:", licznik)

#Zadanie 4 
def podsumowanie_koszyka(klient, *produkty, rabat = 0, **opcje):
    print(f"Klient: {klient}")
    if produkty:
        print("Produkty: ", ", ".join(produkty))
    else:
        print("Produkty: Brak produktow")
    print(f"Rabat: {rabat}%")
    for klucz, wartosc in opcje.items():
        print(f"{klucz}: {wartosc}")
    print("-"*25)
print(podsumowanie_koszyka("Pawel", "Gry", "konsola", "pad", rabat=15, dostawa="kurier", opakowaanie="prezent"))

#Zadanie 5

def generuj_i_licz(n, a1 = 2, r = 3):
    ciag = []
    for i in range(n):
        ciag.append(a1 + r * i)
    min = ciag[0]
    max = ciag[0]
    suma = 0 
    for liczba in ciag:
        if liczba < min:
            min = liczba
        if liczba > max:
            max = liczba    
        suma = suma + liczba
    srednia = suma / len(ciag)
    return "Ciag:", ciag, "Max:", max, "Min: ", min, "Avg: ", srednia
print(generuj_i_licz(5))

#Zadanie 6
tekst = "   aNNa   nowAK-kowalska  2004  "
zamiana = tekst.replace("-", " ")
czysty_tekst = "_".join(zamiana.strip().split())
print(czysty_tekst.lower())
slowka = []
for slowa in zamiana.split():
    slowka.append(slowa)
ostatni_czlon = slowka[-1]
if ostatni_czlon.isdigit():
    print("Ostatni człon składa się wyłącznie z cyfr ")
else:
    print("Ostatni człon nie składa się wyłacznie z cyfr")
litery = []
liczba_a = tekst.lower().count("a")
print(liczba_a)

#Zadanie 7 
sklep = {"Majtki": 10, "Koszulka": 12, "Czapka": 9}
sklep.update({"Majtki": 5, "Skarpety": 3})
sklep.pop("Koszulka")
print(f"Dostępne produkty:  {sklep} Ilość produktów: {len(sklep)}")
u = input("Podaj nazwe produktu").strip().capitalize()
i = int(input("Podaj ilość"))
cena = i * sklep.get(u,0)
print(cena)

#Zadanie 8 
a = float(input('Podaj liczbę rzeczysiwtą'))
b = float(input('Podaj liczbę rzeczysiwtą'))
c = float(input('Podaj liczbę rzeczysiwtą'))

if a > 0 and b > 0 and c > 0 and a+b > c and a+c > b and c+b > a:
    print("wszystkie długości są prawidłowe i da się zbudowac z nich trojkt")
    if a == b == c:
        print("Trójkat jest równoboczny")
    elif a == b or b == c or a == c:
        print("tórjkat jest równoramienny")
    else:
        print("trójkąt jest róznoboczny i nie jest prostokatny")
    if round(a**2+ b**2,9) == round(c**2,) or b**2 +c**2 == a**2 or a**2 + c**2 == b**2:
        print("Trojkąt jest prostokatny")
    else:
        print("trójkąt jest róznoboczny i nie jest prostokatny")
else:
    if a != 0:
        delta = b**2 - 4 * a * c
        if delta > 0:
            x1 = (-b-delta**0.5)/(2*a)
            x2 = (-b+delta**0.5)/(2*a)
            print("Rozwiązania: ", x1 , x2)
        if delta == 0:
            x = -b/(2*a)
            print("Rozwiązanie: ", x)
        if delta < 0:
            print("Brak rozwiazan")
    else:
        print("Nie jest to równanie kwadartowe")

#Zadanie 9
zbior =[]
while True:
    u = input("Podaj liczbę lub wpisz stop")
    if u == "stop":
        break
    liczba = int(u)
    if liczba < 0 and liczba % 2 != 0:
        continue
    zbior.append(liczba)
if zbior:
    print(zbior, sum(zbior), max(zbior), min(zbior))
else:
    print("Nie podano kryteriów")

#Zadanie 10
liczba = int(input("Podaj liczbe:"))
while liczba < 0:
    liczba =int(input("Podaj poprawną liczbę"))

if liczba == 0:
    wynik = "0"
else:
    reszty = []
    zadaniowa = liczba
    while zadaniowa > 0:
        reszty.append(str(zadaniowa % 8))
        zadaniowa = zadaniowa // 8
    reszty.reverse()
    wynik = "".join(reszty)
    #osemkowy = "".join(map(str,reversed(reszty)))
if format(liczba, 'o') == wynik:
    print("wyniki są zgodne")
else: 
    print("wyniki nie są zgodne")

#Zadanie 11
def czy_pierwsza(n):
    if n < 2:
        False
    for dzielniki in range(2,n):
        if n % dzielniki == 0:
            print("n nie jest liczbą pierwszą")
        else:
            print("Liczba jest pierwszą")
def rozdziel_liczby(lista):
    pierwsza = []
    pozostałe = []
    for liczba in lista:
        if czy_pierwsza(liczba):
            pierwsza.append(liczba)
        else:
            pozostałe.append(liczba)
    return pierwsza, pozostałe



    