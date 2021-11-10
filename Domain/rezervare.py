def creeaza_rezervare(id, nume, clasa, pret, checkin):
    '''
    Aceasta funtie creeaza o rezervare
    :param id: ID-ul rezervarii- string
    :param nume: Numele rezervarii - string
    :param clasa: Clasa rezervarii (economy, economy plus, business) - string
    :param pret: Pretul rezervarii - float
    :param checkin: Checkin rezervare (Da sau Nu) - string
    :return: Returneaza un o lista ce retine o rezervare
    '''
    return (
        id,
        nume,
        clasa,
        pret,
        checkin
    )

def get_id(rezervare):
    '''
    Aceasta functie da ID-ul unei rezervari
    :param rezervare: un tuple de tip rezervare
    :return: Returneaza ID-ul unei rezervari - string
    '''
    return rezervare[0]
def get_nume(rezervare):
    '''
    Aceasta functie da numele persoanei care a facut rezervarea
    :param rezervare: un tuple de tip rezervare
    :return: Returneaza numele presoanei care a facut rezervarea
    '''
    return rezervare[1]
def get_clasa(rezervare):
    '''
    Aceasta functie da clasa unei rezervari
    :param rezervare: un tuple de tip rezervare
    :return: Returneaza clasa unei rezervari
    '''
    return rezervare[2]
def get_pret(rezervare):
    '''
    Aceasta functie da pretul unei rezervari
    :param rezervare: un tuple de tip rezervare
    :return: Returneaza pretul unei rezervari
    '''
    return rezervare[3]
def get_checkin(rezervare):
    '''
    Aceasta functie da checkin-ul unei rezervari
    :param rezervare: un tuple de tip rezervare
    :return: Returneaza checkin-ul unei rezervari
    '''
    return rezervare[4]
def to_string(rezervare):
    '''
    :param rezervare: un tuple de tip rezervare
    :return:
    '''
    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        get_id(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare)
    )