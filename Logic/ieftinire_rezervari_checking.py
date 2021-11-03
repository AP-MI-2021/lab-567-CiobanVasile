from Domain.rezervare import get_nume, get_clasa, creeaza_rezervare,get_id,get_checking,get_pret

def ieftinire_procentaj(lst_rezervari, procentaj):
    """
    :param lst_rezervari: lista cu rezervari
    :param procentaj: procentajul cu care se vor reduce rezervarile
    :return:      lista cu toate rezervarile care au checkinul facut cu reducerea pretului
    """
    if not (0 <= procentaj <= 100):
        raise ValueError('Procentajul trebuie sa fie intre 0 si 100 inclusiv.')

    result = []
    for rezervare in lst_rezervari:
        if get_checking(rezervare) == 'da':
            pret_nou = get_pret(rezervare) - (procentaj / 100) * get_pret(rezervare)
            result.append(creeaza_rezervare(
                get_id(rezervare),
                get_nume(rezervare),
                get_clasa(rezervare),
                pret_nou,
                get_checking(rezervare)
            ))
        else:
            result.append(rezervare)

    return result


