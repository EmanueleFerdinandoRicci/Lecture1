import flet as ft

from gestionale.gestoreOrdini import GestoreOrdini


class Controller:
    def __init__(self,v):
        self._model = GestoreOrdini()
        self._view = v

    def add_ordine(self,e):
        #PRODOTTO
        nomePstr = self._view._txtInNomeP.value
        if nomePstr == "":
            self._view._lvOut.controls.append(
                ft.Text (value = "Il campo nome prodotto non può esser vuoto")
            )
            self._view.update_page()
            return

        try:
            prezzoP = float(self._view._txtInPrezzo.value)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text (value="Attenzione! Il prezzo deve essere un numero",color="red"))
            self._view.update_page()
            return

        try:
            quantitaP = int(self._view._txtInQuantita.value)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text (value="Attenzione! La quantità deve essere un numero",color="red"))
            self._view.update_page()
            return

        #CLIENTE
        nomeC = self._view._txtInNomeC.value
        if nomeC == "":
            self._view._lvOut.controls.append(
                ft.Text (value = "Il campo nome cliente non può esser vuoto")
            )
            self._view.update_page()
            return

        mail = self._view._txtInMail.value
        if mail == "":
            self._view._lvOut.controls.append(
                ft.Text (value = "Il campo mail cliente non può esser vuoto")
            )
            self._view.update_page()
            return

        categoria = self._view._txtInCategoria.value
        if categoria == "":
            self._view._lvOut.controls.append(
                ft.Text (value = "Il campo categoria non può esser vuoto")
            )
            self._view.update_page()
            return
        
        ordine = self._model.crea_ordine(nomePstr,prezzoP,quantitaP, nomeC,mail,categoria)
        self._model.add_ordine(ordine)

        self._view._txtInNomeP.value = ""
        self._view._txtInPrezzo.value = ""
        self._view._txtInQuantita.value = ""
        self._view._txtInNomeC.value = ""
        self._view._txtInMail.value = ""
        self._view._txtInCategoria.value = ""

        self._view._lvOut.controls.append(
            ft.Text (value= "Ordine Correttamente Eseguito",
                       color = "green")
        )
        self._view._lvOut.controls.append(
            ft.Text(value = "Dettagli Ordine",
                    color = "green")
        )
        self._view._lvOut.controls.append(
            ft.Text(ordine.riepilogo())
        )
        self._view._lvOut.controls.append(
            ft.Text("\n")
        )
        self._view.update_page()


    def gestisci_ordine(self,e):
        self._view._lvOut.controls.clear()
        res, ordine = self._model.processa_prossimo_ordine()
        if res:
            self._view._lvOut.controls.append(
                ft.Text (value = "Ordine Correttamente Eseguito",color="green")
            )
            self._view._lvOut.controls.append(
                ft.Text(ordine.riepilogo())
            )
            self._view.update_page()
        else:
            self._view._lvOut.controls.append(
                ft.Text (value = "Non ci sono ordini in coda",color="blue")
            )
            self._view.update_page()

    def gestisci_all_ordini(self,e):
        self._view._lvOut.controls.clear()
        ordini = self._model.processa_tutti_ordini()

        if not ordini:
            self._view._lvOut.controls.append(
                ft.Text (value = "Non ci sono ordini in coda",color="blue")
            )
            self._view.update_page()
        else:
            self._view._lvOut.controls.append(
                ft.Text (value = f"Ho processato correttamente {len(ordini)} ordini",color="green")
            )
            for o in ordini:
                self._view._lvOut.controls.append(
                    ft.Text("\n")
                )
                self._view._lvOut.controls.append(
                    ft.Text (o.riepilogo())
                )
            self._view.update_page()

    def stampa_sommario(self,e):
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(
            ft.Text (value = "DI seguito la stampa del sommario delle attività del business",color="orange")
        )
        self._view._lvOut.controls.append(
            ft.Text(self._model.get_riepilogo())
        )
        self._view.update_page()