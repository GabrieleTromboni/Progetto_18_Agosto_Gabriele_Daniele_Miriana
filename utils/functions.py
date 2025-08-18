def aggiungi_studente(lista,nome,cognome):
    try:
        lista.append(nome,cognome)
    except Exception as e:
        raise TypeError