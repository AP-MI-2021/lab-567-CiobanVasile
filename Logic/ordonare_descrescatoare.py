from Domain.rezervare import get_pret

def ordonare_pret_descrescator(list, undo_list , redo_list):
    """
    Ordoneaza lista descrescator dupa pretul rezervarilor
    :param list: lista cu rezervari din baza de date
    :return: lista ordonata descrescator dupa pretul rezervarilor
    """
    undo_list.append(list)
    redo_list.clear()
    return sorted(list, reverse=True, key=get_pret)
