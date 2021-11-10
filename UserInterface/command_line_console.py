from Logic.crud import adauga_rezervare, delete_rezervare, update_rezervare, get_by_id
from UserInterface.console import show_all


def read_in_line():
    '''
    Citire lista in linie
    La parametrul "; " gasit se va sparge lista si vor fi create doua liste separate
    La parametrul ", " gasit se va sparge lista, astfel incat lista noastra va fi parcursa cuvant cu cuvant
    :return:
    '''
    lista_mare = []
    lista_mica = []
    print("Separatori de comenzi: '; '")
    print("Separatori de cuvinte: ', '")
    print("Nu uitati sa puneti spatiu dupa fiecare separator!")
    sir = input("Dati niste comenzi din lista {Adauga, Sterge, Modifica, ShowAll}: ")
    lista = sir.split('; ')
    for index in lista:
        cuvant = index.split(', ')
        lista_mica = []
        for y in range(len(cuvant)):
            lista_mica.append(cuvant[y])
        lista_mare.append(lista_mica)
    return lista_mare


def ui_adauga_rezervare(lista, lista_mea):
    '''
    Adauga o rezervare in lista noastra
    :param lista: lista de rezervari
    :param lista_mea: lista care contine rezervarea mea curenta care trebuie adaugata in lista de rezervari
    :return:
    '''
    try:
        ID = lista_mea[0]
        nume = lista_mea[1]
        clasa = lista_mea[2]
        if clasa != "economy" and clasa != "economy plus" and clasa != "business":
            print("Nu ati introdus o clasa existenta!!!")
            return lista
        checkin = lista_mea[4]
        if checkin != "Da" and checkin != "Nu":
            print("Nu ati introdus Da sau Nu")
            return lista
        pret = float(lista_mea[3])
        return adauga_rezervare(lista_mea[0], lista_mea[1], lista_mea[2], float(lista_mea[3]), lista_mea[4], lista)
    except IndexError as ve:
        print("Eroare: {}".format(ve))
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_sterge_rezervare(lista, lista_mea):
    '''
    Sterge o rezervare in lista noastra
    :param lista: lista de rezervari
    :param lista_mea: lista care contine rezervarea mea curenta care trebuie adaugata in lista de rezervari
    :return:
    '''
    try:
        id = lista_mea[0]
        if get_by_id(id, lista) is None:
            print("Id-ul nu exista!")
            return lista
        else:
            return delete_rezervare(lista_mea[0], lista)
    except IndexError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_update_rezervare(lista, lista_mea):
    '''
    Modifica o rezervare in lista noastra
    :param lista: lista de rezervari
    :param lista_mea: lista care contine rezervarea mea curenta care trebuie adaugata in lista de rezervari
    :return:
    '''
    try:
        ID = lista_mea[0]
        nume = lista_mea[1]
        clasa = lista_mea[2]
        if clasa != "economy" and clasa != "economy plus" and clasa != "business":
            print("Nu ati introdus o clasa existenta!!!")
            return lista
        checkin = lista_mea[4]
        if checkin != "Da" and checkin != "Nu":
            print("Nu ati introdus Da sau Nu")
            return lista
        pret = float(lista_mea[3])
        return update_rezervare(lista_mea[0], lista_mea[1], lista_mea[2], float(lista_mea[3]), lista_mea[4], lista)
    except IndexError as ve:
        print("Eroare: {}".format(ve))
        return lista
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def run_menu_nou(lista_rezervari):
    lista_lista = read_in_line()
    lista_comenzi = ["Adauga", "Sterge", "Modifica", "ShowAll"]
    for lista in lista_lista:
         if lista[0] in lista_comenzi:
            if lista[0] == lista_comenzi[0]:
                lista_noua = lista[1:]
                lista_rezervari = ui_adauga_rezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[1]:
                lista_noua = lista[1:]
                lista_rezervari = ui_sterge_rezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[2]:
                lista_noua = lista[1:]
                lista_rezervari = ui_update_rezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[3]:
               show_all(lista_rezervari)