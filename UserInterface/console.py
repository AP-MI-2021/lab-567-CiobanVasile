from Domain.rezervare import to_string, get_nume, get_clasa, get_pret, get_checkin
from Logic.crud import adauga_rezervare, delete_rezervare, update_rezervare, get_by_id, get_by_Nume
from Logic.functionalitati import Trecerea_Rezervarilor_La_Clasa_Superioara, Ieftinirea_Rezervarilor_Cu_Un_Procentaj, \
    pret_maxim_ficare_clasa, ordonare_descrescatoare_pret, sume_preturi_fiecare_nume, \
    adaugare_in_lista_nume, undo, redo


def Print_Menu():
    print("1. Adaugare Rezervare")
    print("2. Stergere Rezervare")
    print("3. Modificare Rezervare")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit")
    print("6. Determinarea prețului maxim pentru fiecare clasă")
    print("7. Ordonarea rezervărilor descrescător după preț")
    print("8. Afișarea sumelor prețurilor pentru fiecare nume")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare rezervari facute")
    print("x. Iesire")

def UI_Sterge_Rezervare(lista, undo_operations, redo_operations):
    try:
        ID = input("Dati ID-ul rezervarii pe care doriti sa o stergeti: ")
        if get_by_id(ID, lista) is None:
            raise ValueError("Id-ul nu exista!")
        else:
            Rezervare_de_sters = get_by_id(ID, lista)
            rezultat = delete_rezervare(ID, lista)
            undo_operations.append([
                lambda: adauga_rezervare(
                ID,
                get_nume(Rezervare_de_sters),
                get_clasa(Rezervare_de_sters),
                get_pret(Rezervare_de_sters),
                get_checkin(Rezervare_de_sters),
                rezultat
            ),
                lambda: delete_rezervare(ID, lista)
            ])
            return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def UI_Modifica_Rezervare(lista, undo_operations, redo_operations):
    try:
        ID = input("Dati ID-ul rezervarii pe care doriti sa o modificati: ")
        nume = input("Dati un nume nou: ")
        while True:
            clasa = input("Dati o clasa noua(economy, economy plus, business): ")
            if clasa != "economy" and clasa != "economy plus" and clasa != "business":
                print("Nu ati introdus o clasa existenta!!!")
            else:
                break
        while True:
            try:
                pret = float(input("\033[36mDati un pret nou: "))
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            else:
                print("Succes")
                break
        while True:
            checkin = input("Dati checkin nou(Da sau Nu): ")
            if checkin != "Da" and checkin != "Nu":
                print("Introduceti Da sau Nu")
            else:
                break
        rezultat = update_rezervare(ID, nume, clasa, pret, checkin, lista)
        Rezervare_de_modificat = get_by_id(ID, lista)
        undo_operations.append([
            lambda: update_rezervare(
            ID,
            get_nume(Rezervare_de_modificat),
            get_clasa(Rezervare_de_modificat),
            get_pret(Rezervare_de_modificat),
            get_checkin(Rezervare_de_modificat),
            rezultat
        ),
            lambda: update_rezervare(ID, nume, clasa, pret, checkin, lista)
        ])
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def UI_Adauga_Rezervare(lista, undo_operations, redo_operations):
    try:
        ID = input("Dati un ID: ")
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
            checkin = input("Dati checkin (Da sau Nu): ")
            if checkin != "Da" and checkin != "Nu":
                print("Introduceti Da sau Nu")
            else:
                break
        rezultat =  adauga_rezervare(ID, nume, clasa, pret, checkin, lista)
        undo_operations.append([
            lambda: delete_rezervare(ID, rezultat),
            lambda: adauga_rezervare(ID, nume, clasa, pret, checkin, lista)
        ])
        redo_operations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def Show_All(lista):
    for rezervare in lista:
        print(to_string(rezervare))

def ui_trecerea_rezervarilor_la_clasa_superioara(lista, undo_operations, redo_operations):
    try:
        nume = input("Dati un nume: ")
        if get_by_Nume(nume, lista) is None:
            raise ValueError("Numele dat nu exista in lista!")
        else:
            rezultat = Trecerea_Rezervarilor_La_Clasa_Superioara(nume, lista)
            undo_operations.append([lambda: lista, lambda: rezultat])
            redo_operations.clear()
            return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def ui_ieftinirea_rezervarilor_cu_un_procentaj(lista, undo_operations, redo_operations):
    while True:
        procent = input("Dati un procent de forma 'ab%': ")
        if procent[len(procent) - 1] != "%":
            print("Nu ati introdus un procentaj corect")
        else:
            try:
                proc = procent[0: len(procent) - 1]
                rezultat = Ieftinirea_Rezervarilor_Cu_Un_Procentaj(procent, lista)
                undo_operations.append([lambda: lista, lambda: rezultat])
                redo_operations.clear()
                return rezultat
            except ValueError as ve:
                print("Eroare: {}".format(ve))
                return lista

