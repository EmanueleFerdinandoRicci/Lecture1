print("-------------------")
print("SPERIMENTAZIONE DATACLASS")

from gestionale.core.clienti import ClienteRecord
from gestionale.vendite.ordini import Ordine,RigaOrdine,OrdineSconto
from gestionale.core.prodotti import ProdottoRecord

cliente1 = ClienteRecord("Mario Rossi", "mariorossi@gmail.com", "Gold")
p1 = ProdottoRecord("Laptop", 1200)
p2 = ProdottoRecord("Mouse", 20)

ordine = Ordine([RigaOrdine(p1,2),RigaOrdine(p2,10)], cliente1)
ordine_scontato = OrdineSconto([RigaOrdine(p1,2),RigaOrdine(p2,10)], cliente1, 0.10)

print(ordine) #crea essendo una dataclass un repr ragionevole
print("Numero di righe : ",ordine.numero_righe())
print("Totale netto: ", ordine.totale_netto())
print("Totale lordo(IVA 22%) : ", ordine.totale_lordo(0.22))

print(ordine_scontato) #crea essendo una dataclass un repr ragionevole
print("Numero di righe : ",ordine_scontato.numero_righe())
print("Totale netto: ", ordine_scontato.totale_netto())
print("Totale lordo(IVA 22%) : ", ordine_scontato.totale_lordo(0.22))
#il totale lordo viene preso dalla classe padre

print("--------------------------------")

from gestionale.core.prodotti import Prodotto, crea_prodotto_standard
#per prendere il PRODOTTO da prodotti
p1 = Prodotto(name="Ebook",price=120,quantity=1,supplier="AAA")
p2 = crea_prodotto_standard(nome="Tablet",prezzo=750)

print(p1)
print(p2)

#PER IMPORTARE

from gestionale.core.prodotti import ProdottoScontato as ps # gli do anche un nome alternativo
p3 = ps(name="Auricolari",price=230,quantity=1,supplier="AAA",sconto_percento=10)
from gestionale.core import prodotti as p

p4 = p.ProdottoScontato(name="Tastiera",price=270,quantity=1,supplier="AAA",sconto_percento=30)

from gestionale.core.clienti import Cliente
c1 = Cliente(nome="Mario Rossi",email="mariorossi@gmail.com", categoria="Gold")

#dir() di un modulo ci dice che funzioni ha il modulo

#per installare
import networkx as nx
#oppure vedo in pycharm package (secondo tasto dall'alto in fondo a sx)