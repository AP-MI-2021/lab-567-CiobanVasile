def creeaza_rezervare(id_rezervare,nume,clasa,pret,checkin):
    '''
    Creeaza o rezervare
    :param id_rezervare:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :return:
    '''
    return {
            'id': id_rezervare,
            'nume': nume,
            'clasa': clasa,
            'pret': pret,
            'checkin': checkin,
        }

def get_id(rezervare):
    return rezervare['id']

def get_nume(rezervare):
    return rezervare['nume']

def get_clasa(rezervare):
    return rezervare['clasa']

def get_pret(rezervare):
    return rezervare['pret']

def get_checking(rezervare):
    return rezervare['checkin']

def get_str(rezervare):
    return f'Rezervarea cu id-ul {get_id(rezervare)}, pe numele {get_nume(rezervare)}, la clasa {get_clasa(rezervare)}.'

