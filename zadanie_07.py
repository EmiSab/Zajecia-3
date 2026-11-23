n = int(input())
suma = 0
for _ in range(n):
    wynik = int(input())
    while wynik <0 or wynik > 100:
        print("Niepoprawny wynik")
        wynik = int(input())
    suma += wynik
print(f"Suma: {suma}")