from Domain.rezervare import creeaza_rezervare, get_id, get_pret, get_clasa
from Logic.crud import create, read, update, delete
from Logic.ieftinire_rezervari_checking import ieftinire_procentaj
from Logic.trecere_rezervari import trecere_rezervari_nume_clasa_superioara

def get_data():
   return [
    creeaza_rezervare(1, 'Vasile', 'economy', 100, 'da'),
    creeaza_rezervare(2, 'Adrian', 'bussines', 12000, 'nu'),
    creeaza_rezervare(3, 'Marton', 'bussines', 145, 'nu'),
    creeaza_rezervare(4, 'Pap', 'economy plus', 1235, 'da'),
    creeaza_rezervare(5, 'Halas', 'economy', 12, 'nu')
   ]

def test_trecere_rezervari_nume_clasa_superioara():
    rezervari = get_data()
    trecere_rezervari_nume_clasa_superioara(rezervari, 'Alandala')

    assert get_clasa(rezervari[0]) == 'economy'


def test_ieftinire_procentaj():
    rezervari = get_data()
    pret_rez = get_pret(rezervari[0])
    ieftinire_procentaj(rezervari, 0)

    assert pret_rez == get_pret(rezervari[0])

def test_create():
    rezervari = get_data()
    parametrii = (10, 'Babadum', 'economy', 100, 'da')
    r_new = creeaza_rezervare(*parametrii)
    new_rezervari = create(rezervari, *parametrii)

    assert len(new_rezervari) == len(rezervari) + 1
    assert r_new in new_rezervari

    parametrii2 = (10, 'Cioban', 'economyplus', 100, 'nu')
    try:
        rezervare = create(new_rezervari, *parametrii2)
        assert False
    except ValueError:
        assert True

def test_read():
    rezervari = get_data()
    id_rez = rezervari[3]

    assert read(rezervari, get_id(id_rez)) == id_rez
    assert read(rezervari, None) == rezervari

def test_update():
    rezervari = get_data()
    r_up=creeaza_rezervare(1, 'Cioban', 'economy plus', 123456, 'da')
    up = update(rezervari, r_up)

    assert r_up in up
    assert r_up not in rezervari
    assert len(up) == len(rezervari)

def test_delete():
    rezervari = get_data()
    r_to_delete = 2
    r_deleted = read(rezervari, r_to_delete)
    deleted = delete(rezervari, r_to_delete)

def tests_functionalitati():
    test_ieftinire_procentaj()
    test_trecere_rezervari_nume_clasa_superioara()

def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()


