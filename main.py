# 1) Podaj liczbe wejsciowa
# 2) Zakres liczb 0d 1 do 100
# 3) Inna liczba, wroc do wprowadzenia prawidlowej
# 4) Sprawdz czy liczba różna od 1, jeśli nie to koniec zadania
# 5)Sprawdz czy liczba parzysta
#     - jesli tak to x=x//2
#     - jesli nie to x=3*x+1
# 6) ciag - ilość wykonania pętli
# każda petla +1 na koniec pętli
# 7) Każdorazowo wypisz liczbę (do sprawdzenia)
#


x = int(input("Podaj liczbę x (od 1 do 100): "))
while x < 1 or x > 100:
    x = int(input("Liczba x musi być z przedziału od 1 do 100. Podaj jeszcze raz: "))
ciag = 1
while x != 1:
    if x % 2 == 0:
        x = x // 2
        print(x)
    else:
        x = 3 * x + 1
        print(x)
    ciag += 1
print("Długość ciągu Collatza dla liczby", x, "wynosi", ciag)