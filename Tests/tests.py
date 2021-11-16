from Domain.rezervare import creeaza_rezervare, get_id, get_pret, get_clasa
from Logic.crud import create, read, update, delete, get_by_id
from Logic.ieftinire_rezervari_checking import ieftinire_procentaj
from Logic.trecere_rezervari import trecere_rezervari_nume_clasa_superioara
from Logic.afisare_pret_nume import sume_pentru_fiecare_nume
from Logic.ordonare_descrescatoare import ordonare_pret_descrescator
from Logic.determina_pret_maxim import determina_pret_maxim_clase


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
    trecere_rezervari_nume_clasa_superioara(rezervari, 'Alandala', [], [])

    assert get_clasa(rezervari[0]) == 'economy'


def test_ordonare_pret_descrescator():
    rezervari = []
    undo_list = []
    redo_list = []

    rezervari = create(rezervari, 1, 'zbor1', 'economy', 10, 'nu', undo_list, redo_list)
    rezervari = create(rezervari, 2, 'zbor2', 'business', 20, 'da', undo_list, redo_list)
    rezervari = create(rezervari, 3, 'zbor3', 'economy plus', 300, 'nu', undo_list, redo_list)
    rezervari = [rezervare[3] for rezervare in ordonare_pret_descrescator(rezervari,[],[])]

    assert rezervari == [300, 20, 10]


def test_determina_pret_maxim_clase():

    rezervari = []

    rezervari = create(rezervari, 1, 'Rusia', "economy plus", 100.0, "da", [], [])
    rezervari = create(rezervari, 2, 'Rusia', "economy", 20.0, "nu" , [], [])
    rezervari = create(rezervari, 3, 'Rusia', "economy", 30.0, "nu" , [], [])
    rezervari = create(rezervari, 4, "Rusia", "business", 240.0, "nu" , [], [])
    rezervari = create(rezervari, 5, "China", "economy plus", 100.0, "nu" , [], [])

    assert determina_pret_maxim_clase(
        rezervari) == "maxim_economy: 30.0, maxim_economy_plus: 100.0, maxim_business: 240.0"


def test_ieftinire_procentaj():
    rezervari = get_data()
    pret_rez = get_pret(rezervari[0])
    ieftinire_procentaj(rezervari, 0, [], [])

    assert pret_rez == get_pret(rezervari[0])


def test_sume_pentru_fiecare_nume():
    rezervari = []
    rezervari = create(rezervari, 1, 'zbor1', 'economy', 100, 'nu', [], [])
    rezervari = create(rezervari, 2, 'zbor2', 'business', 100, 'da', [], [])
    rezervari = create(rezervari, 3, 'zbor2', 'economy plus', 100, 'nu', [], [])

    lista_sume = sume_pentru_fiecare_nume(['zbor1', 'zbor2'], rezervari)
    assert lista_sume == [100, 200]



def test_create():
    rezervari = get_data()
    parametrii = (10, 'Babadum', 'economy', 100, 'da',[],[])
    r_new = creeaza_rezervare(*parametrii[:-2])
    new_rezervari = create(rezervari, *parametrii)

    assert len(new_rezervari) == len(rezervari) + 1
    assert r_new in new_rezervari

    parametrii2 = (10, 'Cioban', 'economyplus', 100, 'nu',[],[])
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
    up = update(rezervari, r_up, [], [])

    assert r_up in up
    assert r_up not in rezervari
    assert len(up) == len(rezervari)

def test_delete():
    rezervari = get_data()
    r_to_delete = 2
    r_deleted = read(rezervari, r_to_delete)
    deleted = delete(rezervari, r_to_delete, [], [])


def tests_functionalitati():
    test_ieftinire_procentaj()
    test_trecere_rezervari_nume_clasa_superioara()
    test_sume_pentru_fiecare_nume()
    test_ordonare_pret_descrescator()
    test_determina_pret_maxim_clase()

def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()


