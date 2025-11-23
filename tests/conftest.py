import pytest
from ph_b_model import Contacts, Spravochnik
from os import remove

# def test_record_creation(needed_id:int):
#     test_record = Contacts()
#     test_record.ID = needed_id
#     test_record.NAME = "Test Name"
#     test_record.surname = "Test SurName"
#     test_record.phone = "987654321"
#     test_record.EMAIL = "test@test.com"
#     test_record.comment = "test comment"
#     return test_record

# @pytest.fixture(scope="session")
# def test_preparation():
#     test_record = test_record_creation(99)
#     my_tel_spravochnik = Spravochnik('test.json')
#     my_tel_spravochnik.file_save(test_record)
#     yield
#     remove(my_tel_spravochnik.filename)
