from Domain.rezervare import creeaza_rezervare, get_id

def get_by_Nume(nume, lista):
    '''
    Cauta daca exista o rezerare cu numele "nume" in lista de rezervari
    :param nume: Numele rezervarii pe care o cautam
    :param lista: Lista rezervarilor
    :return: Returneaza rezervarea daca aceasta a fost gasita in lista sau None in caz contrar
    '''
    for rezervare in lista:
        if rezervare[1] == nume:
            return rezervare
    return None


def get_by_id(id, lista):
    '''
    Cauta daca exista o rezervare cu id-ul "id" in lista de rezervari
    :param id: id-ul rezervarii pe care o cautam - string
    :param lista: Lista rezervarilor
    :return: Returneaza rezervarea daca rezervarea cu ID-ul "ID" a fost gasita in lista, respectiv None in caz contrar
    '''
    for rezervare in lista:
        if rezervare[0] == id:
            return rezervare
    return None


def adauga_rezervare(id, nume, clasa, pret, checkin, lista): #create
    '''
    Aceasta functie adauga o rezervare noua intr-o lista
    :param id: id-ul rezervarii- string
    :param nume: Numele rezervarii - string
    :param clasa: Clasa rezervarii (economy, economy plus, business) - string
    :param pret: Pretul rezervarii - float
    :param checkin: Checkin rezervare (Da sau Nu) - string
    :param lista: Lista rezervarilor
    :return: Returneaza lista veche + rezervarea noua
    '''
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    new_rezervare = creeaza_rezervare(id, nume, clasa, pret, checkin)
    return lista + [new_rezervare]

def delete_rezervare(id, lista):
    '''
    Sterge o rezervare din lista dupa id
    :param id: id-ul rezervarii pe care dorim sa o stergem
    :param lista: Lista rezervarilor
    :return: Returneaza o lista noua in care rezervarea cu ID-ul "ID" nu mai exista
    '''
    return [rezervare for rezervare in lista if get_id(rezervare) != id]
def update_rezervare(id, nume, clasa, pret, checkin, lista):
    '''
    Modifica o rezervare din lista dupa id
    :param id: id-ul rezervarii- string
    :param nume: Numele nou al rezervarii - string
    :param clasa: Clasa noua a rezervarii (economy, economy plus, business) - string
    :param pret: Pretul nou al rezervarii - float
    :param checkin: Checkin-ul nou al rezervarii (Da sau Nu) - string
    :return:
    '''
    new_list = []
    for rezervare in lista:
        if get_id(rezervare) == id:
            rezervare_noua = creeaza_rezervare(id, nume, clasa, pret, checkin)
            new_list.append(rezervare_noua)
        else:
            new_list.append(rezervare)
    return new_list