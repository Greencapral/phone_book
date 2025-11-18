import ph_b_model
import ph_b_view


def main_menu_control(m_vibor: str):
    """
    Функция управления главным меню
    :param m_vibor: содержит введенное значение для выбора поведения

    """
    while m_vibor != '6':
        if m_vibor == '1':
            ph_b_view.show_all_contacts(my_tel_spravochnik)
        elif m_vibor == '2':
            ph_b_view.new_contact(my_tel_spravochnik)
        elif m_vibor == '3':
            # edit_contact_control()
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


def search_menu_control():
    """
    Функция управления меню поиска
    :return: ничего не возвращает. Возвраты используются для прерывания выполнения функции
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
    # result = ph_b_model.find_one(sch_field, sch_text)
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
            return None
        if ed_item_input not in found_ones[0]:  # !!!!!!!!
            ph_b_view.otkaz_izm()
            return None
        ed_item = next(x[0] for x in found_ones if x[1] == ed_item_input)
        edit_contact_control(my_tel_spravochnik, ed_item)
    elif m_vibor == '2':
        ph_b_view.vozvrat_g_menu()
    else:
        ph_b_view.no_no()

    return None


def edit_contact_control(my_tel_spravochnik, vibor=0):
    """
    Функция управления процессом редактирования.
    Редактирует элемент справочника по переданному ID.
    Если ID не передавалось, инициирует запрос ID для редактирования через рекурсию.
    :param vibor: ID элемента справочника для редактирования
    :return: при успешном редактировании возвращает Истину, иначе None
    """
    if vibor:
        # rez = ph_b_model.chek_edit_possibility(vibor)
        rez = my_tel_spravochnik.chek_edit_possibility(vibor)
        if not rez:
            ph_b_view.net_takogo()
        else:
            ph_b_view.edit_contact_dialog(my_tel_spravochnik, rez)
    else:
        try:
            ed_item_input = int(ph_b_view.select_edit())
        except ValueError:
            ph_b_view.no_no()
            return None
        edit_contact_control(my_tel_spravochnik, ed_item_input)
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
        # rez = ph_b_model.chek_edit_possibility(vibor)
        rez = my_tel_spravochnik.chek_edit_possibility(vibor)
        if not rez:
            ph_b_view.net_takogo()
        else:
            # ph_b_model.delete_contact(rez)
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
    # ph_b_model.file_prep()
    main_menu_control(ph_b_view.welcome())
