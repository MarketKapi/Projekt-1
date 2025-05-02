vzor = {
    "byt0001": "1+1",
    "byt0002": "2+1",
    "byt0003": "2+kk",
    "byt0004": "3+1",
    "byt0005": "3+kk",
    "byt0006": "4+1",
    "byt0007": "4+kk",
}

udaje_k_bytum = [
    "byt0001,55m2,Olomouc,ul.Heyrovského,",
    "byt0003,65m2,Olomouc,ul.Novosadský_dvůr,",
]

def prevedeni_typu_bytu(seznam_udaju, vzor):
    prevedeni_nazvu = []
    for radek in seznam_udaju:
        polozky = radek.split(",")
        kod_bytu = polozky[0]
        if kod_bytu in vzor:
            polozky[0] = vzor[kod_bytu]
        novy_popis = ",".join(polozky)
        prevedeni_nazvu.append(novy_popis)
    return prevedeni_nazvu

upravena_data = prevedeni_typu_bytu(udaje_k_bytum, vzor)
for radek in upravena_data:
    print(radek)


    
    
        


