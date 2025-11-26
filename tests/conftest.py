import pytest
import ph_b_model
from os import remove


@pytest.fixture(scope="session")
def example_spravochnik():
    yield ph_b_model.Spravochnik('test.json')
    remove('test.json')


@pytest.fixture(scope="session")
def example_record():
    return [
        {"Name": "Test",
         "Surname": "STest",
         "Phone": "123",
         "Email": "a@a.com",
         "Comments": "!test!",
         "ID": 99},
    ]
