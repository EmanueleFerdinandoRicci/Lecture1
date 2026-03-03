# Scriviamo un codice python che modelli una semplice
# gestione aziendale. Dovremmo prevedere la possibilità di
# definire entità che modellano i prodotti, i clienti,
# offrire interfacce per calcolare i prezzi, eventualmente scontati...
class Prodotto:
    aliquota_iva = 0.22  # variabile di classe che è uguale per tutte le istanze create

    def __init__(self, name: str, price: float, quantity: int, supplier: None):
        self.name = name
        self._price = None #per rendere inacessibile l'attributo della classe
        self.price = price
        self.quantity = quantity
        self.supplier = supplier

    def valore(self):
        return self._price * self.quantity

    def valore_lordo(self):
        netto = self.valore()
        lordo = netto * (1 + self.aliquota_iva)
        return lordo

    @classmethod  # il metodo non si riferisce all'istanze ma a tutta la classe, per esempio per creare un pattern
    # esempio costruttore alternativo
    def costruttore_con_quantita_1(cls, name: str, price: float, supplier: None):
        cls(name, price, quantity=1, supplier=supplier)  # su Pycharm Supplier e basta senza uguale

    @staticmethod
    def applica_sconto(prezzo, percentuale):  # non devo passare ne cls ne self
        return prezzo * (1 - percentuale)

    @property
    def price(self): #come un getter
        return self._price

    @price.setter #posso farlo solo se prima ho definito un getter
    def price(self, valore):
        if valore < 0:
            raise ValueError("Attenzione il prezzo non può essere negativo")
        self._price = valore

    def __str__(self):
        return f"{self.name}, Disponibilità: {self.quantity} a {self.price} euro"

    def __repr__(self):
        return f"Prodotto(name ={self.name}, price ={self.price}, quantity = {self.quantity}, supplier ={self.supplier})"

    def __eq__(self, other: object):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)

    def __lt__(self, other: "Prodotto")->bool:
        return self.price < other.price

    def prezzo_finale(self)->float:
        return self.price*(1+self.aliquota_iva)

class ProdottoScontato(Prodotto):
    def __init__(self, name: str, price: float, quantity: int, supplier: str, sconto_percento: float):
        #Prodotto.__init__()
        super().__init__(name, price, quantity, supplier)
        self.sconto_percento = sconto_percento

    def prezzo_finale(self)->float:
        return self.valore_lordo()*(1-(self.sconto_percento/100))

class Servizio(Prodotto):
    def __init__(self, name:str, tariffa_oraria: float, ore: int ):
        super().__init__(name=name,price=tariffa_oraria,quantity=1,supplier=None)
        self.ore=ore

    def prezzo_finale(self)->float:
        return self.price*self.ore

class Abbonamento:
    def __init__(self,name:str,prezzo_mensile:float,mesi:int):
        self.name = name
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self)->float:
        return self.prezzo_mensile*self.mesi

def calcola_totale(elementi):
    total = 0
    for elem in elementi:
        total += elem.prezzo_finale()
    return total

from dataclasses import dataclass

@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float

from typing import Protocol

#uso Protocol come classe da cui ereditare

class HaPrezzoFinale(Protocol):
    def prezzo_finale(self)->float:
        ... #uso i tre puntini per dire che non devo scrivere ora codice ma ci sarà una futura scrittura in delega

def calcola_totale(elementi: list[HaPrezzoFinale]):
    #in questo modo dico che gli elementi sono implementati con un protocollo che seguono
    return sum(e.prezzo_finale() for e in elementi) #sommatoria dei prezzi di elementi dentro la lista

MAX_QUANTITA = 1000

def crea_prodotto_standard(nome:str,prezzo:float):
    return Prodotto(nome,prezzo,quantity=1,supplier= None)

#UN MODULO BEN SCRITTO NON CONTIENE CODICE SCRIVIBILE
#MA POSSO AVERE UN MODULO CON CODICE DI VERIFICA
# se prodotti viene eseguito __name__="__main__"

def _test_modulo():
    #dentro ci metto tutto il codice da eseguire di verifica
    myproduct1 = Prodotto(name="Laptop", price=1200, quantity=12, supplier="ABC")  # su PyCharm si usa: invece che =
    print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

    print(f"Il valore totale del prod1 è {myproduct1.valore_lordo()}")  # funzione di istanza
    p3 = Prodotto.costruttore_con_quantita_1(name="Auricolari", price=200.0, supplier="ABC")
    print(f"Prezzo scontato di prod1 {Prodotto.applica_sconto(myproduct1.price, percentuale=0.15)}")

    myproduct2 = Prodotto(name="Mouse", price=10, quantity=25, supplier="CDE")
    print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

    print(f"Valore lordo myproduct1: {myproduct1.valore_lordo()}")
    Prodotto.aliquota_iva = 0.24  # aggiorno iva
    print(f"Valore lordo myproduct1: {myproduct1.valore_lordo()}")

    print(myproduct1.__str__())
    print(myproduct1.__repr__())

    p_b = Prodotto(name="Mouse", price=10, quantity=25, supplier="CDE")
    p_a = Prodotto(name="Laptop", price=1200, quantity=12, supplier="ABC")
    print("myproduct == p_a?", myproduct1 == p_a)  # implementa il metodo eq appena creato
    print("p_a==p_b?", p_a == p_b)

    mylist = [p_a, p_b, myproduct1]
    mylist.sort()  # ordinata con less than

    print("Lista ordinata")
    for p in mylist:
        print(p)

    my_prod_scontato = ProdottoScontato(name="Auricolari", price=320, quantity=1, supplier="ABC", sconto_percento=10)
    my_service = Servizio(name="Consulenza", tariffa_oraria=30, ore=10)

    mylist.append(my_service)
    mylist.append(my_prod_scontato)

    mylist.sort(reverse=True)

    for elem in mylist:
        print(elem.name, "->", elem.prezzo_finale())

    abb = Abbonamento(name="Software gestionale", prezzo_mensile=30.0, mesi=24)
    mylist.append(abb)
    for elem in mylist:
        print(elem.name, "->", elem.prezzo_finale())

    print(f"Il totale è : {calcola_totale(mylist)}")

if __name__ == "__main__":
    _test_modulo()