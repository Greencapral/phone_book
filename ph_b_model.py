import json
from dataclasses import dataclass

class TelSpravochnikErrors(Exception):
    pass

class SaveFileError(TelSpravochnikErrors):
    def __str__(self):
        return 'Проблема с сохранением файла!!! Сделайте что-нибудь с этим немедленно!\n'


@dataclass
class Contacts:
    def __init__(self):
        self.ID: int = 1
        self.Name: str
        self.Surname: str
        self.Phone: str
        self.Email: str
        self.Comments: str


class Spravochnik:
    def __init__(self, filename: str = 'contact.json'):
        self.filename = filename
        try:
            with open(self.filename, 'r'):
                pass
        except FileNotFoundError:
            with open(self.filename, 'w'):
                pass

    def file_save(self, context: list):
        """
        Метод перезаписывает справочник со всеми изменениями
        :param context: содержит список из словарей с элементами справочника

        """
        with open(self.filename, 'w') as fl:
            try:
                json.dump(context, fl)
            except:
                raise SaveFileError

    def file_load(self):
        """
        Метод читает весь справочник,
        :return: возвращается список словарей-элементов
        """
        with open(self.filename, 'r') as fl:
            try:
                context = json.load(fl)
            except json.decoder.JSONDecodeError:
                context = []
            return context

    def find_one(self, field: str, value: str):
        """
        Метод ищет элемент справочника по конкретному значению в конкретном поле
        :param field:  поле,в котором будем искать значение
        :param value:  значение, которое будет искать
        :return: если нашли возвращаем список с элементом, иначе пустой список
        """
        result = []
        datas = self.file_load()
        for i in datas:
            if i[field] == value:
                result.append(i)
        return result

    def new_contact_add(self, n_contact: dict):
        """
        Метод добавляет элемент в переменную-справочник с проверкой на уникальность по номеру телефона
        :param n_contact: словарь который нужно добавить в справочник
        :return: если добавили возвращаем истину
        """
        all_id = []
        datas = self.file_load()
        if not datas:
            n_contact['ID'] = 1
        else:
            for i in datas:
                all_id.append(i.get('ID'))
            n_contact['ID'] = max(all_id) + 1
        tel_chek = self.find_one('Phone', n_contact['Phone'])
        if len(tel_chek) > 0:
            return False
        datas.append(n_contact)
        self.file_save(datas)
        return True

    def chek_edit_possibility(self, vibor: int):
        """
        Метод проверяет наличие элемента в справочнике
        :param vibor: содержит ID элемента, который ищем
        :return: возвращаем элемент
        """
        datas = self.file_load()
        try:
            ed_item = next(x for x in datas if x['ID'] == vibor)
        except StopIteration:
            return False
        return ed_item

    def edit_contact(self, vibor: dict, n_contact: Contacts):
        """
        Метод обновляет поля элемента справочника новыми значениями
        :param vibor: ID элемента для обновления
        :param n_contact: новое состояние элемента, которое нужно записать под указанным ID

        """
        datas = self.file_load()
        temp = next(x for x in datas if x['ID'] == vibor['ID'])
        datas = list(filter(lambda x: not x == temp, datas))
        datas.append(n_contact)
        self.file_save(datas)

    def delete_contact(self, del_item: int):
        """
        Метод удаляет контакт
        :param del_item: элемент, который надо удалить
        :return: возвращает None если не смогла удалить и True если смогла
        """
        datas = self.file_load()
        if not datas:
            return None
        else:
            try:
                temp = next(x for x in datas if x['ID'] == del_item)
            except StopIteration:
                return None
        datas.remove(temp)
        self.file_save(datas)
        return True


if __name__ == '__main__':
    print('Запускайте ph_b_controller.py!')
