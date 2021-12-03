import valasztas

# 1. feladat
szavazatok = valasztas.list_from_file("szavazatok.txt")

kepviselok = []
for x in range(len(szavazatok)):
    kepviselok.append(valasztas.kepviselo_letrehozasa(str(szavazatok[x])))

# 2.feladat
print(f"{valasztas.kepviselok_szama(szavazatok)} jelölt indult a választásokon.")

# 3.feladat
valasztas.nevbol_szavazatszam(kepviselok)

# 4.feladat
szavazasra_jogusultak = 12345
ossz_szavazat_szama = valasztas.reszveteli_arany(szavazasra_jogusultak, kepviselok)

# 5.feladat
valasztas.partszavazok(kepviselok, ossz_szavazat_szama)

# 6.feladat
valasztas.legtobbszavazat(kepviselok)

# 7.feladat
valasztas.gyoztesek(kepviselok)
