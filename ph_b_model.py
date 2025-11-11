import json

CONTACT = {
    'ID': 0,
    'Name': '',
    'Surname': '',
    'Phone': '',
    'Email': '',
    'Comments': ''
}


def file_save(context):
    with open('contact.json', 'w') as fl:
        json.dump(context, fl)


def file_load():
    with open('contact.json', 'r') as fl:
        try:
            context = json.load(fl)
        except json.decoder.JSONDecodeError:
            context = []
        return context

def find_one(field, value):
    result = []
    context = file_load()
    for i in context:
        if i[field] == value:
            result.append(i)
    return result
