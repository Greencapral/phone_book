import pytest
import ph_b_model
import ph_b_view
from ph_b_controller import main_menu_control, search_menu_control, edit_contact_control, delete_contact_control

@pytest.fixture
def test_preparation():
    my_tel_spravochnik = ph_b_model.Spravochnik()


@pytest.mark.parametrize('m_vibor, result',[
    ('1', 1),
    ('2', 1),
    ('3', 1),
    ('4', 1),
    ('5', 1),
    ('6', 1),
])
def test_main_menu_control(m_vibor, result):
    assert main_menu_control(m_vibor) == result

def test_search_menu_control():
    pass

def test_edit_contact_control():
    pass

def test_delete_contact_control():
    pass
