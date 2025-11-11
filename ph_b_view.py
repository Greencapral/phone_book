import time
import ph_b_model
from ph_b_model import CONTACT


def menu():
    print('Пожалуйста, введите номер пункта для выбора операции:')
    print('-' * 25)
    print('[1] - Показать все имеющиеся контакты')
    print('[2] - Создать новый контакт')
    print('[3] - Редактировать имеющиеся контакт')
    print('[4] - Найти контакт')
    print('[5] - Удалить контакт')
    print('[6] - Выход')
    print('-' * 25)


def show_all_contacts():
    context = ph_b_model.file_load()
    if not context:
        print('*' * 25)
        print('В справочнике пока пусто! Скорее наполни его!!!')
        print('*' * 25)

        time.sleep(2)
    else:
        for i in context:
            CONTACT['Name'] = i['Name']
            CONTACT['Surname'] = i['Surname']
            CONTACT['Phone'] = i['Phone']
            CONTACT['Email'] = i['Email']
            CONTACT['Comments'] = i['Comments']
            show_cart()
            time.sleep(1)


def show_cart():
    print(f'Имя        : {CONTACT['Name']}')
    print(f'Фамилия    : {CONTACT['Surname']}')
    print(f'Телефон(🔑): {CONTACT['Phone']}')
    print(f'Email      : {CONTACT['Email']}')
    print(f'Комментарии: {CONTACT['Comments']}')
    print('*' * 25)


def new_contact():
    global CONTACT
    all_id = []

    print('\n')
    print('*' * 25)
    print('Создание нового контакта:\n')
    CONTACT['Name'] = input('Введите имя:')
    CONTACT['Surname'] = input('Введите фамилию:')
    CONTACT['Phone'] = input('Введите номер телефона:')
    CONTACT['Email'] = input('Введите адрес электронной почты:')
    CONTACT['Comments'] = input('Введите комментарии:')
    print('*' * 25)
    print('Вы ввели:\n')
    show_cart()

    while True:
        ansver = input("Всё верно? сохраняем? ('Да'=1, 'нет'=0):")
        if ansver == '1':
            context = ph_b_model.file_load()
            if not context:
                CONTACT['ID'] = 1
            else:
                for i in context:
                    all_id.append(i.get('ID'))
                CONTACT['ID'] = max(all_id) + 1

            tel_chek = ph_b_model.find_one('Phone', CONTACT['Phone'])
            if len(tel_chek) > 0:
                print('!!!ААА!!!')
                print('Всё пропало!')
                print('Контакт с таким номером телефона уже есь в базе!')
                print('А в нашей базе возможны только уникальные номера телефонов!')
                print('Никак не могу записать такое, сорри!')
                break

            context.append(CONTACT)
            ph_b_model.file_save(context)
            print('*' * 25)
            print('Готово!\nВозвращаемся в главное меню...')
            time.sleep(1)
            break
        elif ansver == '0':
            break
        else:
            print('некорректный ввод, повторите.')
            time.sleep(2)


