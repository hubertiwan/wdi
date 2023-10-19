#program wypisujacy podzielniki liczby

number=int(input("Podaj liczbe: "))

factors = []                            #utworzenie tablicy w ktorej beda przechowywane dzielniki 'number'
factors.append(1)                       #dodanie do tablicy dzielnika rownego 1

for i in range(2, int((number/2)+1)):#zakres od 2 do number/2 wlacznie, inkrementacja i o 1
    if number%i==0:                     #sprawdzenie czy liczba modulo 1 rowna sie 0 czy nie == czy liczba jest podzielna przez 1
        factors.append(i)

factors.append(number)                  #dodanie do tablicy dzielnika rownego wprowadzonej liczbie

print("Podzielniki liczby", number, ":", end=' ')
for x in factors:
    print(x, end=' ')

