import os
global balance
balance=0

def ifCorrect(choice):#funkcja sprawdzania poprawnosci wyboru i pinu
    while choice!=1 and choice!=2 and choice!=3 and choice!=4:
        print("Wybierz jedna z trzech opcji:", end=' ')
        choice=int(input())
        os.system('cls')
        if choice==1 or choice==2 or choice==3 or choice==4:
            break
        os.system('cls')

def checkPinF(checkpin):    
    if checkpin==pin:
        pass
    else:        
        while checkpin!=pin:
            os.system('cls')
            print("Podaj pin jeszcze raz: ", end=' ')
            checkpin=int(input())
            if checkpin==pin:
                print("Pin poprawny")
                break

def chooseOption(anotherChoice):
    balanceF=balance
    if anotherChoice == 1:
        deposit=int(input("Jaka kwote chcesz wplacic? "))
        balanceF+=deposit
        os.system('cls')
        print("Twoj stan konta wynosi:", balanceF)
        print("Co chcesz zrobic dalej?\nwplata - 1\nwyplata - 2\nsprawdz saldo konta - 3\nzakoncz - 4")
        anotherChoice=int(input())
        ifCorrect(choice)
        chooseOption(anotherChoice)
    elif anotherChoice == 2:
        withdrawal=int(input("Jaka kwote chcesz wyplacic? "))
        if withdrawal > balanceF:
            os.system('cls')
            print("Nie masz wystarczajacych srodkow na koncie")
            pass            
        elif withdrawal <= balanceF:
            balanceF-=withdrawal
            os.system('cls')
            print("Wyplaciles:", withdrawal, "zl. Twoj stan konta wynosi:", balanceF)            
        print("Co chcesz zrobic dalej?\nwplata - 1\nwyplata - 2\nsprawdz saldo konta - 3\nzakoncz - 4")
        anotherChoice=int(input())
        ifCorrect(choice)
        chooseOption(anotherChoice)
    elif anotherChoice == 3:
        os.system('cls')
        print("Twoj stan konta wynosi:", balanceF)
        print("Co chcesz zrobic dalej?\nwplata - 1\nwyplata - 2\nsprawdz saldo konta - 3\nzakoncz - 4")
        anotherChoice=int(input())
        ifCorrect(choice)
        chooseOption(anotherChoice)
    elif anotherChoice == 3:
        os.system('cls')
        print("Zamykanie...")
        exit()
######################################################################################

#ustawianie pinu do bankomatu
pin=int(input("Podaj czterocyfrowy kod pin do bankomatu: "))
while len(str(pin)) != 4:
    print("Podaj pin jeszcze raz:", end=' ')
    pin=int(input())
    if len(str(pin)) == 4:
        break

os.system('cls')

    #wybieranie operacji
print("Co chcesz zrobic?\nwplata - 1\nwyplata - 2\nsprawdz saldo konta - 3\nzakoncz - 4")
choice=int(input())
ifCorrect(choice)
checkpin=int(input("Potwierdz kodem pin:"))
checkPinF(checkpin)

if choice==1:
    deposit=int(input("Jaka kwote chcesz wplacic? "))
    balance+=deposit
    os.system('cls')
    print("Twoj stan konta wynosi:", balance)
    print("Co chcesz zrobic dalej?\nwplata - 1\nwyplata - 2\nsprawdz saldo konta - 3\nzakoncz - 4")
    anotherChoice=int(input())
    ifCorrect(choice)
    chooseOption(anotherChoice)
elif choice == 2:
    withdrawal=int(input("Jaka kwote chcesz wyplacic? "))
    if withdrawal > balance:
        os.system('cls')
        print("Nie masz wystarczajacych srodkow na koncie")        
    elif withdrawal <= balance:
        balance-=withdrawal
        os.system('cls')
        print("Wyplaciles:", withdrawal, "zl. Twoj stan konta wynosi:", balance)
        
    print("Co chcesz zrobic dalej?\nwplata - 1\nwyplata - 2\nsprawdz saldo konta - 3\nzakoncz - 4")
    anotherChoice=int(input())
    ifCorrect(choice)
    chooseOption(anotherChoice)
elif choice == 3:
    print("Twoj stan konta wynosi:", balance)
    print("Co chcesz zrobic dalej?\nwplata - 1\nwyplata - 2\nsprawdz saldo konta - 3\nzakoncz - 4")
    anotherChoice=int(input())
    ifCorrect(choice)
    chooseOption(anotherChoice)
elif choice == 4:
    os.system('cls')
    print("Zamykanie...")
    exit()


