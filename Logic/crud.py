from Domain.rezervare import creeaza_rezervare, get_id

def inverse_create(lst_rezervari, id_rezervare):
    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != id_rezervare:
            new_rezervari.append(rezervare)
    return new_rezervari

def create(lst_rezervari,
        id_rezervare: int, nume, clasa, pret, checkin, undo_list, redo_list):
    """
    :param lst_rezervari: o lista cu rezervarile
    :param id_rezervare:  id-ul rezervarii
    :param nume:          numele pe care este facuta rezervarea
    :param clasa:         clasa la care este facuta rezervarea
    :param pret:          pretul rezervarii
    :param checkin:       chekinul facut(DA/NU)
    :return:              lista initiala plus rezervarea creata
    """
    if read(lst_rezervari, id_rezervare) is not None:
        raise ValueError(f'Exista deja o rezervare cu id-ul {id_rezervare}')

    rezervare = creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin)

    undo_list.append(lst_rezervari)
    redo_list.clear()

    return lst_rezervari + [rezervare]

def read(lst_rezervari, id_rezervare: int=None):
    """
    :param lst_rezervari: lista de rezervari
    :param id_rezervare:  id-ul rezervarii dorite
    :return:              rezervarea cu id-ul citit, respectiv toata lista daca nu exista id-ul citit
    """
    if not id_rezervare:
        return lst_rezervari

    rezervare_cu_id = None
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_rezervare:
            rezervare_cu_id = rezervare

    if rezervare_cu_id:
        return rezervare_cu_id
    return None

def update(lst_rezervari, new_rezervare, undo_list, redo_list):
    """
    :param lst_rezervari:  lista initiala de rezervari
    :param new_rezervare:  rezervarea pe care vrem sa o modificam
    :return:               o lista nou cu rezervarea modificata
    """

    if read(lst_rezervari, get_id(new_rezervare)) is None:
        raise ValueError(f'Nu exista o rezervare cu id-ul {get_id(new_rezervare)} pe care sa o actualizam.')

    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != get_id(new_rezervare):
            new_rezervari.append(rezervare)
        else:
            new_rezervari.append(new_rezervare)

    undo_list.append(lst_rezervari)
    redo_list.clear()

    return new_rezervari

def delete(lst_rezervari, id_rezervare: int, undo_list, redo_list):
    """

    :param lst_rezervari:   lista initiala de rezervari
    :param id_rezervare:    id-ul rezervarii pe care vrem sa o stergem
    :return:                lista initiala de rezervari fara rezervarea cu id-ul citit
    """

    if read(lst_rezervari, id_rezervare) is None:
        raise ValueError(f'Nu exista o rezervare cu id-ul {id_rezervare} pe care sa o stergem.')

    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != id_rezervare:
            new_rezervari.append(rezervare)

    undo_list.append(lst_rezervari)
    redo_list.clear()

    return new_rezervari

def get_by_id(id_rezervare: int, lst_rezervare):
    '''
    Returneaza rezervarea cu id-ul dat ca parametru
    :param id_rezervare:
    :param lst_rezervare:
    :return:
    '''
    for rezervare in lst_rezervare:
        if get_id(rezervare) == id_rezervare:
            return rezervare
    return None