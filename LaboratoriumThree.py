#Zadanie 1
liczba = int(input("Podaj liczbę całkowitą: "))
if liczba % 2 ==0:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")
if liczba > 0:
    print("Liczba jest dodatnia")
elif liczba < 0:
    print("Liczba jest ujemna")
else:
    print('Liczba jest równa 0')

#Zadanie 2
a = int(input("Podaj pierwsza długość trójkąta"))
b = int(input("Podaj druga długość trójkąta"))
c = int(input("Podaj trzecia długość trójkąta"))
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Z podanych długości da sie zbudować trójkąt")
    if a == b == c:
        print("Trójkąt jest równoboczny")
    elif a == b or b == c or c == a:
        print("Trójkąt jest równoramienny")
    else:
        print("Trójkąt jest różnoboczny")
else:
    print("Z podanych długości nie da sie zbudować trójkąta")

#Zadanie 3
a = int(input("Podaj współcznnik a"))
b = int(input("Podaj współcznnik b"))
c = int(input("Podaj współcznnik c"))
if a == 0:
    print("Równanie nie jest kwadratowe")
else:
    d = b**2 - (4 * a * c)

    if d > 0:
        liczba1 = (-b - (d**0.5))/2*a
        liczba2 = (-b + (d**0.5))/2*a
        print("Rozwiazaniami są: ", liczba1, liczba2)
    elif d == 0:
        liczba = -b/2*a
        print("Rozwiązaniem jest: ", liczba)
    else:
        print("Równanie nie ma rozwiązań rzeczywistych")

#Zadanie 4
lista = []
while True:
    tekst = input("Podaj liczbę lub wpisz 'koniec', aby zakończyć: ")
    if tekst == "koniec":
        break
    lista.append(int(tekst))
print(f"Liczby: {len(lista)} Suma: {sum(lista)} Średnia: {(sum(lista)/ (len(lista)))} Minimum: {min(lista)} Maliczbaimum: {max(lista)}")

#Zadanie 5 
n = int(input('Podaj liczbę n '))
for liczba in range(1, n + 1):
    for y in range(1, n + 1):
        print(liczba * y,end="\t")
    print()
#Zadanie 6 
slowo = input("Podaj słowo")
samogloski = set('aąeęioóuy')
spolgloski = set('bcdcćdfghjklłmnńprstvwliczbazźż')
samo_licznik = []
for znak in slowo.lower():
    if znak in samogloski:
        samo_licznik.append(1)
print(sum(samo_licznik))
spol_licznik = []
for znak in slowo.lower():
    if znak in spolgloski:
        spol_licznik.append(1)
print(sum(spol_licznik))
bez_samoglosek = ""
for litera in slowo.lower():
    if litera.lower() not in samogloski:
        bez_samoglosek += litera
print("Słowo bez samogłosek: ", bez_samoglosek)

#Zadanie 7 
liczba = int(input("Podaj liczbę nieujemną: "))
if liczba < 0:
    print("Podana liczba jest ujemna popraw to ")
else:
    robocza = liczba
    reszta= []
    if robocza == 0:
        reszta.append(0)
    else:
        while robocza > 0:
            reszta.append(robocza % 2)
            robocza = robocza // 2
    print("Liczba w systemie dwojkowym: ", reszta[::-1])
binarna = "".join(map(str, reversed(reszta)))
if format(liczba, "b") == binarna:
    print("Wyniki są zgodne")
else:
    print("Wyniki nie sa zgodne")

#Zadanie 8 
def czy_parzysta(n):
    if n % 2 == 0:
        return True
    return False
parzyste = []
for i in range(1,21):
    if czy_parzysta(i) == True:
        parzyste.append(i)
print(parzyste)

#Zadanie 9 
def na_farenheity(c):
    Faren = 1.8 * c + 32
    return Faren
for i in range(-20,40,10):
    print(f"{i}\t {na_farenheity(i)}")

#Zadanie 10
def czy_pierwsza(n):
    if n < 2:
        return False
    for dzielnik in range(2,n):
        if n % dzielnik == 0:
            return False
    return True
liczba = int(input("Podaj liczbę: "))
if czy_pierwsza(liczba):
    print("Liczba jest pierwsza")
else:
    print("Liczba nie jest pierwsza")

#Zadanie 11
def ramka(tekst):
    szerokosc = len(tekst) + 4
    print("*" * szerokosc)
    print("* " + tekst + " *")
    print("*" * szerokosc)
print(ramka("Python! Jest super!"))

#Zadanie 12 
lista =[1,2,3,4,5,7,8,9]
def podziel_liste(jakas_lista):
    parzyste = []
    nieparzyste = []
    for cyfry in jakas_lista:
        if cyfry % 2 == 0:
            parzyste.append(cyfry)
        else:
            nieparzyste.append(cyfry)
    return parzyste, nieparzyste
parzyste, nieparzyste = podziel_liste(lista)
print("Parzyste: ", parzyste, "długość: ", len(parzyste))
print("Nieparzyste: ", nieparzyste, "długość: ", len(nieparzyste))

#Zadanie 13
def szyfruj(tekst, przesuniecie):
    wynik = ""
    for znak in tekst:
        if "a" <= znak <= "z":
            pozycja = ord(znak) - ord("a")
            nowa_pozycja = (pozycja + przesuniecie) % 26
            nowy_znak = chr(nowa_pozycja + ord("a"))
            wynik = wynik + nowy_znak
        else:
            wynik = wynik + znak
    return wynik
szyfrogram = szyfruj("xyz, abc!", 3)
odszyfrowany = szyfruj(szyfrogram, -3)
print(szyfrogram, end="\n")
print(odszyfrowany)

#Zadanie 14
def liczb_slowa(tekst):
    slownik = {}
    for slowo in tekst.lower().split():
        slownik[slowo] = slownik.get(slowo, 0) + 1
    return slownik
def najczestsze(slownik):
    if not slownik:
        return None
    return max(slownik, key = slownik.get)
slownik = liczb_slowa("Ala ma kota a Ala Ala ma psa")
print(slownik)
print(najczestsze(slownik))