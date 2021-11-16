from Logic.crud import get_by_id, create
from Logic.undo_redo import do_undo, do_redo
from Domain.rezervare import creeaza_rezervare, get_clasa , get_pret
from Logic.trecere_rezervari import trecere_rezervari_nume_clasa_superioara
from Logic.ieftinire_rezervari_checking import ieftinire_procentaj
from Logic.ordonare_descrescatoare import ordonare_pret_descrescator

def test_trecere_rezervari_nume_clasa_superioara_undo_redo():
    undo_list = []
    redo_list = []
    rezervari = []

    rezervari = create(rezervari, 1, "Franta", "economy plus", 100.0, "da", undo_list, redo_list )
    rezervari = create(rezervari, 2, "Franta", "economy", 20.0, "da", undo_list, redo_list )
    rezervari = create(rezervari, 3, "Rusia", "economy", 30.0, "du", undo_list, redo_list )
    rezervari = create(rezervari, 4, "Rusia", "business", 240.0, "nu", undo_list, redo_list )
    rezervari = create(rezervari, 5, "China", "economy plus", 100.0, "nu", undo_list, redo_list )

    rezervari = trecere_rezervari_nume_clasa_superioara(rezervari, "Franta", undo_list, redo_list)

    assert get_clasa(get_by_id(2, rezervari)) == "economy plus"
    assert get_clasa(get_by_id(1, rezervari)) == "business"

    rezervari = do_undo(undo_list, redo_list, rezervari)

    assert get_clasa(get_by_id(2, rezervari)) == "economy"
    assert get_clasa(get_by_id(1, rezervari)) == "economy plus"

    rezervari = do_redo(undo_list, redo_list, rezervari)

    assert get_clasa(get_by_id(2, rezervari)) == "economy plus"
    assert get_clasa(get_by_id(1, rezervari)) == "business"

def test_ieftinirea_rezervarilor_cu_un_procentaj_undo_redo():
    undo = []
    redo = []
    lista = []

    lista = create(lista, 1, "Franta", "economy plus", 100, "da", undo, redo)
    lista = create(lista, 2, "Franta", "economy", 20, "nu", undo, redo)
    lista = create(lista, 3, "Rusia", "economy", 30, "nu", undo, redo)
    lista = create(lista, 4, "Rusia", "business", 240, "nu", undo, redo)
    lista = create(lista, 5, "China", "economy plus", 100, "nu", undo, redo)

    lista_noua = ieftinire_procentaj(lista, 10, undo, redo)

    assert get_pret(get_by_id(1, lista_noua)) == 90
    assert get_pret(get_by_id(2, lista_noua)) == 20

    lista = do_undo(undo, redo, lista)

    assert get_pret(get_by_id(1, lista)) == 100
    assert get_pret(get_by_id(2, lista)) == 20

    lista = do_redo(undo, redo,  lista)

    assert get_pret(get_by_id(1, lista)) == 100
    assert get_pret(get_by_id(2, lista)) == 20

def test_ordonare_descrescator_pret_undo_redo():
    undo = []
    redo = []
    lista = []
    lista = create(lista, 1, "Germaina", "economy plus", 100.0, "Da", undo , redo)
    lista = create(lista, 2, "Franta", "economy", 20.0, "Nu", undo, redo)
    lista = create(lista, 3, "Romania", "economy plus", 80.0, "Da", undo, redo)
    lista = create(lista, 4, "Belgia", "economy", 10.0, "Nu", undo, redo)
    lista_noua = [rezervare for rezervare in ordonare_pret_descrescator(lista, undo, redo)]
    lista_preturi = [rezervare[3] for rezervare in lista_noua]

    assert lista_preturi == [100.0, 80.0, 20.0, 10.0]

    lista = do_undo(undo, redo, lista)
    lista_preturi = [rezervare[3] for rezervare in lista]

    assert lista_preturi == [100.0, 20.0, 80.0, 10.0]

    lista = do_redo(undo, redo, lista)

    lista_preturi = [rezervare[3] for rezervare in lista_noua]
    assert lista_preturi == [100.0, 80.0, 20.0, 10.0]

