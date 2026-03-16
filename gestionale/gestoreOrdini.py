#Scrivere un software che abbia seguenti funzioni:
#-supportare arrivo e gestione ordini
#-quando arriva nuovo ordine aggiungo in una cosa assicurandomi che venga eseguito dopo
#-avere delle funzionalità per aver statistiche su ordini
#-fornire statistiche su distribuzione di ordini per categorie di clienti

from collections import deque, defaultdict, Counter

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import Prodotto, ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdini:

    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)

    def add_ordine(self,ordine:Ordine):
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto un nuovo ordine da parte di {ordine.cliente}")
        print(f"Ordini ancora da evadere: {len(self._ordini_da_processare)}")

    def processa_prossimo_ordine(self):
        #questo metodo legge il prossimo ordine in coda e lo gestisce
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda")
            return False

        ordine = self._ordini_da_processare.popleft()
        print(f"Sto processando l'ordine di {ordine.cliente}")
        print(ordine.riepilogo())

        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)
        self._ordini_processati.append(ordine)
        print(f"Ordine correttamente processato")
        return True

    def processa_tutti_ordini(self):
        print("\n" + "=" * 60)
        print(f"Processando {len(self._ordini_da_processare)} ordini")
        while self._ordini_da_processare:
            self.processa_prossimo_ordine()
        print("Tutti gli ordini son stati processati")

    def get_statistiche_prodotti(self, top_n: int=5):
        #questo restituisce info sui prodotti più venduti con quante unità siano state vendute per prodotto
        valori=[]
        for prodotto,quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto,quantita))
        return valori

    def get_distribuzione_categoria(self):
        #questo metodo restituisce info su un totale fatturato per ogni categoria presente
        valori=[]
        for cat in self._ordini_per_categoria.keys():
            ordini = self._ordini_per_categoria[cat]
            totale_fatturato = sum([o.totale_lordo(0.22) for o in ordini])
            valori.append((cat,totale_fatturato))
        return valori

    def stampa_riepilogo(self):
        #stampa info business
        print("\n" + "="*60)
        print("Stato attuale del business:")
        print(f"Ordini correttamente eseguiti: {len(self._ordini_processati)} ordini")
        print(f"Ordini in coda: {len(self._ordini_da_processare)} ordini")

        print("Prodotti più venduti:")
        for prod,quantita in self.get_statistiche_prodotti():
            print(f"{prod}: {quantita}")

        print("Fatturato per categoria:")
        for cat,fatturato in self.get_distribuzione_categoria():
            print(f"{cat}: {fatturato}")

def test_modulo():
    sistema = GestoreOrdini()

    ordini = [
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop",1200.0),1),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)
        ],ClienteRecord("Mario Rossi","mariorossi@gmail.com","Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Tablet", 2000.0), 1),
            RigaOrdine(ProdottoRecord("Cuffie", 100.0), 3)
        ], ClienteRecord("Fulvio Bianchi", "fulviobianchi@gmail.com","Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 2),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 2)
        ], ClienteRecord("Giuseppe Averta","giuseppeaverta@gmail.com","Silver")),
        Ordine([
            RigaOrdine(ProdottoRecord("Tablet", 2000.0), 1),
            RigaOrdine(ProdottoRecord("Cuffie", 100.0), 1)
        ], ClienteRecord("Carlo Masone","carlomasone@gmail.com","Gold")),
        Ordine([
            RigaOrdine(ProdottoRecord("Laptop", 1200.0), 2),
            RigaOrdine(ProdottoRecord("Mouse", 10.0), 1)
        ], ClienteRecord("Francesca Pistilli","francescapistilli@gmail.com","Bronze")),
    ]

    for o in ordini:
        sistema.add_ordine(o)

    sistema.processa_tutti_ordini()
    sistema.stampa_riepilogo()

if __name__ == "__main__":
    test_modulo()