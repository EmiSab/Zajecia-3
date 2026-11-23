n = int(input())
poprawne = 0
for liczba in range(1, n + 1):
    print(f"Podaj kwadrat liczby {liczba}")
    poprawny_kwadrat = liczba * liczba
    proby = 0
    zgadnieto = False
    while proby < 3 and not zgadnieto:
        odpowiedz = int(input())
        proby += 1
        if odpowiedz == poprawny_kwadrat:
            print("Poprawna odpowiedz")
            poprawne += 1 
        else:
            print("Bledna odpowiedz")
print(f"Poprawnie rozwiazane: {poprawne}")