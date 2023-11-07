#program wypisujacy silnie liczb z zakresu od 1 do M, gdzie M jest liczba podana przez uzytkownika

import os

def FactorialN(endOfRangeF):
    factorials = []
    for i in range(1, endOfRangeF + 1):# liczby od 1 do konca zakresu podanego przez uzytkownika
        factorial = 1       
        for j in range(1, i + 1):   # liczenie silni poprzez mnozenie liczb od 1 do i wlacznie
            factorial *= j
        print("Silnia liczby ", i, " wynosi: ", factorial)
        factorials.append(factorial)
    for i in range(1, len(factorials)):
        print("Roznica miedzy silnia z liczby ", i+1, " a silnia z liczby ", i, " wynosi: ", factorials[i]-factorials[i-1])
    
def CheckIfCorrect(endOfRangeF):
    while endOfRangeF <= 0 or endOfRangeF > 10000:
        os.system('clear')
        endOfRangeF = int(input("Podaj inna liczbe z zakresu [1, 10000]: "))        
    FactorialN(endOfRangeF)        
        
endOfRange = int(input("Podaj liczbe, do ktorej zostanie policzona silnia: "))  #maksymalna liczba dla ktorej nie pojawi sie blad to 1558
CheckIfCorrect(endOfRange)

'''
Silnia liczby  1  wynosi:  1
Silnia liczby  2  wynosi:  2
Silnia liczby  3  wynosi:  6
Silnia liczby  4  wynosi:  24
Roznica miedzy silnia z liczby  2  a silnia z liczby  1  wynosi:  1
Roznica miedzy silnia z liczby  3  a silnia z liczby  2  wynosi:  4
Roznica miedzy silnia z liczby  4  a silnia z liczby  3  wynosi:  18
'''
