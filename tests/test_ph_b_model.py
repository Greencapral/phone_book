from os import remove

import ph_b_model

test_record = [
    {"Name": "Test",
     "Surname": "STest",
     "Phone": "123",
     "Email": "a@a.com",
     "Comments": "!test!",
     "ID": 99},
    ]


def test_record_creation(needed_id: int):
    test_record = ph_b_model.Contacts()
    test_record.ID = needed_id
    test_record.Name = "Test Name"
    test_record.surname = "Test SurName"
    test_record.phone = "987654321"
    test_record.Email = "test@test.com"
    test_record.comment = "test comment"
    return test_record


def test_spr_file_safe():
    global test_record
    my_tel_spravochnik = ph_b_model.Spravochnik('test.json')
    assert my_tel_spravochnik.file_save(test_record) == True
    remove(my_tel_spravochnik.filename)


def test_spr_file_load():
    my_tel_spravochnik = ph_b_model.Spravochnik('test.json')
    assert isinstance(my_tel_spravochnik.file_load(), list)
    remove(my_tel_spravochnik.filename)


def test_spr_find_one():
    global test_record
    my_tel_spravochnik = ph_b_model.Spravochnik('test.json')
    my_tel_spravochnik.file_save(test_record)
    name = 'Test'
    email = 'a@a.com'
    assert my_tel_spravochnik.find_one('Name', name)[0]['Name'] == name
    assert my_tel_spravochnik.find_one('Email', email)[0]['Email'] == email
    remove(my_tel_spravochnik.filename)

def test_file_availability():
    test_file = 'test.test'
    assert ph_b_model.Spravochnik.file_availability(test_file) == 'w'
    remove(test_file)



