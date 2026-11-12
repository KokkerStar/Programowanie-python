#Zadanie 1 
a = int(input("Podaj czesc rzeczywista " ))
c = int(input("Podaj czesc rzeczywista " ))
b = int(input("Podaj czesc utojona " ))
d = int(input("Podaj czesc urojona " ))
z1 = complex(a, b)
z2 = complex(c, d)
wynik1 = z1 + z2
wynik2 = abs(z1)
wynik3 = z1.conjugate()
wynik4 = z1**2
print(f"Suma dwoch liczb zespolonych wynosi: {format(wynik1, '.2f').replace("j", "i)" )})")
print(f" modul liczby zespolonej wynosi: {format(wynik2, '.2f').replace("j", "i)" )}")
print(f"sprzezenie liczby zespolonejwynosi: {format(wynik3, '.2f').replace("j", "i)" )}")
print(f"kwadrat liczby zespolonej wynosi: {format(wynik4, '.2f').replace("j", "i)" )}")

#Zadanie 2 
liczba = int(input("Podaj liczbe:"))
reszty = []
if 0 < liczba < 16:
    zadaniowa = liczba
    for i in range(4):
        reszty.append(zadaniowa % 2)
        zadaniowa = zadaniowa // 2
else:
    print("Liczba nie miesci sie w przedziale 0-15")
#reszty.reverse()
print(reszty[::-1])
print(bin(liczba).replace("0b",""))

#Zadanie 3, 4
import turtle

kod = input("Podaj kod koloru w formacie #RRGGBB: ")
kod2 = input("Podaj kod koloru w formacie #RRGGBB: ")
Size = input("Podaj rozmiar czcionki ")
R = kod[1:3]
G = kod[3:5]
B = kod[5:7]
R2 = kod2[1:3]
G2 = kod2[3:5]
B2 = kod2[5:7]
print(f"RGB({int(R, 16)}, {int(G, 16)}, {int(B, 16)})")
turtle.colormode(255) 
turtle.bgcolor(int(R,16), int(G, 16) , int(B, 16))
turtle.pencolor(int(R2, 16), int(G2, 16), int(B2, 16))
turtle.write("Krowa", font=("Arial", int(Size)))
turtle.done()

#Zadanie 5
v = 3e5
t = 365 * 24 *60 * 60
s = v * t
og = float(input("Podaj odleglosc do gwiazdy w latach swietlnych:"))
ogkm = og * s
vs = 6.1e4
t2 = ogkm / vs 
dni = t2 // 24
lata = dni // 365
pozostale = dni % 365
print(f"Odleglosc do gwiazd: {ogkm:.2e} km")
print(f"Czas lotu sondy: {t2:.2e} h, czyli {lata} lat i {pozostale} dni")

#Zadanie 6 
cennik = {"Czarna": 12, "Biała": 14, "Latte": 16}
cennik.update({"Espresso": 10, "Czarna": 13})
cennik.pop("Biała")
print("Dostępne rodzaje kawy:", cennik, "Liczba dostępnych kaw: ", len(cennik))
rodzaj = input("Jaka kawe chcesz zamowic? ")
liczba = int(input("Ile sztuk dla pana bedzie? "))
cena = cennik.get(rodzaj, 0)
koszt = cena * liczba
print(f"Kwota do zaplaty: {koszt} zl")

#Zadanie 7
dane = input("Podaj imie i nazwisko: ")
czyste_dane = " ".join(dane.split())
print("Uporządkowane dane:", czyste_dane.upper())
login = ".".join(dane.split()).lower()
print("Login:", login)
email = input("Podaj adres email: ")
liczba_malpek = email.count("@")
if liczba_malpek == 1:
    print("Adres ma: ", liczba_malpek, "znaków @")
else:
    print("Adres jest nieprawidłowy i ma :", liczba_malpek,"znaków @")
numer = input("Podaj numer telefonu")
czysty_numer = "".join(znak for znak in numer if znak.isdigit())
if czysty_numer.isdigit():
    print("Po oczyszczeniu zostały same cyfry", czysty_numer)
else:
    print("Nie podano żadnych cyfr")