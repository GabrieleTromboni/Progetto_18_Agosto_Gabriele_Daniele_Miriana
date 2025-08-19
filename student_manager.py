from utils.functions import aggiungi_studente, ordina_studenti, cerca_per_nome
from utils.students import listaGabriele, listaMiriana, listaDaniele
from typing import List, Tuple

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

    def sort_lists(
            self,
            liste: List[str]
        ) -> bool:
        try:
            for lista in liste:
                if lista not in self.liste:
                    print(f"Lista {lista} non trovata, cambia il nome della lista.")
                else:
                    sorted_list = ordina_studenti(lista)
                    print(f"Lista {lista} ordinata.")
                print(sorted_list)
            return True
        except Exception as e:
            print(f"Errore durante l'ordinamento degli studenti: {e}")
    
    def search_students(
            self,
            liste:  List[str],
            studenti: List[str]
        ) -> bool:

        try:
            for lista in liste:
                if lista not in self.liste:
                    print(f"Lista {lista} non trovata, cambia il nome della lista.")
                else:
                    for studente in studenti:
                        if isinstance(studente, str):
                            cerca_per_nome(lista, studente)
                        else:
                            print(f"Studente {studente} non valido. Deve essere una stringa.")
            return True
        except Exception as e:
            print(f"Errore durante la ricerca dello studente: {e}")
        return False
        