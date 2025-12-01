""" Øvelse: "Calculator"

Som altid, læs hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

-------

Opret et program, der fungerer som en simpel lommeregner. Programmet skal fungere som følger:
    1. Forklar brugeren hvordan man betjener programmet.
    2. Præsenter en menu med følgende muligheder:
        - Addition
        - Subtraktion
        - Multiplikation
        - Division
        - Afslut
    3. Bed brugeren om at vælge en mulighed fra menuen.
    4. Hvis brugeren vælger en aritmetisk operation, bed om to tal.
    5. Udfør den valgte operation og vis resultatet.
    6. Gentag processen, indtil brugeren vælger at afslutte.

-------

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""
while True:
    print("Velkommen til en lommeregner, Her kan du Plusse,Minusse,Gange,Dividere eller Exit")
    print("Matematik eller Exit?")
    test = input()
    if test == "Exit":
        break
    if test == "Matematik":
        print("Vælg et tal")
        tal1 = int(input())
        print("Vælg et andet tal")
        tal2 = int(input())
        print("Vil du plus,minus,gange eller dividere ")
        valg = input()

        if valg == "plus":
            resultplus = int(tal1 + tal2)
            print(resultplus)
            break

        if valg == "minus":
            resultminus = int(tal1 - tal2)
            print(resultminus)
            break

        if valg == "gange":
            resultgange = int(tal2 * tal1)
            print(resultgange)
            break

        if valg == "divider":
            resultdivider = int(tal2 / tal1)
            print(resultdivider)
            break

