def aggiungi_studente(lista,nome,cognome):
    try:
        lista.append(nome,cognome)
    except TypeError as e:
        print(f"TypeError occured: {str(e)}. All arguments must be passed to this function in str format")