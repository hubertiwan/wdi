import random, os

def ifContinue():
    yn=str(input("Czy chcesz wprowadzic nowe dane?y/n: "))
    if yn == "y":
        choice=str(input("Jakie dzialanie chcesz wykonac?\n+ - dodawanie\n- - odejmowanie\n"
        "* - mnozenie\n/ - dzielenie\n^ - potegowanie\n# - pierwiastkowanie\nx - losowanie liczby\n"))
        action(choice)
    elif yn == "n":
        exit()

def action(choice):
    os.system('cls')
    if choice == '+':
        num1=int(input("Podaj pierwsza liczbe: "))
        num2=int(input("Podaj druga liczbe: "))
        print("Suma liczb", num1, "i", num2, "wynosi:", num1 + num2)
        ifContinue()
    elif choice == '-':
        num1=int(input("Podaj pierwsza liczbe: "))
        num2=int(input("Podaj druga liczbe: "))
        print("Roznica liczb", num1, "i", num2, "wynosi:", num1 - num2)
        ifContinue()
    elif choice == '*':
        num1=int(input("Podaj pierwsza liczbe: "))
        num2=int(input("Podaj druga liczbe: "))
        print("Iloczyn liczb", num1, "i", num2, "wynosi:", num1 * num2) 
        ifContinue()
    elif choice == '/':
        num1=int(input("Podaj pierwsza liczbe: "))
        num2=int(input("Podaj druga liczbe: "))
        print("Iloraz liczb", num1, "i", num2, "wynosi:", num1 / num2)
        ifContinue()
    elif choice == '^':
        num1=int(input("Podaj pierwsza liczbe: "))
        num2=int(input("Podaj druga liczbe: "))
        print("Liczba", num1, "do potegi", num2, "wynosi:", num1**num2)
        ifContinue()
    elif choice == '#':
        num1=int(input("Podaj pierwsza liczbe: "))
        num2=int(input("Podaj druga liczbe: "))
        print("Pierwiastek liczby", num1, "stopnia", num2, "wynosi:", num1**(1/num2))
        ifContinue()
    elif choice == 'x':
        num1=int(input("Podaj pierwsza liczbe: "))
        num2=int(input("Podaj druga liczbe: "))    
        print("Losowa liczba z zakresu od", num1, "do", num2, "wynosi:", random.randint(num1, num2))
        ifContinue()

#wybor funkcji
choice=str(input("Jakie dzialanie chcesz wykonac?\n+ - dodawanie\n- - odejmowanie\n"
        "* - mnozenie\n/ - dzielenie\n^ - potegowanie\n# - pierwiastkowanie\nx - losowanie liczby\n"))

action(choice)
