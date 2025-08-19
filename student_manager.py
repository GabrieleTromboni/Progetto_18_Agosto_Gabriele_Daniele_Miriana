'''
Questo è lo script principale per lo svolgimento dell'esercitazione di gruppo del 18 Agosto durante l'AI Academy.
Deve essere chiamato da terminale e svolgerà le seguenti funzionalità:
    - aggiunge uno studente ad una lista già esistente.
    - ordina una lista esistente in ordine alfabetico. Se il cognome corrisponde, ordinerà in base al nome.
'''

from utils.functions import aggiungi_studente, ordina_studenti, cerca_per_nome
import utils.students as students


def stampa_menu():
    """Stampa il menu principale dell'applicazione"""
    print("\n")
    print(" SISTEMA DI GESTIONE STUDENTI")
    print("1.  Visualizza tutti gli studenti")
    print("2.  Aggiungi nuovo studente")  
    print("3.  Ordina studenti alfabeticamente")
    print("4.  Cerca studente per nome")
    print("5.  Esci")

def ottieni_scelta_menu():
    """
    Ottiene e valida la scelta dell'utente dal menu
    
    Returns:
        int: Scelta valida dell'utente (1-5)
    """
    while True:
        try:
            scelta = input("\n Inserisci la tua scelta (1-5): ").strip()
            if scelta in ['1', '2', '3', '4', '5']:
                return int(scelta)
            else:
                print("Scelta non valida. Inserisci un numero tra 1 e 5.")
        except ValueError:
            print("Input non valido. Inserisci un numero.")
        except KeyboardInterrupt:
            print("\n\nArrivederci!")
            return 5
        
def gestisci_aggiunta_studente(lista_studenti):
    """
    Gestisce l'aggiunta di un nuovo studente
    
    Args:
        lista_studenti (list): Lista degli studenti
    """
    print("\nAGGIUNGI NUOVO STUDENTE")
    print("-" * 30)
    
    try:
        nome = input("Nome: ").strip()
        if not nome:
            print("Il nome non può essere vuoto.")
            return
        
        cognome = input(" Cognome: ").strip()
        if not cognome:
            print("Il cognome non può essere vuoto.")
            return
        
        if aggiungi_studente(lista_studenti, nome, cognome):
            print(f"Studente {nome.title()} {cognome.title()} aggiunto con successo!")
        else:
            print(f"Lo studente {nome.title()} {cognome.title()} esiste già nella lista.")
            
    except KeyboardInterrupt:
        print("\nOperazione annullata.")