def UI_Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa(lista):
    print(pret_maxim_ficare_clasa(lista))
    return lista


def UI_Ordonare_Descrescator_Pret(lista, undo_operations, redo_operations):
    rezultat = ordonare_descrescatoare_pret(lista)
    undo_operations.append([lambda: lista, lambda: rezultat])
    redo_operations.clear()
    return rezultat

def UI_Sume_Preturi_Pentru_Fiecare_Nume(lista_nume, lista):
    lista_sume = sume_preturi_fiecare_nume(lista_nume, lista)
    for nume in range(len(lista_nume)):
        print("Suma preturilor pentru numele " + " " + lista_nume[nume] + " este " + " " + str(lista_sume[nume]))

def UI_Lista_de_rezervari():
    lista = []
    lista = adauga_rezervare("1", "Anglia", "economy plus", 100.0, "Da", [])
    lista = adauga_rezervare("2", "Anglia", "economy", 20.0, "Da", lista)
    lista = adauga_rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = adauga_rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = adauga_rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista = adauga_rezervare("6", "China", "economy", 50.0, "Da", lista)
    lista = adauga_rezervare("7", "Germania", "business", 200.0, "Da", lista)
    lista = adauga_rezervare("8", "Germania", "economy", 57.0, "Nu", lista)
    lista = adauga_rezervare("9", "Germania", "economy", 57.0, "Da", lista)
    lista = adauga_rezervare("10", "Austria", "business", 120.0, "Nu", lista)
    lista = adauga_rezervare("11", "Romania", "economy plus", 76.0, "Nu", lista)
    lista = adauga_rezervare("12", "Franta", "economy plus", 123.7, "Nu", lista)
    lista = adauga_rezervare("13", "Franta", "business", 199.9, "Da", lista)
    lista = adauga_rezervare("14", "Franta", "economy", 83.0, "Nu", lista)
    lista = adauga_rezervare("15", "Cehia", "economy", 50.0, "Nu", lista)
    lista = adauga_rezervare("16", "Belgia", "economy", 150.7, "Da", lista)
    lista = adauga_rezervare("17", "Romania", "economy plus", 76.0, "Da", lista)
    lista = adauga_rezervare("18", "Bulgaria", "business", 91.23, "Nu", lista)
    lista = adauga_rezervare("19", "Ungaria", "economy plus", 91.35, "Nu", lista)
    lista = adauga_rezervare("20", "Austria", "business", 120.0, "Da", lista)
    return lista

def run_menu_vechi(lista):
    undo_operations = []
    redo_operations = []
    while True:
        Print_Menu()
        lista_nume = []
        lista_nume = adaugare_in_lista_nume(lista_nume, lista)
        Optiune = input("Dati optiunea: ")
        if Optiune == "1":
            lista = UI_Adauga_Rezervare(lista, undo_operations, redo_operations)
        elif Optiune == "2":
            lista = UI_Sterge_Rezervare(lista, undo_operations, redo_operations)
        elif Optiune == "3":
            lista = UI_Modifica_Rezervare(lista, undo_operations, redo_operations)
        elif Optiune == "4":
            lista = ui_trecerea_rezervarilor_la_clasa_superioara(lista, undo_operations, redo_operations)
        elif Optiune == "5":
            lista = ui_ieftinirea_rezervarilor_cu_un_procentaj(lista, undo_operations, redo_operations)
        elif Optiune == "6":
            UI_Determinarea_Pretului_Maxim_Pentru_Fiecare_Clasa(lista)
        elif Optiune == "7":
            lista = UI_Ordonare_Descrescator_Pret(lista, undo_operations, redo_operations)
        elif Optiune == "8":
            UI_Sume_Preturi_Pentru_Fiecare_Nume(lista_nume, lista)
        elif Optiune == 'u':
            if len(undo_operations) > 0:
                lista = undo(lista, undo_operations, redo_operations)
            else:
                print("Nu se poate face Undo")
        elif Optiune == "r":
            if len(redo_operations) > 0:
                lista = redo(lista, undo_operations, redo_operations)
            else:
                print("Nu se poate face Redo")
        elif Optiune == "a":
            Show_All(lista)
        elif Optiune == "x":
            break
        else:
            print("Optiune invalida")