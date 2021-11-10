from Domain.rezervare import get_nume, creeaza_rezervare, get_clasa, get_id, get_pret, get_checkin


def Trecerea_Rezervarilor_La_Clasa_Superioara(nume, lista):
    '''
    Trece clasa rezervarile cu numele "nume" la o clasa superioara
    :param nume: Numele rezervarilor pentru care trebuie modificata clasa la o clasa superioara
    :param lista: Lista rezervarilor
    :return: Lista rezervarilor modificata
    '''
    new_list = []
    for rezervare in lista:
        if get_nume(rezervare) == nume:
            if get_clasa(rezervare) == "economy":
                rezervare_noua = creeaza_rezervare(
                    get_id(rezervare),
                    get_nume(rezervare),
                    "economy plus",
                    get_pret(rezervare),
                    get_checkin(rezervare)
                )
                new_list.append(rezervare_noua)
            elif get_clasa(rezervare) == "economy plus":
                rezervare_noua = creeaza_rezervare(
                    get_id(rezervare),
                    get_nume(rezervare),
                    "business",
                    get_pret(rezervare),
                    get_checkin(rezervare)
                )
                new_list.append(rezervare_noua)
            elif get_clasa(rezervare) == "business":
                rezervare_noua = creeaza_rezervare(
                    get_id(rezervare),
                    get_nume(rezervare),
                    get_clasa(rezervare),
                    get_pret(rezervare),
                    get_checkin(rezervare)
                )
                new_list.append(rezervare_noua)
        else:
             new_list.append(rezervare)
    return new_list
def Ieftinirea_Rezervarilor_Cu_Un_Procentaj(procent, lista):
    '''
    Rezervarile care au facut checkin-ul vor fi ieftinite cu un procentaj dat "procent"
    :param procent: procentul cu care vor fi ieftinite preturile rezervarilor - string
    :param lista: Lista rezervarilor
    :return: Lista rezervarilor modificata
    '''
    procentaj = procent[0: len(procent) - 1]
    numar = float(procentaj)
    new_list = []
    for rezervare in lista:
        if get_checkin(rezervare) == "Da":
            new_rezervare = creeaza_rezervare(
                get_id(rezervare),
                get_nume(rezervare),
                get_clasa(rezervare),
                get_pret(rezervare) - numar / 100 * get_pret(rezervare),
                get_checkin(rezervare)
            )
            new_list.append(new_rezervare)
        else:
            new_list.append(rezervare)
    return new_list


def pret_maxim_ficare_clasa(lista):
    '''
    Determina pretul maxim pentru fiecare clasa
    :param lista:Lista rezervarilor
    :return: Returneaza preturie maxime pentru fiecare clasa
    '''
    maxim_economy = -1
    maxim_economy_plus = -1
    maxim_business = -1
    for rezervare in lista:
        if get_clasa(rezervare) == "economy":
            if get_pret(rezervare) > maxim_economy:
                maxim_economy = get_pret(rezervare)
        elif get_clasa(rezervare) == "economy plus":
            if get_pret(rezervare) > maxim_economy_plus:
                maxim_economy_plus = get_pret(rezervare)
        elif get_clasa(rezervare) == "business":
            if get_pret(rezervare) > maxim_business:
                maxim_business = get_pret(rezervare)
    return "maxim_economy: {}, maxim_economy_plus: {}, maxim_business: {}".format(
        maxim_economy,
        maxim_economy_plus,
        maxim_business
    )
def ordonare_descrescatoare_pret(lista):
    '''
    Ordoneaza lista descrescator dupa pretul rezervarilor
    :param lista: Lista rezervarilor
    :return: Lista ordonata descrescator dupa pretul rezervarilor
    '''
    new_list = sorted(lista, key = lambda i: get_pret(i), reverse = True)
    return new_list

def adaugare_in_lista_nume(lista_nume, lista):
    '''
    Introduce intr-o lista noua numele din lista veche. Acestea vor aparea doar o singura data
    :param lista_nume: lista numelor rezervarilor din lista "lista"
    :param lista: Lista rezervarilor
    :return:
    '''
    for rezervare in lista:
        if get_nume(rezervare) not in lista_nume:
            lista_nume.append(get_nume(rezervare))
    return lista_nume


def suma_preturi_nume(Nume, lista):
    '''
    Aceasta functie face suma preturilor unei rezervari cu numele "Nume"
    :param Nume: Numele rezervarii pentru care trebuie facuta suma - string
    :param lista: Lista rezervarilor
    :return: Returneaza suma preturilor rezervarilor cu numele "Nume"
    '''
    suma = 0
    for rezervare in lista:
        if get_nume(rezervare) == Nume:
            suma = suma + get_pret(rezervare)
    return suma
def sume_preturi_fiecare_nume(lista_nume, lista):
    '''
    Aceasta functie returneaza sumele prețurilor pentru fiecare nume
    :param lista_nume: Lista numelor din lista rezervarilor
    :param lista: Lista rezervarilor
    :return: Returneaza sumele prețurilor pentru fiecare nume
    '''
    lista_sume = []
    for rezervare_nume in lista_nume:
        lista_sume.append(suma_preturi_nume(rezervare_nume, lista))
    return lista_sume

def undo(lista, undo_operations, redo_operations):
    '''
    Afiseaza lista anterioara modificarii efectuate
    :param lista: lista rezervarilor
    :param undo_operations: operatiile de undo (functionalitati)
    :param redo_operations: operatiile de redo (functionalitati)
    :return: Returneaza lista in urma unui Undo
    '''
    operations = undo_operations.pop()
    redo_operations.append(operations)
    lista = operations[0]()
    return lista

def redo(lista, undo_operations, redo_operations):
    '''
    Doar daca s-a facut undo se poate aplica redo-ul
    Afiseaza lista modificata
    :param lista: lista rezervarilor
    :param undo_operations: operatiile de undo (functionalitati)
    :param redo_operations: operatiile de redo (functionalitati)
    :return: Returneaza lista in urma unui Redo
    '''
    operations = redo_operations.pop()
    undo_operations.append(operations)
    lista = operations[1]()
    return lista