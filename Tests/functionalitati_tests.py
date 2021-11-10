from Domain.rezervare import get_clasa, get_pret,creeaza_rezervare
from Logic.crud import adauga_rezervare, get_by_id, delete_rezervare
from Logic.functionalitati import trecerea_rezervarilor_la_clasa_superioara, ieftinirea_rezervarilor_cu_un_procentaj, \
     ordonare_descrescatoare_pret,sume_preturi_fiecare_nume,pret_maxim_ficare_clasa,undo,redo


def test_trecerea_rezervarilor_la_clasa_superioara():
    lista = adauga_rezervare("1", "Franta", "economy plus", 100.0, "Da", [])
    lista = adauga_rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = adauga_rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = adauga_rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = adauga_rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista = trecerea_rezervarilor_la_clasa_superioara("Franta", lista)

    assert get_clasa(get_by_id("2", lista)) == "economy plus"
    assert get_clasa(get_by_id("1", lista)) == "business"

def test_trecerea_rezervarilor_la_clasa_superioara_undo_redo():
    undo_operations = []
    redo_operations = []
    lista = adauga_rezervare("1", "Franta", "economy plus", 100.0, "Da", [])
    lista = adauga_rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = adauga_rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = adauga_rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = adauga_rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista_noua = trecerea_rezervarilor_la_clasa_superioara("Franta", lista)
    assert get_clasa(get_by_id("2", lista_noua)) == "economy plus"
    assert get_clasa(get_by_id("1", lista_noua)) == "business"
    undo_operations.append([lambda: lista, lambda: lista_noua])
    redo_operations.clear()
    if len(undo_operations) > 0:
        lista = undo(lista, undo_operations, redo_operations)
    assert get_clasa(get_by_id("2", lista)) == "economy"
    assert get_clasa(get_by_id("1", lista)) == "economy plus"
    if len(redo_operations) > 0:
        lista = redo(lista, undo_operations, redo_operations)
    assert get_clasa(get_by_id("2", lista)) == "economy plus"
    assert get_clasa(get_by_id("1", lista)) == "business"

def test_ieftinirea_rezervarilor_cu_un_procentaj():
    lista = adauga_rezervare("1", "Franta", "economy plus", 100.0, "Da", [])
    lista = adauga_rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = adauga_rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = adauga_rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = adauga_rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista = ieftinirea_rezervarilor_cu_un_procentaj("10%", lista)

    assert get_pret(get_by_id("1",lista)) == 90

def test_ieftinirea_rezervarilor_cu_un_procentaj_undo_redo():
    undo_operations = []
    redo_operations = []
    lista = adauga_rezervare("1", "Franta", "economy plus", 100.0, "Da", [])
    lista = adauga_rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = adauga_rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = adauga_rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = adauga_rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista_noua = ieftinirea_rezervarilor_cu_un_procentaj("10%", lista)
    assert get_pret(get_by_id("2", lista_noua)) == 20
    assert get_pret(get_by_id("1", lista_noua)) == 90
    undo_operations.append([lambda: lista, lambda: lista_noua])
    redo_operations.clear()
    if len(undo_operations) > 0:
        lista = undo(lista, undo_operations, redo_operations)
    assert get_pret(get_by_id("2", lista)) == 20
    assert get_pret(get_by_id("1", lista)) == 100
    if len(redo_operations) > 0:
        lista = redo(lista, undo_operations, redo_operations)
    assert get_pret(get_by_id("2", lista)) == 20
    assert get_pret(get_by_id("1", lista)) == 90

