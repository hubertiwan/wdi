#program wypisujacy silnie liczb z zakresu od 1 do M, gdzie M jest liczba podana przez uzytkownika

import os,time
global factorial, tempFactorial

def FactorialN(endOfRangeF):
    tempFactorial = 1
    factorials = []
    for i in range(1, endOfRangeF + 1):# liczby od 1 do konca zakresu podanego przez uzytkownika
        factorial = 1       
        for j in range(1, i + 1): #liczenie silnii poprzez mnozenie liczb od 1 do i wlacznie
            factorial *= j
        print("Silnia liczby ", i, " wynosi: ", factorial)
        factorials.append(factorial)
    for i in range(1, len(factorials)): #podany zakres bo dla 'i in factorials' wychodzimy poza zakres
        print("Roznica miedzy silnia z liczby ", i+1, " a silnia z liczby ", i, " wynosi: ", factorials[i]-factorials[i-1])
    
def CheckIfCorrect(endOfRangeF):
    while endOfRangeF <= 0 or endOfRangeF > 10000:
        endOfRangeF = int(input("Podaj inna liczbe z zakresu [1, 10000]: "))
        #CheckIfCorrect(endOfRangeF1)
        time.sleep(0.2)
        os.system('cls')
    FactorialN(endOfRangeF)        
        
endOfRange = int(input("Podaj liczbe, do ktorej zostanie policzona silnia: "))#maksymalna liczba dla ktorej nie pojawi sie blad to 1558
CheckIfCorrect(endOfRange)
