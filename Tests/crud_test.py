from Domain.rezervare import get_id, get_nume, get_clasa, get_pret, get_checkin
from Logic.crud import adauga_rezervare, get_by_id, delete_rezervare, update_rezervare, get_by_Nume


def test_get_by_id():
    lista = adauga_rezervare("1", "Anglia", "business", 100, "Da", [])
    lista = adauga_rezervare("2", "Germania", "economy", 20, "Nu", lista)
    lista = adauga_rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = adauga_rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = adauga_rezervare("5", "China", "economy plus", 100.0, "Nu", lista)

    assert get_by_id('1', lista) == lista[0]
    assert get_by_id('6', lista) is None


def test_get_by_Nume():
    lista = adauga_rezervare("1", "Anglia", "business", 100, "Da", [])
    lista = adauga_rezervare("2", "Germania", "economy", 20, "Nu", lista)
    lista = adauga_rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = adauga_rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = adauga_rezervare("5", "China", "economy plus", 100.0, "Nu", lista)

    assert get_by_Nume('Anglia', lista) == lista[0]
    assert get_by_Nume('6', lista) is None


def test_create_rezervare():
    lista = adauga_rezervare("1", "Anglia", "business", 100, "Da", [])

    assert len(lista) == 1
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_nume(get_by_id("1", lista)) == "Anglia"
    assert get_clasa(get_by_id("1", lista)) == "business"
    assert get_pret(get_by_id("1", lista)) == 100
    assert get_checkin(get_by_id("1", lista)) == "Da"


def test_delete_rezervare():
    lista = adauga_rezervare("1", "Anglia", "business", 100, "Da", [])
    lista = adauga_rezervare("2", "Germania", "economy", 20, "Nu", lista)
    lista = adauga_rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = adauga_rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = adauga_rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista = delete_rezervare("1", lista)

    assert len(lista) == 4
    assert get_by_id('1', lista) is None
    assert get_by_id('2', lista) is not None


def test_update_rezervare():
    lista = adauga_rezervare("1", "Anglia", "business", 100, "Da", [])
    lista = adauga_rezervare("2", "Germania", "economy", 20, "Nu", lista)
    lista = adauga_rezervare("3", "Rusia", "economy", 30.0, "Nu", lista)
    lista = adauga_rezervare("4", "Rusia", "business", 240.0, "Nu", lista)
    lista = adauga_rezervare("5", "China", "economy plus", 100.0, "Nu", lista)
    lista = update_rezervare("2", "Franta", "economy plus", 20, "Nu", lista)

    assert get_id(get_by_id("2", lista)) == "2"
    assert get_nume(get_by_id("2", lista)) == "Franta"
    assert get_clasa(get_by_id("2", lista)) == "economy plus"
    assert get_pret(get_by_id("2", lista)) == 20
    assert get_checkin(get_by_id("2", lista)) == "Nu"