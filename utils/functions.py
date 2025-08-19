'''
Questo script raccoglie le varie funzioni da richiamare nello script 'student_manager.py'.
Abbiamo tre differenti funzioni:
    - aggiungi_studente: permette di aggiungere uno studente nel formato (Nome, Cognome) ad una lista presente nel database 'students.py'.
    - ordina_studenti: permette di ordinare gli studenti presenti nella lista in ordine alfabetico con priorità al cognome.
    - cerca_per_nome: permette la ricerca di una qualsiasi stringa data all'interno dei vari nomi degli studenti presenti in uan specifica lista.
'''

from operator import itemgetter
from typing import List

# FUNZIONI
def aggiungi_studente(
        lista: str,
        nome: str,
        cognome: str
    ) -> bool:
    '''
    La funzione aggiunge uno studente ad una lista già presente.
    Gli argomenti devono essere tutti nel formato str, sia il nome della lista, nome e cognome dello studente.

    Args:
        lista (str): nome della lista in cui aggiungere lo studente.
        nome (str): nome dello studente da aggiungere alla lista.
        cognome (str): cognome dello studente da aggiungere alla lista.

    Returns:
        bool: se lo studente è stato aggiunto (True) oppure no (False)
    '''
    
    try:
        # appendere alla lista esistente la tupla (nome, cognome) dello studente
        lista.append(nome,cognome)
    except TypeError as e:
        print(f"TypeError occured: {str(e)}. All arguments must be passed to this function in str format")


def ordina_studenti(lista: str) -> List:
    '''
    Questa funzione permette di ordinare gli studenti presenti in una lista già esistente, 
    sia prima che dopo aver aggiunto uno o più studenti alla stessa lista o a varie liste.
    
    Args:
        lista (str): Nome della lista esistente da oridnare.
        
    Returns:
        lista ordinata in ordine alfabetico.
    '''

    try:
        # ordinare la lista di tuple dando priorità al cognome dello studente
        return sorted(lista, key=itemgetter(1,0))
    except TypeError as e:
        print(f"TypeError occured: {str(e)}. All arguments must be passed to this function in str format")

def cerca_per_nome(
        lista: str, 
        stringa: str
    ) -> tuple:
    '''
    La funzione permette di cercare un qualsiasi studente nella lista esistente chiamata.
    Se la stringa da cercare è un nome completo o incompleto, non cambia nulla
    e avremo in output una tupla che ci indica che la ricerca è andata a buon fine (True)
    associando la lista dei vari nomi di studenti trovati in cui la stringa è presente.
    
    Args:
        lista (str): Nome della lista in cui ricercare la stringa.
        stringa (str): stringa da ricercare nella lista esistente.
        
    Returns:
        tuple or bool in base al successo o non successo della ricerca.
    '''

    try:
        # ricerchiamo la stringa passata in ogni nome di tutti gli studenti presenti nella lista esistente richiamata
        # lista di tuple (nome, cognome) derivanti dalla lista esistente selezionate SE la stringa è presente nel nome!
        studenti = [(nome,cognome) for nome, cognome in lista if stringa.lower() in nome.lower()]
        # ritorna tupla sia per il successo che per l'insuccesso della ricerca
        return (True, studenti) if studenti else (False, [])
    except TypeError as e:
        print(f"TypeError occured: {str(e)}. All arguments must be passed to this function in str format")