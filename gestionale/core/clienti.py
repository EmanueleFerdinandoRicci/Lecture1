# Scrivere una classe Cliente che abbia i campi "nome","email","categoria"("Gold","Silver","Bronze"),
# vorremo che questa classe avesse un metodo che chiamiamo "descrizione"
# che deve restituire una stringa formattata ad esempio
# "Cliente Fulvio Bianchi (Gold) - fulvio@google.com"


#si modifichi la classe cliente in maniera che la categoria sia protetta
#e accetti solo Gold,Silver,Bronze
categorie_valide = {"Gold", "Silver", "Bronze"}

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
        if stringa not in categorie_valide:
            raise ValueError("Attenzione, categoria non valida. Scegliere tra Gold, Silver e Bronze")
        self._categoria = stringa

from dataclasses import dataclass
@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria: str
    
def _test_modulo():
    myclient1 = Cliente(nome="Fulvio Bianchi", email="fulvio@google.com", categoria="Gold")
    print(myclient1.descrizione())
    #myclient2 = Cliente(nome="Carlo Masone", email="carlomasone@google.com", categoria="Platinum")
    #print(myclient2.descrizione())

if __name__ == "__main__":
    _test_modulo()