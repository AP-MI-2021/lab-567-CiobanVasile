def creeaza_rezervare(id_rezervare,nume,clasa,pret,checkin):
    '''
    Creeaza o rezervare
    :param lst_rezervari: o lista cu rezervarile
    :param id_rezervare:  id-ul rezervarii
    :param nume:          numele pe care este facuta rezervarea
    :param clasa:         clasa la care este facuta rezervarea
    :param pret:          pretul rezervarii
    :param checkin:       chekinul facut(DA/NU)
    :return:              rezervarea creata
    '''
    return {
            'id': id_rezervare,
            'nume': nume,
            'clasa': clasa,
            'pret': pret,
            'checkin': checkin,
        }

def get_id(rezervare):
    """
    TODO
    :param rezervare: rezervarea
    :return:          id-ul rezervarii
    """
    return rezervare['id']

def get_nume(rezervare):
    """
    TODO
    :param rezervare: rezervarea
    :return:          numele pe care este facuta rezervarea
    """
    return rezervare['nume']

def get_clasa(rezervare):
    """
    TODO
    :param rezervare: rezervarea
    :return:          clasa la care este facuta rezervarea
    """
    return rezervare['clasa']

def get_pret(rezervare):
    """
    TODO
    :param rezervare: rezervarea
    :return:          pretul rezervarii
    """
    return rezervare['pret']

def get_checking(rezervare):
    """
    TODO
    :param rezervare: rezervarea
    :return:          daca este sau nu facut checkinul
    """
    return rezervare['checkin']

def get_str(rezervare):
    """
    TODO
    :param rezervare: rezervarea
    :return:          detalii despre rezervare
    """
    return f'Rezervarea cu id-ul {get_id(rezervare)}, pe numele {get_nume(rezervare)}, la clasa {get_clasa(rezervare)}.'

