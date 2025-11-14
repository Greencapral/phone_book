import ph_b_view
import ph_b_model


def main_menu_control(m_vibor):
    while m_vibor != '6':
        if m_vibor == '1':
            ph_b_view.show_all_contacts()
        elif m_vibor == '2':
            ph_b_view.new_contact()
        elif m_vibor == '3':
            ph_b_view.select_edit()
        elif m_vibor == '4':
            ph_b_view.search_contact()
        elif m_vibor == '5':
            ph_b_view.delete_contact()
        else:
            ph_b_view.no_no()

        ph_b_view.menu()
        m_vibor = ph_b_view.vash_vibor()
    else:
        ph_b_view.bye()

def vse_verno_control():
    ansver = '!'
    while ansver:
        ansver = ph_b_view.vse_verno()
        if ansver == '1':
            return True
        else:
            ph_b_view.wrong_vvod()
    return False


ph_b_model.file_prep_1()
ph_b_view.welcome()
main_menu_control(ph_b_view.vash_vibor())
