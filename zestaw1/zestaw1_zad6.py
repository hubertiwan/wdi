num1=int(input("Podaj pierwsza liczbe: ")) #wprowadzenie pierwszej liczby
num2=int(input("Podaj druga liczbe: ")) #wprowadzenie drugiej liczby

#sprawdzanie warunkow

if num1<0 and num2<0:#jesli obie liczby ujemne koniec programu
    print("Obie liczby sa ujemne. Koniec programu.")
    exit()
elif num1<0 and num2>0:#jesli pierwsza liczba ujemna, a druga dodatnia to num1 przyjmuje wartosc bezwzgledna tej liczby
    num1=abs(num1)
elif num1>0 and num2<0:#jesli druga liczba ujemna, a pierwsza dodatnia to num2 przyjmuje wartosc bezwzgledna tej liczby
    num2=abs(num2)    

'''
obliczanie:
sumy, różnicy, iloczynu, ilorazu, kwadaratu oraz pierwiastka
liczb num1 i num2
'''

print("Suma liczb", num1, "i", num2, "wynosi", num1+num2)
print("Różncia liczb", num1, "i", num2, "wynosi", num1-num2)
print("Iloczyn liczb", num1, "i", num2, "wynosi", num1*num2)
print("Iloraz liczb", num1, "i", num2, "wynosi", num1/num2)
print("Kwadrat liczby", num1, "wynosi", num1**2)
print("Kwadrat liczby", num2, "wynosi", num2**2)
print("Pierwiastek liczby", num1, "wynosi", num1**(1/2))
print("Pierwiastek liczby", num2, "wynosi", num2**(1/2))

if num1*num2==10:
    print("Yay")
