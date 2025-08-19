from operator import itemgetter


'''
Questo script raccoglie le varie funzioni da richiamare nello script 'student_manager.py'.
Abbiamo tre differenti funzioni:
    - aggiungi_studente: permette di aggiungere uno studente nel formato (Nome, Cognome) ad una lista presente nel database 'students.py'.
    - ordina_studenti: permette di ordinare gli studenti presenti nella lista in ordine alfabetico.
    - cerca_per_nome: 
'''

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
        lista.append(nome,cognome)
    except TypeError as e:
        print(f"TypeError occured: {str(e)}. All arguments must be passed to this function in str format")


def ordina_studenti(lista):
    return sorted(lista, key=itemgetter(1,0))

def cerca_per_nome(lista, stringa):
    studenti = [(nome,cognome) for nome, cognome in lista if stringa.lower() in nome.lower()]
    return (True, studenti) if studenti else False