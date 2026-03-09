import copy

from gestionale.core.prodotti import ProdottoRecord

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1,p2,p3,ProdottoRecord("Tablet",700.0)]

print("Prodotti nel carrello:")
for i,p in enumerate(carrello):
    print(f"{i} {p.name} - {p.prezzo_unitario}")

#Aggiungere ad una lista
carrello.append(ProdottoRecord("Monitor", 150.0))

carrello.sort(key=lambda x: x.prezzo_unitario) #crescente con reverse = true invece descrescente

print("Prodotti nel carrello:")
for i,p in enumerate(carrello):
    print(f"{i} {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Prezzo totale: {tot}")

#aggiungere
carrello.append(ProdottoRecord("A",10.0)) #passa singolo elemento
carrello.extend([ProdottoRecord("B",20.0),ProdottoRecord("C",15.0)]) #passa lista
carrello.insert(2,ProdottoRecord("D",60.0)) #all'indice 2 inserisco elemento
#rimuovere
carrello.pop() #rimuove ultimo elemento
carrello.pop(2) #rimuove elemento in pos 2
carrello.remove(p1) #rimuove il primo p1 che trova nella lista
#carrello.clear() #elimina tutto
#sorting
#carrello.sort() #ordina seguendo ordinamento naturale con lt
#carrello.sort(reverse=True) #al contrario
#carrello.sort(key= function) #fuction = itemgetter() o lambda
#carrello_ordinato = sorted(carrello)
#carrello.reverse() #inverte ordine
#copie
carrello_copia = carrello.copy() #crea shallow copy (ovvero stesso identici oggetti)
carrello_copia2 = copy.deepcopy(carrello) #deepcopy copia ma crea due oggetti uguali ma separati
#tuple
sede_principale = (45,8) #lat e long di sede di Torino (esempio)
sede_milano = (45,9) #lat e long di sede di Milano

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")
print(f"Sede Milano lat: {sede_milano[0]}, long: {sede_milano[1]}")

aliquoteIVA = (
    ("Standard",0.22),
    ("Ridotta",0.10),
    ("Alimentare",0.04),
    ("Esente",0.0)
)

for descr,valore in aliquoteIVA:
    print(f"{descr}: {valore*100} %")

def calcola_statistiche_carrello(carrello):
    #restituisce prezzo_totale,prezzo_medio,max,min
    prezzi = [p.prezzo_unitario for p in carrello]
    return (sum(prezzi), sum(prezzi) / len(prezzi), max(prezzi), min(prezzi))

tot,media,v_max,v_min = calcola_statistiche_carrello(carrello)
tot, *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

#set
categoria = {"Gold", "Silver", "Bronze", "Gold"}
print(categoria)
print(len(categoria))
categoria2 = {"Platinum", "Elite", "Gold"}
categorie_all = categoria | categoria2 # aggiunge a 1 la 2 (unisce)
print(categorie_all)
categorie_comuni = categoria & categoria2
print(categorie_comuni)

categorie_esclusive1 = categoria - categoria2 #solo elementi presenti in 1 e non 2
print(categorie_esclusive1)

categorie_esclusive_tot = categoria ^ categoria2 # toglie l'intersezione e restituisce gli univoci delle due
print(categorie_esclusive_tot)

prodotti_ordineA = {
    ProdottoRecord("Laptop", 1200.0),
    ProdottoRecord("Mouse", 20.0),
    ProdottoRecord("Auricolari", 250.0)
}

prodotti_ordineB = {
    ProdottoRecord("Laptop", 1200.0),
    ProdottoRecord("Mouse", 20.0),
    ProdottoRecord("Auricolari", 250.0)
}

#metodi utili per i set
s = set()
s1 = set()
s.add(ProdottoRecord("Laptop", 1200.0))
s.update([ProdottoRecord("Laptop", 1200.0),ProdottoRecord("Mouse", 20.0)])
#togliere
#s.remove(elem) #rimuove un elemento e se non esiste errore
#s.discard(elem) #rimuove un elemento ma se non esiste non da errore
s.pop() #rimuove e restituisce elem
s.clear()
#operazioni insiemistiche
s.union(s1)
s.intersection(s1)
s.difference(s1)
s.symmetric_difference(s1)
s.issubset(s1) #se gli elementi di s1 sono contenuti in s
s.issuperset(s1) #se gli elementi di s sono contenuti in s1
s1.isdisjoint(s) #se gli elementi di s e s1 sono diversi (1 se vero)

#dizionari