def test_undo_redo():
    rezervari = []
    undo_list = []
    redo_list = []

    rezervari = create(rezervari, 1, 'zbor1', 'economy', 1234, 'nu', undo_list, redo_list)
    rezervari = create(rezervari, 2, 'zbor2', 'business', 2345, 'da', undo_list, redo_list)
    rezervari = create(rezervari, 3, 'zbor3', 'economy plus', 3456, 'nu', undo_list, redo_list)

    rezervare1 = creeaza_rezervare(1, 'zbor1', 'economy', 1234, 'nu')
    rezervare2 = creeaza_rezervare(2, 'zbor2', 'business', 2345, 'da')
    rezervare3 = creeaza_rezervare(3, 'zbor3', 'economy plus', 3456, 'nu')

    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 2

    assert get_by_id(1, rezervari) == rezervare1
    assert get_by_id(2, rezervari) == rezervare2
    assert get_by_id(3, rezervari) is None


    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 1
    assert get_by_id(1, rezervari) == rezervare1
    assert get_by_id(2, rezervari) is None
    assert get_by_id(3, rezervari) is None

    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 0

    assert get_by_id(1, rezervari) is None
    assert get_by_id(2, rezervari) is None
    assert get_by_id(3, rezervari) is None

    assert do_undo(undo_list, redo_list, rezervari) is None
    assert len(rezervari) == 0

    rezervari = create(rezervari, 1, 'Cioban', 'economy', 1000, 'da', undo_list, redo_list)
    rezervari = create(rezervari, 2, 'Adrian', 'economy plus', 1600, 'nu', undo_list, redo_list)
    rezervari = create(rezervari, 3, 'Marton', 'economy plus', 1600.60, 'da', undo_list, redo_list)

    rezervare1 = creeaza_rezervare(1, 'Cioban', 'economy', 1000, 'da')
    rezervare2 = creeaza_rezervare(2, 'Adrian', 'economy plus', 1600, 'nu')
    rezervare3 = creeaza_rezervare(3, 'Marton', 'economy plus', 1600.60, 'da')

    assert do_redo(undo_list, redo_list, rezervari) is None
    assert len(rezervari) == 3

    assert get_by_id(1, rezervari) == rezervare1
    assert get_by_id(2, rezervari) == rezervare2
    assert get_by_id(3, rezervari) == rezervare3

    rezervari = do_undo(undo_list, redo_list, rezervari)
    rezervari = do_undo(undo_list, redo_list, rezervari)

    assert len(rezervari) == 1
    assert get_by_id(1, rezervari) == rezervare1
    assert get_by_id(2, rezervari) is None
    assert get_by_id(3, rezervari) is None

    rezervari = do_redo(undo_list, redo_list, rezervari)
    rezervari = do_redo(undo_list, redo_list, rezervari)

    assert len(rezervari) == 3
    assert get_by_id(1, rezervari) == rezervare1
    assert get_by_id(2, rezervari) == rezervare2
    assert get_by_id(3, rezervari) == rezervare3


    rezervari = do_undo(undo_list, redo_list, rezervari)
    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 1
    assert get_by_id(1, rezervari) == rezervare1
    assert get_by_id(2, rezervari) is None
    assert get_by_id(3, rezervari) is None

    rezervari = create(rezervari,4,'Raluca', 'business', 1000, 'da', undo_list, redo_list)
    rezervare4 = creeaza_rezervare(4, 'Raluca', 'business', 1000, 'da')
    assert len(rezervari) == 2
    assert get_by_id(1, rezervari) == rezervare1
    assert get_by_id(2, rezervari) is None
    assert get_by_id(3, rezervari) is None
    assert get_by_id(4, rezervari) == rezervare4


    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 1
    assert get_by_id(1, rezervari) == rezervare1
    assert get_by_id(2, rezervari) is None
    assert get_by_id(3, rezervari) is None
    assert get_by_id(4, rezervari) is None

    rezervari = do_undo(undo_list, redo_list, rezervari)
    assert len(rezervari) == 0
    assert get_by_id(1, rezervari) is None
    assert get_by_id(2, rezervari) is None
    assert get_by_id(3, rezervari) is None
    assert get_by_id(4, rezervari) is None

    rezervari = do_redo(undo_list, redo_list, rezervari)
    rezervari = do_redo(undo_list, redo_list, rezervari)

    assert len(rezervari) == 2
    assert get_by_id(1, rezervari) == rezervare1
    assert get_by_id(2, rezervari) is None
    assert get_by_id(3, rezervari) is None
    assert get_by_id(4, rezervari) == rezervare4

    assert do_redo(undo_list, redo_list, rezervari) is None





