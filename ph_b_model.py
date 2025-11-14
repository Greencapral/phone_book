import json

import ph_b_controller


contact = {
    'ID': 0,
    'Name': '',
    'Surname': '',
    'Phone': '',
    'Email': '',
    'Comments': ''
}


def file_prep_1():
    try:
        with open('contact.json', 'r') as file:
            tmp = file.read()
    except FileNotFoundError:
        with open('contact.json', 'w') as file:
            pass


def file_save(context):
    with open('contact.json', 'w') as fl:
        json.dump(context, fl)


def file_load():
    with open('contact.json', 'r') as fl:
        datas = []
        try:
            context = json.load(fl)
        except json.decoder.JSONDecodeError:
            context = []

        for i in context:
            contact['Name'] = i['Name']
            contact['Surname'] = i['Surname']
            contact['Phone'] = i['Phone']
            contact['Email'] = i['Email']
            contact['Comments'] = i['Comments']
            datas.append(contact)

        return datas


def find_one(field, value):
    result = []
    datas = file_load()
    for i in datas:
        if i[field] == value:
            result.append(i)
    return result


def new_contact_add():
    all_id = []
    ansver = ph_b_controller.vse_verno_control()
    if ansver:
        datas = file_load()
        if not datas:
            contact['ID'] = 1
        else:
            for i in datas:
                all_id.append(i.get('ID'))
            contact['ID'] = max(all_id) + 1

        tel_chek = find_one('Phone', contact['Phone'])
        if len(tel_chek) > 0:
            return False

        datas.append(contact)
        file_save(datas)
        return True
    else:
        return False
