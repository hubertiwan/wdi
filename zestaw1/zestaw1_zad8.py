#pobieranie liczby naturalnej od uzytkwonika

height=int(input("Podaj liczbe ktora bedzie wysokoscia choinki:"))
while height<=0:
    print("Podales liczbe niedodtnia!\nPodaj liczbe jeszcze raz:",end=' ')
    height=int(input())

for i in range(1, height+1):  
    spaces=height-i                  #dla height=9 calkowita dlugosc wynosi 17, wiec spacji w pierwszej linii bedzie (17-1)/2
    stars=(2*i)-1                    #dlugosc gwiazdek (height*2)-1
    if i==1:
        tree=' '*spaces + "X"*stars   
    else:             
        if i%2==0:
            tree=' '*spaces + "o" + "*"*stars
        else:
            tree=' '*spaces + "*"*stars + "o"
    print(tree)                      #rysowanie linni drzewa
print((height-1)*' '+"U")            #rysowanie pnia
        

