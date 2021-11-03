from UserInterface.console import run_ui
from Tests.tests import test_crud, tests_functionalitati
from UserInterface.command_line_console import menu_help


def meniuri():
    print('1. Meniul vechi')
    print('2. Meniul nou')
    print('x. Exit')


def main():
    rezervari = []
    while True:
        meniuri()
        optiune = input('Alegeti interfata: ')
        if optiune == '1':
            menu_help(rezervari)
        elif optiune == '2':
            run_ui(rezervari)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida ")


if __name__ == '__main__':
    test_crud()
    tests_functionalitati()
    main()
