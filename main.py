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


# Scrivere una classe Cliente che abbia i campi "nome","email","categoria"("Gold","Silver","Bronze"),
# vorremo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad esempio
# "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"


#si modifichi la classe cliente in maniera che la categoria sia protetta
#e accetti solo Gold,Silver,Bronze

class Cliente:
    def __init__(self, nome: str, email: str, categoria: str):
        self.nome = nome
        self.email = email
        self._categoria = None
        self.categoria = categoria

    def descrizione(self):
        return f"Cliente {self.nome} ({self.categoria}) - {self.email}"

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, stringa):
        categorieValide = {"Gold", "Silver", "Bronze"}
        if stringa not in categorieValide:
            raise ValueError("Attenzione, categoria non valida. Scegliere tra Gold, Silver e Bronze")
        self._categoria = stringa


myproduct1 = Prodotto(name="Laptop", price=1200, quantity=12, supplier="ABC")  # su PyCharm si usa: invece che =
print(f"Nome prodotto: {myproduct1.name} - prezzo: {myproduct1.price}")

print(f"Il valore totale del prod1 è {myproduct1.valore_lordo()}")  # funzione di istanza
p3 = Prodotto.costruttore_con_quantita_1(name="Auricolari", price=200.0, supplier="ABC")
print(f"Prezzo scontato di prod1 {Prodotto.applica_sconto(myproduct1.price, percentuale=0.15)}")

myproduct2 = Prodotto(name="Mouse", price=10, quantity=25, supplier="CDE")
print(f"Nome prodotto: {myproduct2.name} - prezzo: {myproduct2.price}")

myclient1 = Cliente(nome="Fulvio Bianchi", email="fulvio@google.com", categoria="Gold")
print(myclient1.descrizione())

print(f"Valore lordo myproduct1: {myproduct1.valore_lordo()}")
Prodotto.aliquota_iva = 0.24 #aggiorno iva
print(f"Valore lordo myproduct1: {myproduct1.valore_lordo()}")

myclient2 = Cliente(nome="Carlo Masone", email="carlomasone@google.com", categoria="Platinum")
print(myclient2.descrizione())
