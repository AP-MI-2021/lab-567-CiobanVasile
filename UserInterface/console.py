from Domain.rezervare import get_str, get_nume, get_pret, get_clasa, get_checking, creeaza_rezervare, get_id
from Logic.crud import create, read, update, delete
from Logic.trecere_rezervari import trecere_rezervari_nume_clasa_superioara
from Logic.ieftinire_rezervari_checking import ieftinire_procentaj

def show_menu():
    print('1.CRUD')
    print('2.Trecerea rezervarilor a unui nume la o clasa superioara')
    print('3.Ieftinirea rezervarilor care au checkinul facut cu un anumit procentaj')
    print('x.Exit')

def handle_add(rezervari):
    id_rezervare = int(input('Dati id-ul rezervarii '))
    nume = input('Dati numele pe care e facuta rezervarea ')
    pret = float(input('Dati pretul rezervarii '))
    clasa = input('Dati clasa rezervarii ')
    checking = input("Este facut checkinul? ")

    return create(rezervari,id_rezervare,nume,clasa,pret,checking)

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

def handle_update(rezervari):
    id_rezervare = int(input('Dati id-ul rezervarii care se actualizeaza: '))
    nume = input('Dati noul nume al rezervarii: ')
    pret = float(input('Dati noul pret al rezervarii: '))
    clasa= input('Dati noua clasa a rezervarii: ')
    checkin = input('Dati checkinul rezervarii: ')
    return update(rezervari, creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin))



def handle_delete(rezervari):
    id_rezervare = int(input('Dati id-ul rezervarii care se va sterge: '))
    rezervari = delete(rezervari, id_rezervare)
    print('Stergerea a fost efectuata cu succes.')
    return rezervari

def handle_crud(rezervari):
    while True:
        print('1. Adaugare')
        print('2. Modificare')
        print('3. Stergere')
        print('a. Afisare')
        print('d. Detalii rezervare')
        print('b. Revenire')

        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_add(rezervari)
        elif optiune == '2':
            rezervari = handle_update(rezervari)
        elif optiune == '3':
            rezervari = handle_delete(rezervari)
        elif optiune == 'a':
            handle_show_all(rezervari)
        elif optiune == 'd':
            handle_show_details(rezervari)
        elif optiune == 'b':
            break
        else:
            print('Optiune invalida.')
    return rezervari

def handle_trecere_rezervari(rezervari):
    nume = input("Dati numele pentru care rezervarile vor fi trecute la o clasa superioara: ")
    rezervari = trecere_rezervari_nume_clasa_superioara(rezervari, nume)

    return rezervari

def handle_ieftinire_rezervari(rezervari):
    procentaj = int(input('Dati procentajul cu care se ieftinesc rezervarile: '))
    rezervari = ieftinire_procentaj(rezervari, procentaj)

    return rezervari

def run_ui(rezervari):

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune == '1':
            rezervari = handle_crud(rezervari)
        elif optiune == '2':
            rezervari = handle_trecere_rezervari(rezervari)
        elif optiune == '3':
            rezervari = handle_ieftinire_rezervari(rezervari)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida.')

    return rezervari