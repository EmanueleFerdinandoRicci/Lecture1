import copy
from collections import Counter

from networkx.classes import non_edges

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine

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
catalogo = {
    "LAP001":ProdottoRecord("Laptop", 1200.0),
    "LAP002":ProdottoRecord("Laptop Pro", 2300.0),
    "MOU001":ProdottoRecord("Mouse", 20.0),
    "AUR001":ProdottoRecord("Auricolari", 250.0)
}

cod = "LAP002"
prod= catalogo[cod] #così non devo fare i cicli
print(f"Il prodotto con codice {cod} è {prod}")

prod1 = catalogo.get("NONESISTE") #con il get mette non se lo avessi solo cercato dava errore
if prod1 is None:
    print("Prodotto non trovato")

prod2 = catalogo.get("NONESISTE",ProdottoRecord("NunTeConosco", 0.0)) #o Sconosciuto
print(prod2)

keys = list(catalogo.keys())
values = list(catalogo.values())
#danno entrambi set con chiavi o valori o con list davanti diventa lista

for k in keys:
    print(k)
for v in values:
    print(v)

for key,val in catalogo.items():
    print(f"Cod {key} è associata a : {val}")

#rimuovere
rimosso = catalogo.pop("LAP002")
print(rimosso)

#dict comprehension
prezzi = {codice: prod.prezzo_unitario for codice, prod in catalogo.items()}

#DA RICORDARE PER DICT
#v = dict[key] #leggere ma se non esiste key da errore
#dict[key] = v #scrivere
#v = dict.get(key,default) #legge senza possibile errore di keyerror
#p = dict.pop(key) #da il valore che  cancella dal dizionario
#dict.clear() #toglie tutto
#dict.keys()
#dict.values()
#dict.items() #coppie key value
#key in dict #verifica se chiave in dizionario

"""Esercizio
Per ciascuno dei seguenti casi, decidere quale struttura usare:"""

"""1) Memorizzare un elenco di ordini che dovranno poi essere processare in ordine di arrivo  LISTA"""

ordini_da_processare=[]
o1 = Ordine([],ClienteRecord("Mario Rossi","mariorossi@gmail.com","Gold"))
o2 = Ordine([],ClienteRecord("Vik Vik","vikivk@gmail.com","Gold"))
o3 = Ordine([],ClienteRecord("Tip Tap","tiptap@gmail.com","Gold"))
ordini_da_processare.append((o1,0))
ordini_da_processare.append((o2,10))
ordini_da_processare.append((o3,3))

"""2) Memorizzare i CF dei clienti (univoco)  SET"""

codici_fiscali={
    "akjkasncurbsu3223",
    "finrnuoenvbuc2835",
    "disuhgoerviow2802",
    "finrnuoenvbuc2835"
}
print(codici_fiscali) #ne farà tre perchè due uguali

"""3) Creare un database di prodotti che posso cercare con un codice univoco DIZIONARIO"""

listino_prezzi = {
    "LAP1": ProdottoRecord("Laptop", 1200.0),
    "LAP2": ProdottoRecord("LaptopPRO",3000.0)
}

"""4) Memorizzare le coordinate gps della nuova sede di ROMA TUPLA"""

magazzino_ROMA = (45,9)

"""5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale  SET"""

categorie = set()
categorie.add("Gold")

print("=================================================================================================")

#counter
lista_clienti={
    ClienteRecord("Mario Rossi","mariorossi@gmail.com","Gold"),
    ClienteRecord("Vik Vik","vikivk@gmail.com","Gold"),
    ClienteRecord("Tip Tap","tiptap@gmail.com","Gold"),
    ClienteRecord("Marco Rossi", "marco.rossi@outlook.it", "Silver"),
    ClienteRecord("Elena Bianchi", "elena88@gmail.com", "Silver"),
    ClienteRecord("Luca Verga", "luca.v@yahoo.it", "Bronze"),
    ClienteRecord("Sara Neri", "sara.neri@gmail.com", "Bronze")
}

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)

print("Distribuzione categorie clienti")
print(categorie_counter)

print("Categorie più frequenti")
print(categorie_counter.most_common(3)) # con valore dato

print("Totale:")
print(categorie_counter.total())

vendite_gennaio = Counter(
    {"Laptop": 13, "Stampante": 1}
)
vendite_febbraio = Counter(
    {"Laptop": 3, "Tablet": 21}
)

#aggregare
vendite = vendite_febbraio+vendite_gennaio
print(f"Vendite del bimestre: {vendite}")

#differenza
print(f"Differenza nella vendita da gennaio a febbraio: {vendite_gennaio-vendite_febbraio}")

#modifiche valori
vendite_gennaio["Laptop"] += 4
print(f"Vendite gennaio: {vendite_gennaio}")

#da ricordare per COUNTER
c.most_common(n) #restituisce gli n elementi più frequenti
c.total() #somma conteggi