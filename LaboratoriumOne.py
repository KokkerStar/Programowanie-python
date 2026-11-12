#Zadanie 1 
print("Kawa czy herbata?")

#Zadanie 2.1, 2.2
pytanie1 = input("Jakie preferujesz rodzaj kawy? ")
pytanie2 = input("Iloma łyżkyżeczkami cukru słodzisz kawę? ")
print("Preferują kawę ", pytanie1, end="\n\n\n")                #Im więcej \n tym większy odstęp między wierszami
print("i słodzą ją ", pytanie2, "łyżeczkami cukru.",end="\n")

#Zadanie 3.1, 3.2
print(pytanie1, pytanie2, sep="+")
print(pytanie1.strip(), "+", pytanie2.strip(), sep="")

#Zadanie 4.1, 4.2
zamowienie = int(input("Ile chce pan zamowic kawy? "))
cena_kawy = 12
cena_koncowa = cena_kawy * zamowienie
print(f"Za {zamowienie} kawy zaplaci pan {cena_koncowa} zlotych ")

#Zadanie 5
zamowienie = int(input("Ile chce pan zamowic kawy? "))
napiwek = float(input("Ile chce pan zasoawic napiwku?"))
cena_kawy = 12
cena_kaucji = 0.25
cena_koncowa = cena_kawy * zamowienie + cena_kaucji * zamowienie + abs(napiwek)
print(f"Za {zamowienie} kawy zaplaci pan {cena_koncowa:.2f} zlotych ")

#Zadanie 6 
print(20*"*")
print(5*" ","Rachunek")
print(20*"*")
print(f"Liczba kaw: {zamowienie}")
print(f"Cena jednej kawy: {cena_kawy:.2f} zlotych")
print(f"Koszt kaw: {cena_kawy * zamowienie:.2f} zlotych")
print(f"Opata SUP: {cena_kaucji * zamowienie:.2f} zlotych")
print(f"Napiwek: {abs(napiwek):.2f} zlotych")
print(20*"*")
print(f"Do zapaty: {cena_koncowa:.2f} zlotych")
print(20*"*")'''

'''#Zadanie 7
Dzien = input("Podaj dzien: ")
Miesiac = input("Podaj miesiac: ")
Rok = input("Podaj rok: ")
print(Dzien, Miesiac, Rok, sep=".")

#Zadanie 8
print("Czekaj", end="...") 
print("Gotowe!")

#Zadanie 9 
minuty = int(input("Podaj liczbe minut: "))
godziny = minuty // 60
print(f"{minuty} minut to {godziny} godzina i {minuty % 60} minut"  )

#Zadanie 10 
Numer_pietra = int(input(("Podaj numer pietra: ")))
parter = 0
print(f"Liczba pieter dzielacych od parteru wynosi: {abs(Numer_pietra) - parter}")