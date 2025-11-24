import pytest
import ph_b_model
import ph_b_view
from ph_b_controller import main_menu_control, search_menu_control, edit_contact_control, delete_contact_control

# @pytest.fixture
# def example_spravochnik():
#     return ph_b_model.Spravochnik('test.json')

def test_main_menu_control(mocker):
    example_spravochnik = ph_b_model.Spravochnik('test.json')
    mock1 = mocker.patch("ph_b_view.show_all_contacts", example_spravochnik)
    mock1.return_value = 1

    # mocker.patch('ph_b_view.new_contact', return_value=1)
    # mocker.patch('ph_b_controller.edit_contact_control', return_value=1)
    # mocker.patch('ph_b_controller.search_menu_control', return_value=1)
    # mocker.patch('ph_b_controller.delete_contact_control', return_value=1)
    # mocker.patch('ph_b_view.no_no', return_value=1)
    # mocker.patch('ph_b_view.menu', return_value=1)
    # mocker.patch('ph_b_view.vash_vibor', return_value=1)
    # mocker.patch('ph_b_view.bye', return_value=1)
    assert main_menu_control('1') == 1
    # assert main_menu_control('2') == 1
    # assert main_menu_control('3') == 1
    # assert main_menu_control('4') == 1
    # assert main_menu_control('5') == 1
    # assert main_menu_control('6') == 1





def test_search_menu_control():
    pass


def test_edit_contact_control():
    pass


def test_delete_contact_control():
    pass