def test_determinarea_pretului_maxim_pentru_fiecare_clasa():
    lista = adauga_rezervare("1", "Rusia", "economy plus", 100.0, "Da", [])
    lista = adauga_rezervare("2", "Rusia", "economy", 20.0, "Nu", lista)
    lista = adauga_rezervare ("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = adauga_rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = adauga_rezervare("5", "China", "economy plus", 100.0, "Nu", lista)

    assert pret_maxim_ficare_clasa(lista) == "maxim_economy: 30.0, maxim_economy_plus: 100.0, maxim_business: 240.0"

def test_ordonare_descrescator_pret():
    lista = adauga_rezervare("1", "Germaina", "economy plus", 100.0, "Da", [])
    lista = adauga_rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = adauga_rezervare("3", "Romania", "economy plus", 80.0, "Da", lista)
    lista = adauga_rezervare("4", "Belgia", "economy", 10.0, "Nu", lista)
    lista = [rezervare[3] for rezervare in ordonare_descrescatoare_pret(lista)]

    assert lista == [100.0, 80.0, 20.0, 10.0]

def test_ordonare_descrescator_pret_undo_redo():
    undo_operations = []
    redo_operations = []
    lista = adauga_rezervare("1", "Germaina", "economy plus", 100.0, "Da", [])
    lista = adauga_rezervare("2", "Franta", "economy", 20.0, "Nu", lista)
    lista = adauga_rezervare("3", "Romania", "economy plus", 80.0, "Da", lista)
    lista = adauga_rezervare("4", "Belgia", "economy", 10.0, "Nu", lista)
    lista_noua = [rezervare for rezervare in ordonare_descrescatoare_pret(lista)]
    lista_preturi = [rezervare[3] for rezervare in lista_noua]
    assert lista_preturi == [100.0, 80.0, 20.0, 10.0]
    undo_operations.append([lambda: lista, lambda: lista_noua])
    redo_operations.clear()
    if len(undo_operations) > 0:
        lista = undo(lista,undo_operations, redo_operations)
    lista_preturi = [rezervare[3] for rezervare in lista]
    assert lista_preturi == [100.0, 20.0, 80.0, 10.0]
    if len(redo_operations) > 0:
        lista = redo(lista, undo_operations, redo_operations)
    lista_preturi = [rezervare[3] for rezervare in lista]
    assert lista_preturi == [100.0, 80.0, 20.0, 10.0]

def test_sume_preturi_pentru_fiecare_nume():
    lista = adauga_rezervare("1", "Ucraina", "economy plus", 100.0, "Da", [])
    lista = adauga_rezervare("2", "Ucraina", "economy", 20.0, "Nu", lista)
    lista = adauga_rezervare("3", "Austria", "economy plus", 80.0, "Da", lista)
    lista = adauga_rezervare("4", "Ucraina", "economy", 10.0, "Nu", lista)
    lista_sume = sume_preturi_fiecare_nume(['Ucraina', 'Austria'], lista)

    assert lista_sume == [130.0, 80.0]

def test_functia_undo_si_redo():
    Undo = []
    Redo = []
    lista = []

    lista = adauga_rezervare("1", "Ucraina", "economy plus", 100.0, "Da", lista)
    lista = adauga_rezervare("2", "Ucraina", "economy", 20.0, "Nu", lista)
    lista = adauga_rezervare("3", "Austria", "economy plus", 80.0, "Da", lista)

    lista = undo(lista, Undo, Redo)

    assert get_by_id('1',lista) == creeaza_rezervare("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_id("3", lista) is None

    lista = undo(lista, Undo, Redo)
    assert get_by_id('1',lista) == ("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None
    lista = undo(lista, Undo, Redo)

    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None

    lista = undo(lista, Undo, Redo)
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None

    lista = adauga_rezervare("1", "Ucraina", "economy plus", 100.0, "Da", lista)
    lista = adauga_rezervare("2", "Ucraina", "economy", 20.0, "Nu", lista)
    lista = adauga_rezervare("3", "Austria", "economy plus", 80.0, "Da", lista)

    lista = redo(lista, Undo, Redo)
    assert get_by_id('1',lista) == creeaza_rezervare("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_id('2',lista) == creeaza_rezervare("2", "Ucraina", "economy", 20.0, "Nu")
    assert get_by_id('3',lista) == creeaza_rezervare("3", "Austria", "economy plus", 80.0, "Da")


    lista = undo(lista, Undo, Redo)
    assert get_by_id('1',lista) == creeaza_rezervare("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_id('2',lista) == creeaza_rezervare("2", "Ucraina", "economy", 20.0, "Nu")
    assert get_by_id("3", lista) is None

    lista = undo(lista, Undo, Redo)

    assert get_by_id('1',lista) == creeaza_rezervare("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None

    lista = adauga_rezervare("4", "Ucraina", "economy", 10.0, "Nu", lista)


    lista = redo(lista, Undo, Redo)
    assert get_by_id('1',lista) == creeaza_rezervare("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_id('2',lista) == creeaza_rezervare("4", "Ucraina", "economy", 10.0, "Nu")

    lista = undo(lista, Undo, Redo)
    assert get_by_id('1',lista) == creeaza_rezervare("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_id('4', lista) is None

    lista = undo(lista, Undo, Redo)
    assert get_by_id('1', lista) is None
    assert get_by_id('4', lista) is None

    lista = redo(lista, Undo, Redo)

    lista = redo(lista, Undo, Redo)
    assert get_by_id('1',lista) == creeaza_rezervare("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_id('4',lista) == creeaza_rezervare("4", "Ucraina", "economy", 10.0, "Nu")

    lista = redo(lista, Undo, Redo)
    assert get_by_id('1',lista) == creeaza_rezervare("1", "Ucraina", "economy plus", 100.0, "Da")
    assert get_by_id('4',lista) == creeaza_rezervare("4", "Ucraina", "economy", 10.0, "Nu")