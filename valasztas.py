from builtins import int
from kepviselo import Kepviselo


def list_from_file(filename: str) -> list:
    with open(filename, "r") as f:
        szavazatok = f.readlines()
        return szavazatok


def kepviselo_letrehozasa(adatai: str) -> Kepviselo:
    adatai = adatai.split()
    return Kepviselo(str(f"{adatai[2]} {adatai[3]}"), int(adatai[0]), adatai[4], int(adatai[1]))


def kepviselok_szama(lista: list) -> int:
    return len(lista)


def nevbol_szavazatszam(kepviselok: list):
    helyes_nev = False
    while not helyes_nev:
        vezeteknev = input("Kérem adja meg a képviselő vezeteknevét: ")
        keresztnev = input("Kérem adja meg a képviselő keresztnevét: ")
        if vezeteknev.isalpha() and keresztnev.isalpha():
            helyes_nev = True
        megtalalva = False
        for kepviselo in kepviselok:
            if kepviselo.nev == str(f"{vezeteknev} {keresztnev}"):
                megtalalva = True
                print(f"A {kepviselo.nev}-ra adott szavazatok száma: {kepviselo.szavazatok_szama}")
        if megtalalva is False:
            print("Nincs ilyen nevű képviselő.")
        else:
            print("Hibás adatmegadás, kérem próbálja újra")


def reszveteli_arany(szavazasra_jogosultak: int, kepviselok: list) -> int:
    szavazatok_szama = 0
    for kepviselo in kepviselok:
        szavazatok_szama += kepviselo.szavazatok_szama
    print(f"Összesen {szavazatok_szama}fő szavazott, ez a jogosultak "
          f"{szavazatok_szama/szavazasra_jogosultak*100:.2f}%-a.")
    return szavazatok_szama


def partszavazok(kepviselok: list, ossz_szavazatok_szama):
    gyep = hep = tisz = zep = fuggetlenek = 0
    for kepviselo in kepviselok:
        if kepviselo.part_neve == "GYEP":
            gyep += kepviselo.szavazatok_szama
        elif kepviselo.part_neve == "HEP":
            hep += kepviselo.szavazatok_szama
        elif kepviselo.part_neve == "TISZ":
            tisz += kepviselo.szavazatok_szama
        elif kepviselo.part_neve == "ZEP":
            zep += kepviselo.szavazatok_szama
        elif kepviselo.part_neve == "-":
            fuggetlenek += kepviselo.szavazatok_szama
    print(f"Gyümölcsevők pártja: {gyep / ossz_szavazatok_szama * 100:.2f}%")
    print(f"Gyümölcsevők pártja: {hep / ossz_szavazatok_szama * 100:.2f}%")
    print(f"Gyümölcsevők pártja: {tisz / ossz_szavazatok_szama * 100:.2f}%")
    print(f"Gyümölcsevők pártja: {zep / ossz_szavazatok_szama * 100:.2f}%")
    print(f"Gyümölcsevők pártja: {fuggetlenek / ossz_szavazatok_szama * 100:.2f}%")


def legtobbszavazat(kepviselok: list):
    legtobb = 0
    for kepviselo in kepviselok:
        if kepviselo.szavazatok_szama > legtobb:
            legtobb = kepviselo.szavazatok_szama
    for kepviselo in kepviselok:
        if kepviselo.part_neve == "-":
            kepviselo.part_neve = "független"
        if kepviselo.szavazatok_szama == legtobb:
            print(f"A legtobb szavazatot {kepviselo.nev} {kepviselo.part_neve} kapta")


def gyoztesek(kepviselok: list):
    x = 1
    while x <= 8:
        legtobb = 0
        for kepviselo in kepviselok:
            if kepviselo.valasztoker == x and kepviselo.szavazatok_szama > legtobb:
                legtobb = kepviselo.szavazatok_szama
        for kepviselo in kepviselok:
            if kepviselo.valasztoker == x and kepviselo.szavazatok_szama == legtobb:
                with open("kepviselok.txt", "a") as f:
                    f.write(f"{kepviselo.valasztoker} {kepviselo.nev}\n")
        x += 1
        
        