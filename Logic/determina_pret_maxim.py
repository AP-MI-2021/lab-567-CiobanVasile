from Domain.rezervare import  get_clasa , get_pret

def determina_pret_maxim_clase(list):
    """
    Determina pretul maxim la fiecare clasa de rezervare
    :param list: O lista cu toate rezervarile
    :return: Toate preturile maxime la fiecare dintre cele 3 clase
    """
    maxim_economy = -1
    maxim_economy_plus = -1
    maxim_business = -1
    for rezervare in list:
        if get_clasa(rezervare) == "economy":
            if get_pret(rezervare) > maxim_economy:
                maxim_economy = get_pret(rezervare)
        elif get_clasa(rezervare) == "economy plus":
            if get_pret(rezervare) > maxim_economy_plus:
                maxim_economy_plus = get_pret(rezervare)
        elif get_clasa(rezervare) == "business":
            if get_pret(rezervare) > maxim_business:
                maxim_business = get_pret(rezervare)
    return "maxim_economy: {}, maxim_economy_plus: {}, maxim_business: {}".format(maxim_economy, maxim_economy_plus, maxim_business)

