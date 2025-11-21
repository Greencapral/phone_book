import pytest
from ph_b_model import Spravochnik
from os import remove


@pytest.fixture(scope='session')
def test_preparation():
    my_tel_spravochnik = Spravochnik('test.json')
    yield
    remove(my_tel_spravochnik.filename)
