hledane_cislo = 7
dotazovani = True
pokusy = []

while dotazovani:
    cislo = int(input("Hadej cislo od 1 do 10:"))
    pokusy.append(cislo)
    if cislo < 7:
        print("tohle cislo je mensi nez to, ktere si myslim, hadej znovu!")
    elif cislo > 7:
        print("tohle cislo je vetsi nez to, ktere si myslim, hadej znovu!")
    elif cislo == hledane_cislo:
        print(f"spravne! cislo {cislo} jsem si myslela!Uhadl jsi ho za {len(pokusy)} pokusu.")
        dotazovani = False
        break










    
