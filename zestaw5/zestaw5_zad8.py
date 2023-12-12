# dane [(x1, y1),(x2, y2),(x3, y3),...,(xN, yN)]
# funkcja -> 'True' jesli w zbiorze dane sa 3 punkty ktore tworza trojkat rownoboczny
# wewnatrz trojkatu nie moze byc zadnych innych punktow
# program ma wskazac podane punkty

import random, math

global size
amounnt = 0
data = []

def SetSize():
    global amount
    amount = int(input("Podaj ilosc punktow: "))
    return amount
        
def GeneratingPoints(amountF):    
    for i in range(0, amountF):
        x = round(random.uniform(0, 20), 5)
        y = round(random.uniform(0, 20), 5)        
        point = [x, y]
        data.append(point)
    print(data)
    
def Distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def TriangleArea(x1, y1, x2, y2, x3, y3):
    return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

def CheckingEquilateralTriangle(length1, length2, length3, tolerance = 0.01):
    if abs(length1 - length2) < tolerance and abs(length1 - length3) < tolerance and abs(length2 - length3) < tolerance:
        return True
    else:
        return False

def Main():
    global amount
    countTriangles = 0
    
    for i in range(amount):
        for j in range(i + 1, amount):
            for k in range(j + 1, amount):                
                distance1 = Distance(data[i], data[j])
                distance2 = Distance(data[j], data[k])
                distance3 = Distance(data[i], data[k])
                if CheckingEquilateralTriangle(distance1, distance2, distance3, tolerance = 0.01) == True:
                    for x in data:
                        if x != data[i] and x != data[j] and x != data[k]:
                            triangleAreaMain = TriangleArea(data[i][0], data[i][1], data[j][0], data[j][1], data[k][0], data[k][1])
                            triangleArea1 = TriangleArea(x[0], x[1], data[j][0], data[j][1], data[k][0], data[k][1])
                            triangleArea2 = TriangleArea(data[i][0], data[i][1], x[0], x[1], data[k][0], data[k][1])
                            triangleArea3 = TriangleArea(data[i][0], data[i][1], data[j][0], data[j][1], x[0], x[1])
                        if abs(triangleAreaMain - (triangleArea1 + triangleArea2 + triangleArea3)) < 0.01:
                            countTriangles += 1
                            print(data[i], data[j], data[k])
                            break                               
                    
    print(countTriangles)         
                
GeneratingPoints(SetSize())
Main()

'''
CZY WYGENEROWANE PUNKTY TWORZA TROJKAT ROWNOBOCZNY?
WWYGENEROWANE WSPOLRZEDNE:
1. [5.84095, 14.93834]
2. [1.85261, 10.76853]
3. [7.46103, 9.40353]
__              __              __
12 = 5.7701     13 = 5.767      23 = 5.7721  -->  dokladnosc 0.01
'''
