def creeaza_rezervare(id_rezervare,nume,clasa,pret,checkin):
    '''
    Creeaza o rezervare
    :param id_rezervare:  id-ul rezervarii
    :param nume:          numele pe care este facuta rezervarea
    :param clasa:         clasa la care este facuta rezervarea
    :param pret:          pretul rezervarii
    :param checkin:       chekinul facut(DA/NU)
    :return:              rezervarea creata

    return {
            'id': id_rezervare,
            'nume': nume,
            'clasa': clasa,
            'pret': pret,
            'checkin': checkin,
        }
    '''
    return [
        id_rezervare,
        nume,
        clasa,
        pret,
        checkin,
    ]
def get_id(rezervare):
    """
    :param rezervare: rezervarea
    :return:          id-ul rezervarii
    """
    #return rezervare['id']
    return rezervare[0]

def get_nume(rezervare):
    """
    :param rezervare: rezervarea
    :return:          numele pe care este facuta rezervarea
    """
    #return rezervare['nume']
    return rezervare[1]

def get_clasa(rezervare):
    """
    :param rezervare: rezervarea
    :return:          clasa la care este facuta rezervarea
    """
    #return rezervare['clasa']
    return rezervare[2]

def get_pret(rezervare):
    """
    :param rezervare: rezervarea
    :return:          pretul rezervarii
    """
    #return rezervare['pret']
    return rezervare[3]

def get_checking(rezervare):
    """

    :param rezervare: rezervarea
    :return:          daca este sau nu facut checkinul
    """
    #return rezervare['checkin']
    return rezervare[4]

def get_str(rezervare):
    """

    :param rezervare: rezervarea
    :return:          detalii despre rezervare
    """
    return f'Rezervarea cu id-ul {get_id(rezervare)}, pe numele {get_nume(rezervare)}, la clasa {get_clasa(rezervare)}.'

