vstupni_text = "Ahoj všem, tady Engeto"
def zdvojnasob_znaky(text):
  zdvojene = list()
  for znak in text:
    znak += znak
    zdvojene.append(znak)
  return zdvojene
vysledek = zdvojnasob_znaky(vstupni_text)
print("Zdvojene znaky:","".join(vysledek))