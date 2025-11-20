"""
Opgave "Cars":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en funktion drive_car(), der udskriver en bils motorlyd (f.eks. "roooaar")

I hovedprogrammet:
    Definer variabler, som repræsenterer antallet af hjul og den maksimale hastighed for 2 forskellige biler
    Udskriv disse egenskaber for begge biler
    Kald derefter funktionen drive_car()

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du åbne 0460_cars_help.py og starte derfra.
Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.
Hvis du stadig er gået i stå, skal du åbne 0470_cars_solution.py og sammenligne den med din løsning.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import time


def drive_car():
    print("Roaaaar")

print("Hvor mange hjul har din første bil?")
car1wheel = input()
print("Hvor hurtigt kan din første bil køre?")
car1maxspeed = input()
print("Hvor mange hjul har din anden bil?")
car2wheel = input()
print("Hvor hurtigt kan din anden bil køre?")
car2maxspeed = input()

print(f"Din første bil har {car1wheel} hjul, og kan køre {car1maxspeed} km/t")
time.sleep(5)
print(f"Din anden bil har{car2wheel} hjul, og kan køre {car2maxspeed} km/t")
drive_car()