from Logic.crud import create,delete,update,read,creeaza_rezervare
from UserInterface.console import handle_show_all
from Domain.rezervare import get_id

def read_in_line():
    '''
    Citire lista in liniei
    La separatorul ";" gasit se va rupe lista si vor fi create doua liste separate
    La separatorul "," gasit se va rupe lista, astfel incat lista noastra va fi parcursa cuvant cu cuvant
    :return:
    '''
    list_one = []
    list_two = []
    print("Separatorii de comenzi: '; '")
    print("Separatori de cuvinte: ', '")
    print("!Nu uitati sa puneti cate un spatiu dupa fiecare separator!")
    comanda= input("Dati niste comenzi din lista {Adaugare, Stergere, Modificarea, showAll}: ")
    lista = comanda.split('; ')
    for i in lista:
        word = i.split(', ')
        list_two = []
        for x in range(len(word)):
            list_two.append(word[x])
        list_one.append(list_two)
    return list_one
def adauga_rezervare(list, new_list):
        '''
        Adauga o rezervare in lista noastra
        :param list: lista de rezervari
        :param new_list: lista care contine rezervarea mea curenta care trebuie adaugata in lista de rezervari
        :return:
        '''
        try:
            ID = new_list[0]
            nume = new_list[1]
            clasa = new_list[2]
            if clasa != "economy" and clasa != "economy plus" and clasa != "business":
                print('Clasa pe care ati introdus-o nu exista ')
                return list
            checkin = new_list[4]
            if checkin != "da" and checkin != "nu":
                print('Introduceti daca este sau nu facut checkinul ')
                return list
            pret = float(new_list[3])
            return create(list, new_list[0], new_list[1], new_list[2], float(new_list[3]), new_list[4])
        except IndexError as ve:
            print('Eroare', ve)
            return list
        except ValueError as ve:
            print('Eroare ', ve)
            return list

def sterge_rezervare(list, new_list):
        '''
        Sterge o rezervare in lista din baza de date
        :param list: lista de rezervari
        :param new_list: lista care contine rezervarea curenta care trebuie adaugata in lista de rezervari
        :return:
        '''
        try:
            if read(list,get_id(new_list[0])) is None:
                print(f'Rezervarea cu id-ul {get_id(new_list[0])} nu exista')
                return list
            else:
                return delete(list, get_id(new_list[0]))
        except ValueError as ve:
            print('Eroare ', ve)
            return list

def modifica_rezervare(list , new_list):
        '''
        Modifica o rezervare in lista noastra
        :param list: lista de rezervari
        :param new_list: lista care contine rezervarea mea curenta care trebuie adaugata in lista de rezervari
        :return:
        '''
        try:
            id = new_list[0]
            nume = new_list[1]
            clasa = new_list[2]
            if clasa != "economy" and clasa != "economy plus" and clasa != "business":
                print("Nu ati introdus o clasa existenta! ")
                return list
            checkin = new_list[4]
            if checkin != "da" and checkin != "nu":
                print("Nu ati introdus da sau nu")
                return list
            pret = float(new_list[3])
            return update(list, creeaza_rezervare(id, nume, clasa, pret, checkin))
        except IndexError as ve:
            print('Eroare:', ve)
            return list
        except ValueError as ve:
            print('Eroare:', ve)
            return list


def menu_help(lista_rezervari):
    lista_lista = read_in_line()
    lista_comenzi = ["Adaugare", "Stergere", "Modificare", "ShowAll"]
    for lista in lista_lista:
         if lista[0] in lista_comenzi:
            if lista[0] == lista_comenzi[0]:
                lista_noua = lista[1:]
                lista_rezervari = adauga_rezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[1]:
                lista_noua = lista[1:]
                lista_rezervari = sterge_rezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[2]:
                lista_noua = lista[1:]
                lista_rezervari = modifica_rezervare(lista_rezervari, lista_noua)
            elif lista[0] == lista_comenzi[3]:
                handle_show_all(lista_rezervari)
