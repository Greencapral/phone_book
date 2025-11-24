from os import remove
import pytest
import ph_b_model
from copy import deepcopy


@pytest.fixture
def example_spravochnik():
    return ph_b_model.Spravochnik('test.json')


@pytest.fixture
def example_record():
    return [
        {"Name": "Test",
         "Surname": "STest",
         "Phone": "123",
         "Email": "a@a.com",
         "Comments": "!test!",
         "ID": 99},
    ]


def test_spr_file_safe(example_spravochnik, example_record):
    assert example_spravochnik.file_save(example_record) == True
    remove(example_spravochnik.filename)


def test_spr_file_load(example_spravochnik):
    assert isinstance(example_spravochnik.file_load(), list)
    remove(example_spravochnik.filename)


def test_spr_find_one(example_spravochnik, example_record):
    example_spravochnik.file_save(example_record)
    name = 'Test'
    email = 'a@a.com'
    assert example_spravochnik.find_one('Name', name)[0]['Name'] == name
    assert example_spravochnik.find_one('Email', email)[0]['Email'] == email
    remove(example_spravochnik.filename)


def test_new_contact_add(example_spravochnik, example_record):
    example_spravochnik.file_save(example_record)
    surname = 'STest'
    phone = '123'
    assert example_spravochnik.find_one('Surname', surname)[0]['Surname'] == surname
    assert example_spravochnik.find_one('Phone', phone)[0]['Phone'] == phone
    remove(example_spravochnik.filename)


def test_chek_edit_possibility(example_spravochnik, example_record):
    example_spravochnik.file_save(example_record)
    result = example_spravochnik.chek_edit_possibility(example_record[0]['ID'])
    assert result['Comments'] == '!test!'
    remove(example_spravochnik.filename)


def test_edit_contact(example_spravochnik, example_record):
    example_spravochnik.file_save(example_record)
    new_one = deepcopy(example_record)
    new_one[0]['Phone'] = '987654'
    example_spravochnik.edit_contact(example_record[0], new_one[0])
    assert example_spravochnik.find_one('Name', example_record[0]['Name'])[0]['Phone'] == new_one[0]['Phone']
    remove(example_spravochnik.filename)


def test_delete_contact(example_spravochnik, example_record):
    example_spravochnik.file_save(example_record)
    assert example_spravochnik.delete_contact(example_record[0]['ID']) == True
    remove(example_spravochnik.filename)


def test_file_availability(example_spravochnik):
    test_file = 'test.json'
    assert example_spravochnik.file_availability(test_file) == 'r'
    remove(test_file)
