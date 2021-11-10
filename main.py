from Tests.all_tests import Run_All
from UserInterface.command_line_console import run_menu_nou
from UserInterface.console import run_menu_vechi, ui_lista_de_rezervari

def Meniu():
    print("1. Interfata veche")
    print("2. Interfata noua")
    print("x. Iesire")

def main():
    #lista = ui_Lista_de_rezervari()
    lista = []
    Run_All()
    while True:
        Meniu()
        optiune = input("Alegeti interfata: ")
        if optiune == '1':
            run_menu_vechi(lista)
        elif optiune == '2':
            run_menu_nou(lista)
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida ")
if __name__ == '__main__':
    main()