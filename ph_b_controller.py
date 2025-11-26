import ph_b_model
import ph_b_view
from ph_b_model import Spravochnik


def main_menu_control(m_vibor: str):
    """
    Функция управления главным меню
    :param m_vibor: содержит введенное значение для выбора поведения
    :return: возвращает 1 если все прошло штатно

    """
    while m_vibor != '6':
        if m_vibor == '1':
            ph_b_view.show_all_contacts(my_tel_spravochnik)
        elif m_vibor == '2':
            ph_b_view.new_contact(my_tel_spravochnik)
        elif m_vibor == '3':
            edit_contact_control(my_tel_spravochnik)
        elif m_vibor == '4':
            search_menu_control()
        elif m_vibor == '5':
            delete_contact_control()
        else:
            ph_b_view.no_no()

        ph_b_view.menu()
        m_vibor = ph_b_view.vash_vibor()
    else:
        ph_b_view.bye()
    return 1


def search_menu_control():
    """
    Функция управления меню поиска
    :return: возвращает поле для поиска или False если выходим без изменений
    """
    found_ones = []
    sch_field = ''
    ph_b_view.search_contact_menu()
    while m_vibor := ph_b_view.vash_vibor():
        if m_vibor == '1':
            sch_field = 'Name'
            break
        elif m_vibor == '2':
            sch_field = 'Surname'
            break
        elif m_vibor == '3':
            sch_field = 'Phone'
            break
        elif m_vibor == '4':
            sch_field = 'Email'
            break
        elif m_vibor == '5':
            return False
        else:
            ph_b_view.no_no()
            ph_b_view.search_contact_menu()
    sch_text = ph_b_view.chto_ishem()
    result = my_tel_spravochnik.find_one(sch_field, sch_text)
    if not result:
        ph_b_view.net_takogo()
        return False
    else:
        for k, i in enumerate(result, 1):
            ph_b_view.pech_find_number(k)
            found_ones.append((i['ID'], k))
            ph_b_view.show_cart(i)
    m_vibor = ph_b_view.ask_want_izm()
    if m_vibor == '1':
        try:
            ed_item_input = int(ph_b_view.ed_item_input())
        except ValueError:
            ph_b_view.no_no()
            return False
        if ed_item_input not in found_ones[0]:
            ph_b_view.otkaz_izm()
            return False
        ed_item = next(x[0] for x in found_ones if x[1] == ed_item_input)
        edit_contact_control(my_tel_spravochnik, ed_item)
    elif m_vibor == '2':
        ph_b_view.vozvrat_g_menu()
    else:
        ph_b_view.no_no()

    return sch_field


def edit_contact_control(my_t_spravochnik: Spravochnik, vibor=0):
    """
    Функция управления процессом редактирования.
    Редактирует элемент справочника по переданному ID.
    Если ID не передавалось, инициирует запрос ID для редактирования через рекурсию.
    :param my_t_spravochnik: Объект-справочник с которым работаем
    :param vibor: ID элемента справочника для редактирования
    :return: при успешном редактировании возвращает Истину, иначе None
    """
    if vibor:
        rez = my_t_spravochnik.chek_edit_possibility(vibor)
        if not rez:
            ph_b_view.net_takogo()
        else:
            ph_b_view.edit_contact_dialog(my_t_spravochnik, rez)
    else:
        try:
            ed_item_input = int(ph_b_view.select_edit())
        except ValueError:
            ph_b_view.no_no()
            return None
        edit_contact_control(my_t_spravochnik, ed_item_input)
    return True


def delete_contact_control(vibor=0):
    """
    Функция управления процессом удаления.
    Удаляет элемент справочника по переданному ID.
    Если ID не передавалось, инициирует запрос ID для удаления через рекурсию.
    :param vibor: ID элемента справочника для удаления
    :return: при успешном удалении возвращает Истину, иначе None
    """
    if vibor:
        rez = my_tel_spravochnik.chek_edit_possibility(vibor)
        if not rez:
            ph_b_view.net_takogo()
        else:
            my_tel_spravochnik.delete_contact(vibor)
            ph_b_view.delete_contact_dialog()
    else:
        try:
            del_item_input = int(ph_b_view.select_edit())
        except ValueError:
            ph_b_view.no_no()
            return None
        delete_contact_control(del_item_input)
    return True


if __name__ == '__main__':
    my_tel_spravochnik = ph_b_model.Spravochnik()
    main_menu_control(ph_b_view.welcome())
