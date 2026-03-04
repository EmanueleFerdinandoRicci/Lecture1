#nel package gestionale scriviamo un modulo fatture.py che contenga:
#-una classe Fattura che contiene un Ordine, un numero fattura e una data
#-un metodo genera_fattura() che restituisce una stringa formattata con info
from gestionale.core.clienti import Cliente
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine
from dataclasses import dataclass
from datetime import date

@dataclass
class Fattura:
    ordine : Ordine
    numero_di_fattura: str
    data: date

    def genera_fattura(self):
        linee = [
            f"="*60,
            #intestazione con data e numero
            f"Fattura no. {self.numero_di_fattura} del {self.data}",
            f"="*60,
            #dettahli cliente
            f"Cliente: {self.ordine.cliente.nome}",
            f"Categoria: {self.ordine.cliente.categoria}",
            f"Mail: {self.ordine.cliente.email}",
            f"-"*60,
            f"DETTAGLIO ORDINE"
        ]
        for i, riga in enumerate(self.ordine.righe):
            linee.append(
                f"{i}"
                f"{riga.prodotto.name}"
                f"Qta. {riga.quantita} X {riga.prodotto.prezzo_unitario} = "
                f"Tot. {riga.totale_riga()}"
            )
        linee.extend(
            [
            f"-" * 60,
            f"Totale netto: {self.ordine.totale_netto()}",
            f"IVA(22%): {self.ordine.totale_netto()*0.22}",
            f"Totale lordo: {self.ordine.totale_lordo(0.22) }",
            f"="*60
            ]
        )

        return "\n".join(linee)

def _test_modulo():

    p1 = ProdottoRecord("Laptop",1200.0)
    p2 = ProdottoRecord("Mousse",20.0)
    p3 = ProdottoRecord("Tablet",600.0)

    cliente = Cliente("Mario Bianchi", "mariobia@gmail.com","Gold")

    ordine = Ordine([RigaOrdine(p1,1),RigaOrdine(p2,5), RigaOrdine(p3,2)], cliente)

    fattura = Fattura(ordine= ordine, numero_di_fattura = "2026/01", data = date.today())
    print(fattura.genera_fattura())

if __name__ == "__main__":
    _test_modulo()