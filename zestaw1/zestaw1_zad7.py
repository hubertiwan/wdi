#wporwadzenie liczb
num1=int(input("Podaj pierwsza liczbe: "))
num2=int(input("Podaj druga liczbe: "))

#uzywajac petli for
print("\nUzywajac petli for:")
if abs(num1-num2)<=20:
    for x in range(num1+1, num2, 1):
        print(x)
elif abs(num1-num2)>20:
    mean=int(abs((num1-num2)/2)) #obliczanie sredniej zakresu
    for x in range(mean-3, mean+4, 1):
        if x==mean:            
            continue
        print(x)

#uzywajac petli while
print("\n\nUzywajac petli while:")
if abs(num1-num2)<=20:
    num1+=1
    while num1<num2:        
        print(num1)
        num1+=1
elif abs(num1-num2)>20:
    mean=int(abs((num1-num2)/2)) #obliczanie sredniej zakresu
    num1=mean-4                  #przypisanie do zmiennej num1 sredniej zakresu -4
    while num1<mean+3:           #wypisanie liczb {mean-3, mean-2, mean-1, mean+1, mean+2, mean+3}
        num1+=1                  #mean+3 bo inkrementacja na poczatku
        if num1==mean:            
            continue
        print(num1)
        
        
