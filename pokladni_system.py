# Načtení ceny nákupu
cena = int(input("Zadejte cenu nákupu:\n"))
# Načtení platby od uživatele, její převedení na celá čísla a sečtení
platba = input("Čím zaplatíte (oddělte bankovky čárkou):\n").split(',')
platba = [int(x) for x in platba]
platba = sum(platba)

# Definice funkce pro výpočet vrácených drobných
def vrat_drobne(cena, platba):
    # Seznam hodnot bankovek a mincí
    drobne = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    # Seznam pro uložení vrácených drobných
    vraceno = []
    # Výpočet částky k vrácení
    vratit = platba - cena

    # Pokud je platba menší než cena, vypočte se nedostatek a umožní uživateli doplatit
    if vratit < 0:
        nedostatek = cena - platba
        print("Musíte zaplatit ještě:", nedostatek, "Kč")
        doplatek = int(input("Čím doplatíte:\n"))
        platba += doplatek
        vratit = platba - cena
        # Výpočet vrácených drobných
        for hodnota in drobne:
            while vratit >= hodnota:
                vraceno.append(hodnota)
                vratit -= hodnota

    # Pokud je platba vyšší nebo rovná spočítá se kolik se má vrátit
    else:
        for hodnota in drobne:
            while vratit >= hodnota:
                vraceno.append(hodnota)
                vratit -= hodnota
    # Návrat seznamu vrácených drobných
    return vraceno
# Zavolání funkce pro výpočet drobných
vracene_drobne = vrat_drobne(cena, platba)
# Výpis vrácených drobných
print("Vrácené drobné:", vracene_drobne)