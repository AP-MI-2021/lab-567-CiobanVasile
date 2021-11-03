from Logic.crud import create
from UserInterface.console import run_ui
from Tests.tests import test_crud, tests_functionalitati


def main():
    rezervari = []
    rezervari = run_ui(rezervari)

if __name__ == '__main__':
    test_crud()
    tests_functionalitati()
    main()