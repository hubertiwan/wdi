#wypisanie danych bez zmiennych

print("Hubert Iwanowski", 20, "pizza pies", round(5/7, 1), round(5/7, 3), round(5/7, 5), round(5/7, 10))  

print("Hubert",end=' ')
print("Iwanowski",end=' ')
print(20,end=' ')
print("pizza",end=' ')
print("pies",end=' ')
print(round(5/7, 1),end=' ') #5/7 zaokrąglone do 1 miejsca po przecinku
print(round(5/7, 3),end=' ') #5/7 zaokraglone do 3 miesjc po przecinku
print(round(5/7, 5),end=' ') #5/7 zaokraglone do 5 miesjc po przecinku
print(round(5/7, 10)) #5/7 zaokraglone do 10 miesjc po przecinku

#wypisywanie danych ze zmiennymi
name="Hubert"
surname="Iwanowski"
age=20
favfood="pizza"
favpet="pies"
floatnum=5/7

print(name, surname, age, favfood, favpet, round(floatnum, 1), round(floatnum, 3), round(floatnum, 5), round(floatnum, 10))

print(name,end=' ')
print(surname,end=' ')
print(age,end=' ')
print(favfood,end=' ')
print(favpet,end=' ')
print(round(floatnum, 1),end=' ')
print(round(floatnum, 3),end=' ')
print(round(floatnum, 5),end=' ')
print(round(floatnum, 10))