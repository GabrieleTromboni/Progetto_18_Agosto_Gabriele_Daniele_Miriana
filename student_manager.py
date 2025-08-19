from utils.functions import aggiungi_studente, ordina_studenti, cerca_per_nome
from utils.students import listaGabriele, listaMiriana, listaDaniele
from typing import Optional, List, Tuple

class StudentManager:
    def __init__(self):
        self.liste = [listaGabriele, listaMiriana, listaDaniele]

    def manage_add_student(
            self,
            liste: List[str],
            studenti: List[Tuple[str,str]]
        ) -> bool:

        try:
            for lista in liste:
                if lista not in self.liste:
                    print(f"Lista {lista} non trovata, cambia il nome della lista.")
                else:
                    for studente in studenti:
                        if isinstance(studente, tuple) and len(studente) == 2:
                            nome, cognome = studente
                            if isinstance(nome, str) and isinstance(cognome, str):
                                aggiungi_studente(lista, nome, cognome)
                            else:
                                print(f"Studente {studente} non valido. Deve essere una tupla di due stringhe.")
            return True
        except Exception as e:
            print(f"Errore durante l'aggiunta dello studente: {e}")
        return False

    def ordina_studenti(self):
        self.lista_studenti.sort(key=lambda x: (x["cognome"], x["nome"]))

    def cerca_per_nome(self, nome):
        risultati = [s for s in self.lista_studenti if s["nome"].lower() == nome.lower()]
        return risultati