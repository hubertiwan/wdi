# program wczytujacy tablice dwuwymiarowa o wymiarach n x n, gdzie n jest podane przez uzytkownika
# program uzupełnia tablice losowymi liczbami naturalnymi
# program zwraca liczbe par elementow o podanym iloczynie odleglych od siebie w tablicy o jeden ruch skoczka szachowego

import random

global size
size = 0
board = []

def SetBoardSize():
    global board
    global size
    size = int(input("Podaj wielkosc tablicy: "))
    board = [[None]*size for _ in range(size)] # wypelnia wartoscia 'None' size-razy, tworzy size takich list -> tablica dwuwymiarowa; '_' oznacza zmienna zastepcza, nieuzywana pozniej

def GeneratingNumbers():
    global board
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = random.randint(0, 5)            

def PrintBoard():    
    for i in range(len(board)):  
        for j in range(len(board[i])):
            if board[i][j] < 10:
                print(board[i][j], end="  ")      
            else:
                print(board[i][j], end=" ") 
        print()  
    
def CountingPair():
    product = int(input("Podaj iloczyn, ktory chcesz sprawdzic: "))
    pairsSum = 0
    length = len(board)
        
    for i in range(length): # petle z 'i' i 'j' trzymaja jeden punkt, a z 'x' i 'y' ida po calej tablicy sprawdzajc warunki z dwóch if-ow
        for j in range(length):
            for x in range(length):
                for y in range(length):
                    if i != x and j != y: # punkt sprawdzany [x][y] ma byc rozny od punkty do ktorego porownujemy [i][j]
                        if abs(i-x) * abs(j-y) == 2 and board[i][j] * board[x][y] == product: # abs(i-x) * abs(j-y) == 2 --> skoczek, dwa do przodu, jeden w bok
                            pairsSum += 1
    pairsSum = pairsSum // 2 # liczba policzonych par jest podwojna, wiec dzielimy na 2         
    print(f"Liczba par elementow o iloczynie {product}, odleglych od siebie o jeden ruch skoczka szachowego wynosi: {pairsSum}")
        
SetBoardSize()
GeneratingNumbers()
PrintBoard()
CountingPair()












'''
for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] * board[i+2][j-1] == product:
                pairsSum += 1
            elif board[i][j] * board[i+2][j+1] == product:
                pairsSum += 1
            elif board[i][j] * board[i-1][j+2] == product:
                pairsSum += 1
            elif board[i][j] * board[i+1][j+2] == product:
                pairsSum += 1 
            elif board[i][j] * board[i-2][j-1] == product:
                pairsSum += 1
            elif board[i][j] * board[i-2][j+1] == product:
                pairsSum += 1
            elif board[i][j] * board[i-1][j-2] == product:
                pairsSum += 1
            elif board[i][j] * board[i+1][j-2] == product:
                pairsSum += 1 
'''
