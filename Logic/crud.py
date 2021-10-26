from Domain.rezervare import creeaza_rezervare,get_id
def create(lst_rezervari,
        id_rezervare: int, nume, clasa, pret, checkin):
    """
    TODO
    :param lst_rezervari:
    :param id_rezervare:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :return:
    """

    rezervare = creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin)

    return lst_rezervari + [rezervare]

def read(lst_rezervari, id_rezervare: int=None):
    """

    :param lst_rezervari: lista de rezervari
    :param id_rezervare: id-ul rezervarii dorite
    :return:
    """
    rezervare_cu_id = None
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_rezervare:
            rezervare_cu_id = rezervare

    if rezervare_cu_id:
        return rezervare_cu_id
    return lst_rezervari

def update(lst_rezervari, new_rezervare):
    """
    TODO
    :param lst_rezervari:
    :param new_rezervare:
    :return:
    """
    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != get_id(new_rezervare):
            new_rezervari.append(rezervare)
        else:
            new_rezervari.append(new_rezervare)
    return new_rezervari

def delete(lst_rezervari, id_rezervare: int):
    """
    TODO
    :param lst_rezervari:
    :param id_rezervare:
    :return:
    """
    new_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != id_rezervare:
            new_rezervari.append(rezervare)

    return new_rezervari
