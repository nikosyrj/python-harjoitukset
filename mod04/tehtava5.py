oikea_tunnus = "nikoadmin"
oikea_salasana = "pythonkurssitesti"
yritykset = 0
kirjautunut = False
while yritykset < 5 and not kirjautunut:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")
    yritykset = yritykset + 1
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        kirjautunut = True
if kirjautunut:
    print("Tervetuloa")
else:
    print("Pääsy evätty")