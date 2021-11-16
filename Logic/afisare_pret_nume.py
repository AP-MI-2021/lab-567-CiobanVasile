from Domain.rezervare import get_nume,get_pret

def suma_un_nume(Nume, list):
    '''
    Aceasta functie face suma preturilor unei rezervari cu numele "Nume"
    :param Nume: Numele rezervarii pentru care trebuie facuta suma - string
    :param list: Lista rezervarilor
    :return: Returneaza suma preturilor rezervarilor cu numele "Nume"
    '''
    suma = 0
    for rezervare in list:
        if get_nume(rezervare) == Nume:
            suma = suma + get_pret(rezervare)
    return suma
def sume_pentru_fiecare_nume(list_nume, list):
    '''
    Aceasta functie returneaza sumele prețurilor pentru fiecare nume
    :param list_nume: Lista numelor din lista rezervarilor
    :param list: Lista rezervarilor
    :return: Returneaza sumele prețurilor pentru fiecare nume
    '''
    list_sume = []
    for rezervare_nume in list_nume:
        list_sume.append(suma_un_nume(rezervare_nume, list))
    return list_sume