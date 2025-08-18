from operator import itemgetter

def aggiungi_studente(lista,nome,cognome):
    try:
        lista.append(nome,cognome)
    except Exception as e:
        raise TypeError
    
def ordina_studenti(lista):
    return sorted(lista, key=itemgetter(1,0))
