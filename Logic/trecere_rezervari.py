from Domain.rezervare import get_nume, get_clasa, creeaza_rezervare,get_id,get_checking,get_pret

def trecere_rezervari_nume_clasa_superioara(lst_rezervari, nume, undo_list, redo_list):
    """
    :param lst_rezervari: lista cu rezervari din baza de date
    :param nume:          numele la care vrem sa treceme rezervarile la o clasa superioara
    :return:              lista cu rezervari cu clasele schimbate
    """

    result = []
    for rezervare in lst_rezervari:
        if get_nume(rezervare) == nume:
            if get_clasa(rezervare) == 'economy':
                result.append(creeaza_rezervare(
                    get_id(rezervare),
                    get_nume(rezervare),
                    'economy plus',
                    get_pret(rezervare),
                    get_checking(rezervare)
                ))
            elif get_clasa(rezervare) == 'economy plus':
                result.append(creeaza_rezervare(
                    get_id(rezervare),
                    get_nume(rezervare),
                    'business',
                    get_pret(rezervare),
                    get_checking(rezervare)
                ))
        else:
            result.append(rezervare)

    undo_list.append(lst_rezervari)
    redo_list.clear()
    return result
