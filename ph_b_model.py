import json

contact = {
    'ID': 1,
    'Name': '',
    'Surname': '',
    'Phone': '',
    'Email': '',
    'Comments': ''
}


def file_prep():
    """
    Функция проверяет наличие файла данных, если его нет - создает

    """
    try:
        with open('contact.json', 'r'):
            pass
    except FileNotFoundError:
        with open('contact.json', 'w'):
            pass


def file_save(context:list):
    """
    Функция перезаписывает справочник со всеми изменениями
    :param context: содержит список из словарей с элементами справочника

    """
    with open('contact.json', 'w') as fl:
        json.dump(context, fl)


def file_load():
    """
    Функция читает весь справочник,
    :return: возвращается список словарей-элементов
    """
    with open('contact.json', 'r') as fl:
        try:
            context = json.load(fl)
        except json.decoder.JSONDecodeError:
            context = []
        return context


def find_one(field:str, value:str):
    """
    Функция ищет элемент справочника по конкретному значению в конкретном поле
    :param field:  поле,в котором будем искать значение
    :param value:  значение, которое будет искать
    :return: если нашли возвращаем список с элементом, иначе пустой список
    """
    result = []
    datas = file_load()
    for i in datas:
        if i[field] == value:
            result.append(i)
    return result


def new_contact_add(n_contact:dict):
    """
    Функция добавляет элемент в переменную-справочник с проверкой на уникальность по номеру телефона
    :param n_contact: словарь который нужно добавить в справочник
    :return: если добавили возвращаем истину
    """
    all_id = []
    datas = file_load()
    if not datas:
        n_contact['ID'] = 1
    else:
        for i in datas:
            all_id.append(i.get('ID'))
        n_contact['ID'] = max(all_id) + 1
    tel_chek = find_one('Phone', n_contact['Phone'])
    if len(tel_chek) > 0:
        return False
    datas.append(n_contact)
    file_save(datas)
    return True


def chek_edit_possibility(vibor:int):
    """
    Функция проверяет наличие элемента в справочнике
    :param vibor: содержит ID элемента, который ищем
    :return: возвращаем элемент
    """
    datas = file_load()
    try:
        ed_item = next(x for x in datas if x['ID'] == vibor)
    except StopIteration:
        return False
    return ed_item


def edit_contact(vibor:dict, n_contact:dict):
    """
    Функция обновляет поля элемента справочника новыми значениями
    :param vibor: ID элемента для обновления
    :param n_contact: новое состояние элемента, которое нужно записать под указанным ID

    """
    datas = file_load()
    temp = next(x for x in datas if x['ID'] == vibor['ID'])
    datas = list(filter(lambda x: not x == temp, datas))
    datas.append(n_contact)
    file_save(datas)


def delete_contact(del_item:dict):
    """
    Функция удаляет контакт
    :param del_item: элемент, который надо удалить
    :return: возвращает None если не смогла удалить и True если смогла
    """
    datas = file_load()
    if not datas:
        return None
    else:
        try:
            temp = next(x for x in datas if x['ID'] == del_item['ID'])
        except StopIteration:
            return None
    datas.remove(temp)
    file_save(datas)
    return True


if __name__ == '__main__':
    print('Запускайте ph_b_controller.py!')
