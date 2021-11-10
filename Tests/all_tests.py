from Tests.crud_test import test_get_by_Nume,test_get_by_id,test_create_rezervare,test_update_rezervare,\
    test_delete_rezervare
from Tests.functionalitati_tests import test_functia_undo_si_redo, test_ordonare_descrescator_pret_undo_redo,\
    test_ordonare_descrescator_pret,test_sume_preturi_pentru_fiecare_nume,test_determinarea_pretului_maxim_pentru_fiecare_clasa,\
    test_ieftinirea_rezervarilor_cu_un_procentaj,test_ieftinirea_rezervarilor_cu_un_procentaj_undo_redo,\
    test_trecerea_rezervarilor_la_clasa_superioara,test_trecerea_rezervarilor_la_clasa_superioara_undo_redo


def Run_All():
    '''
    In aceasta functie se introduc toate testele
    :return:
    '''
    test_get_by_Nume()
    test_get_by_id()
    test_create_rezervare()
    test_delete_rezervare()
    test_update_rezervare()
    test_trecerea_rezervarilor_la_clasa_superioara()
    test_ieftinirea_rezervarilor_cu_un_procentaj()
    test_determinarea_pretului_maxim_pentru_fiecare_clasa()
    test_ordonare_descrescator_pret()
    test_sume_preturi_pentru_fiecare_nume()
    test_functia_undo_si_redo()
    test_trecerea_rezervarilor_la_clasa_superioara_undo_redo()
    test_ieftinirea_rezervarilor_cu_un_procentaj_undo_redo()
    test_ordonare_descrescator_pret_undo_redo()