def search_contact():
    while True:
        print('Пожалуйста, введите номер пункта для выбора операции:')
        print('-' * 25)
        print('[1] - Поиск по имени')
        print('[2] - Поиск по фамилии')
        print('[3] - Поиск по телефону')
        print('[4] - Поиск по адресу электронной почты')
        print('[5] - Выход')
        print('-' * 25)

        vibor = input('Ваш выбор: ')
        if vibor == '1':
            sch_field = 'Name'
        elif vibor == '2':
            sch_field = 'Surname'
        elif vibor == '3':
            sch_field = 'Phone'
        elif vibor == '4':
            sch_field = 'Email'
        elif vibor == '5':
            return
        else:
            print('ваш выбор пока не реализован в справочнике, попробуйте выбрать что-то другое.\n')
            time.sleep(1)
            continue

        sch_text = input('введите строку поиска: ')
        result = ph_b_model.find_one(sch_field, sch_text)

        if not result:
            print('-' * 25)
            print('Хммм. нет такого. Если хотите то добавьте')
            print('-' * 25)
            time.sleep(1)
        else:
            found_ones = []

            for k, i in enumerate(result, 1):
                CONTACT['Name'] = i['Name']
                CONTACT['Surname'] = i['Surname']
                CONTACT['Phone'] = i['Phone']
                CONTACT['Email'] = i['Email']
                CONTACT['Comments'] = i['Comments']
                print(f'№ найденной записи: {k}')
                found_ones.append((i['ID'], k))
                show_cart()
                time.sleep(1)

            while True:
                vibor = input("Хотите отредактировать найденную запись? (1 - 'да', 2 - 'нет'): ")
                if vibor == '1':
                    ed_item_input = int(input('Введите номер найденной записи: '))
                    if ed_item_input not in found_ones:
                        print('-' * 25)
                        print('Этого я не смогу сделать. Начинай сначала (ты вышел за рамки дозволенного!)')
                        print('-' * 25)
                        time.sleep(1)
                        return
                    ed_item = next(x[0] for x in found_ones if x[1] == ed_item_input)
                    edit_contact(ed_item)
                    break
                elif vibor == '2':
                    break
                else:
                    print('ваш выбор пока не реализован в справочнике, попробуйте выбрать что-то другое.\n')
                    time.sleep(1)


def select_edit():
    print('-' * 25)
    print('Вообще-то, по хорошему, прежде чем изменять, объект неплохо было бы найти...')
    edit_item = int(input('Но если вы такой умный, то просто введите ID записи для изменения: '))
    edit_contact(edit_item)


def edit_contact(vibor):
    print('-' * 25)
    context = ph_b_model.file_load()
    try:
        ed_item = next(x for x in context if x['ID'] == vibor)
    except StopIteration:
        print('нет такого! не могу редактировать несуществующее!')
        print('-' * 25)
        time.sleep(1)
        return
    print('Добро пожаловать в режим редактирования существующих записей!')
    print('\n')
    print('*' * 25)
    print('Редактирование существующего контакта:\n')
    CONTACT['Name'] = input(f'Имя (сейчас)        : {ed_item['Name']}.  Введите новое имя: ')
    CONTACT['Surname'] = input(f'Фамилия (сейчас)    : {ed_item['Surname']}.  Введите новую фамилию: ')
    CONTACT['Phone'] = input(f'Телефон (сейчас)    : {ed_item['Phone']}.  Введите новый телефон: ')
    CONTACT['Email'] = input(f'Email (сейчас)      : {ed_item['Email']}.  Введите новый Email: ')
    CONTACT['Comments'] = input(f'Комментарии (сейчас): {ed_item['Comments']}.  Введите новые комментарии: ')
    print('*' * 25)
    print('Вы ввели:\n')
    show_cart()

    while True:
        ansver = input("Всё верно? сохраняем? ('Да'=1, 'нет'=0):")
        if ansver == '1':
            context = ph_b_model.file_load()
            temp = next(x for x in context if x['ID'] == vibor)
            context = list(filter(lambda x: not x == temp, context))
            context.append(CONTACT)
            ph_b_model.file_save(context)
            print('*' * 25)
            print('Готово! Все поменяно!')
            return
        elif ansver == '0':
            return
        else:
            print('ваш выбор пока не реализован в справочнике, попробуйте выбрать что-то другое.\n')
            time.sleep(2)


def delete_contact():
    temp = ''
    print('-' * 25)
    print('Вообще-то, по хорошему, прежде чем удалять, объект неплохо было бы найти...')
    del_item = int(input('Но если вы такой умный, то просто введите ID записи для удаления: '))
    context = ph_b_model.file_load()
    if context == []:
        print('А удалять-то нечего - всё пусто!')
        time.sleep(1)
    else:
        try:
            temp = next(x for x in context if x['ID'] == del_item)
        except StopIteration:
            print('нет такого! не могу удалить несуществующее!')

        if not temp:
            print('нет такого! не могу удалить несуществующее!')
            time.sleep(1)
            return

        context.remove(temp)
        ph_b_model.file_save(context)
        print('*' * 25)
        print('Всё! Хана! Удалили насмерть!')
        print('-' * 25)
        time.sleep(1)
