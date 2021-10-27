from Domain.rezervare import creeaza_rezervare, get_id
from Logic.crud import create, read, update, delete

def get_data():
   return [
    creeaza_rezervare(1, 'Vasile', 'economy', 12345, 'da'),
    creeaza_rezervare(2, 'Adrian', 'bussines', 12000, 'nu'),
    creeaza_rezervare(3, 'Marton', 'bussines', 145, 'nu'),
    creeaza_rezervare(4, 'Pap', 'economy plus', 1235, 'da'),
    creeaza_rezervare(5, 'Halas', 'economy', 12, 'nu')
   ]

def test_create():
    rezervari = get_data()
    parametrii = (6, 'Babadum', 'ecnomy', 100, 'da')
    r_new = creeaza_rezervare(*parametrii)
    new_rezervari = create(rezervari, *parametrii)

    assert len(new_rezervari) == len(rezervari) + 1

def test_read():
    rezervari = get_data()
    id_rez = rezervari[3]

    assert read(rezervari, get_id(id_rez)) == id_rez
    assert read(rezervari, None) == rezervari

def test_update():
    rezervari = get_data()
    r_up=creeaza_rezervare(1, 'Cioban', 'economy plus', 123456, 'da')
    up = update(rezervari,r_up)

    assert r_up in up
    assert r_up not in rezervari
    assert len(up) == len(rezervari)

def test_delete():
    rezervari = get_data()
    r_to_delete = 2
    r_deleted = read(rezervari, r_to_delete)
    deleted = delete(rezervari, r_to_delete)

def test_crud():
    test_create()
    test_read()
    test_update()
    test_delete()


