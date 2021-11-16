from UserInterface.console import run_ui
from Tests.tests import test_crud, tests_functionalitati
from Tests.tests_undo_and_redo import test_undo_redo
from UserInterface.command_line_console import menu_help
from Tests.tests_undo_and_redo import test_trecere_rezervari_nume_clasa_superioara_undo_redo
from Tests.tests_undo_and_redo import test_ieftinirea_rezervarilor_cu_un_procentaj_undo_redo
from Tests.tests_undo_and_redo import test_ordonare_descrescator_pret_undo_redo


def meniuri():
    print('1. Meniul vechi(Toate cerintele inclusiv unde si redo)')
    print('2. Meniul nou(Doar primele 3 cerinte)')
    print('x. Exit')

def main():
    undo_list = []
    redo_list = []
    rezervari = []
    while True:
        meniuri()
        optiune = input('Alegeti interfata: ')
        if optiune == '1':
            run_ui(rezervari, undo_list, redo_list)
        elif optiune == '2':
            menu_help(rezervari)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida ")


if __name__ == '__main__':
    test_crud()
    tests_functionalitati()
    test_undo_redo()
    test_trecere_rezervari_nume_clasa_superioara_undo_redo()
    test_ieftinirea_rezervarilor_cu_un_procentaj_undo_redo()
    test_ordonare_descrescator_pret_undo_redo()
    main()
