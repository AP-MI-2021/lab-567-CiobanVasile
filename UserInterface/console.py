from Domain.rezervare import get_str, get_nume, get_pret, get_clasa, get_checking, creeaza_rezervare, get_id
from Logic.crud import create, read, update, delete
from Logic.trecere_rezervari import trecere_rezervari_nume_clasa_superioara
from Logic.ieftinire_rezervari_checking import ieftinire_procentaj
from Logic.determina_pret_maxim import determina_pret_maxim_clase
from Logic.ordonare_descrescatoare import ordonare_pret_descrescator
from Logic.afisare_pret_nume import sume_pentru_fiecare_nume
from Logic.undo_redo import do_undo, do_redo


def show_menu():
    print('1.CRUD')
    print('2.Trecerea rezervarilor a unui nume la o clasa superioara. ')
    print('3.Ieftinirea rezervarilor care au checkinul facut cu un anumit procentaj. ')
    print('4.Determinarea pretului maxim pentru fiecare clasa in parte. ')
    print('5.Ordonarea rezervarilor descrescător după pret. ')
    print('6.Afișarea sumelor prețurilor pentru fiecare nume.')
    print('u.Undo ')
    print('r.Redo ')
    print('x.Exit ')


def handle_add(rezervari, undo_list, redo_list):
    try:
        ID = int(input("Dati un ID: "))
        nume = input("Dati un nume: ")
        while True:
            clasa = input("Dati o clasa (economy, economy plus, business): ")
            if clasa != "economy" and clasa != "economy plus" and clasa != "business":
                print("Nu ati introdus o clasa existenta!!!")
            else:
                break
        while True:
            try:
                pret = float(input("Dati un pret: "))
            except ValueError as ve:
                print("Eroare : {}".format(ve))
            else:
                print("Succes")
                break
        while True:
            checkin = input("Dati checkin (da sau nu): ")
            if checkin != "da" and checkin != "nu":
                print("Introduceti da sau nu")
            else:
                break
        rezultat = create(rezervari, ID, nume, clasa, pret, checkin, undo_list, redo_list)

        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return rezervari


def handle_show_all(rezervari):
    for rezervare in rezervari:
        print(get_str(rezervare))

def handle_show_details(rezervari):
    is_id = False
    id_rezervare = int(input('Dati id-ul rezervarii pentru care doriti detalii: '))
    for i in rezervari :
        if id_rezervare == get_id(i):
             is_id = True
             rezervare = read(rezervari, id_rezervare)
             print(f'Nume: {get_nume(rezervare)}')
             print(f'Clasa: {get_clasa(rezervare)}')
             print(f'Pret: {get_pret(rezervare)}')
             print(f'Checking: {get_checking(rezervare)}')

    if is_id == False :
        print("Rezervarea cu id-ul dat nu apare in baza de date ")

def handle_update(rezervari, undo_list, redo_list):
    try:
        ID = int(input("Dati ID-ul rezervarii pe care doriti sa o modificati: "))
        nume = input("Dati un nume nou: ")
        while True:
            clasa = input("Dati o clasa noua(economy, economy plus, business): ")
            if clasa != "economy" and clasa != "economy plus" and clasa != "business":
                print("Nu ati introdus o clasa existenta!!!")
            else:
                break
        while True:
            try:
                pret = float(input("Dati un pret nou: "))
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            else:
                print("Succes")
                break
        while True:
            checkin = input("Dati checkin nou(da sau nu): ")
            if checkin != "da" and checkin != "nu":
                print("Introduceti Da sau Nu")
            else:
                break

        updated = creeaza_rezervare(ID, nume, clasa, pret, checkin)
        rezultat = update(rezervari, updated, undo_list, redo_list)

        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return rezervari


def handle_delete(rezervari, undo_list, redo_list):

    try:
        id_rezervare = int(input('Dati id-ul rezervarii care se va sterge: '))
        rezervari = delete(rezervari, id_rezervare, undo_list, redo_list)
        print('Stergerea a fost efectuata cu succes.')
        return rezervari
    except ValueError as ve:
        print('Eroare:',ve)

    return rezervari

def handle_trecere_rezervari(rezervari, undo_list, redo_list):
    nume = input("Dati numele pentru care rezervarile vor fi trecute la o clasa superioara: ")
    rezervari = trecere_rezervari_nume_clasa_superioara(rezervari, nume, undo_list, redo_list)

    return rezervari


def handle_ieftinire_rezervari(rezervari, undo_list, redo_list):
    try:
        procentaj = int(input('Dati procentajul cu care se ieftinesc rezervarile: '))
        rezervari = ieftinire_procentaj(rezervari, procentaj, undo_list, redo_list)
    except ValueError as ve:
        print('Eroare:', ve)
    return rezervari


def handle_determina_pret_maxim(rezervari):
    print(determina_pret_maxim_clase(rezervari))
    return rezervari


def handle_ordonare_pret_descrescator(rezervari, undo_list, redo_list):
    new_list = ordonare_pret_descrescator(rezervari, undo_list, redo_list)
    return new_list


def handle_sume_pentru_fiecare_nume(list_nume, rezervari):
    list_sume = sume_pentru_fiecare_nume(list_nume, rezervari)
    for nume in range(len(list_nume)):
        print("Suma preturilor pentru numele " + " " + list_nume[nume] + " este " + " " + str(list_sume[nume]))

    return rezervari


def handle_undo(rezervari, undo_list, redo_list):
    undo_result = do_undo(undo_list, redo_list, rezervari)
    if undo_result is not None:
        return undo_result
    return rezervari


def handle_redo(rezervari, undo_list, redo_list):
    redo_result = do_redo(undo_list, redo_list, rezervari)
    if redo_result is not None:
        return redo_result
    return rezervari


def handle_crud(rezervari, undo_list, redo_list):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii rezervare')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_add(rezervari, undo_list, redo_list)
        elif optiune == '2':
            rezervari = handle_update(rezervari, undo_list, redo_list)
        elif optiune == '3':
            rezervari = handle_delete(rezervari, undo_list, redo_list)
        elif optiune == 'a':
            handle_show_all(rezervari)
        elif optiune == 'd':
            handle_show_details(rezervari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return rezervari


def run_ui(rezervari, undo_list, redo_list):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_crud(rezervari, undo_list, redo_list)
        elif optiune == '2':
            rezervari = handle_trecere_rezervari(rezervari, undo_list, redo_list)
        elif optiune == '3':
            rezervari = handle_ieftinire_rezervari(rezervari, undo_list, redo_list)
        elif optiune == '4':
            rezervari = handle_determina_pret_maxim(rezervari)
        elif optiune == '5':
            rezervari = handle_ordonare_pret_descrescator(rezervari, undo_list, redo_list)
        elif optiune == 'u':
            rezervari = handle_undo(rezervari, undo_list, redo_list)
        elif optiune == 'r':
            rezervari = handle_redo(rezervari, undo_list, redo_list)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return rezervari