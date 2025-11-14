import time
import ph_b_model
import ph_b_controller

contact ={}

def welcome():
    print('-' * 25)
    print('Добро пожаловать в лучший телефонный справочник на этом компьютере!')
    menu()

def bye():
    print('Всего хорошего!\nДо новых встреч!')

def no_no():
    print('ваш выбор пока не реализован в справочнике, попробуйте выбрать что-то другое.\n')
    time.sleep(2)

def vash_vibor():
    return input('Ваш выбор: ')

def vse_verno():
    return input("Всё верно? сохраняем? ('Да'=1, 'нет'=0):")

def wrong_vvod():
    print('некорректный ввод, повторите.')
    time.sleep(2)

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
    datas = ph_b_model.file_load()
    if not datas:
        print('*' * 25)
        print('В справочнике пока пусто! Скорее наполни его!!!')
        print('*' * 25)
    else:
         show_cart(datas)

    time.sleep(2)


def show_cart(datas):
    for i in datas:
        print(f'Имя        : {i['Name']}')
        print(f'Фамилия    : {i['Surname']}')
        print(f'Телефон(🔑): {i['Phone']}')
        print(f'Email      : {i['Email']}')
        print(f'Комментарии: {i['Comments']}')
        print('*' * 25)


def new_contact():
    data = []
    print('\n')
    print('*' * 25)
    print('Создание нового контакта:\n')
    contact['Name'] = input('Введите имя:')
    contact['Surname'] = input('Введите фамилию:')
    contact['Phone'] = input('Введите номер телефона:')
    contact['Email'] = input('Введите адрес электронной почты:')
    contact['Comments'] = input('Введите комментарии:')
    print('*' * 25)
    print('Вы ввели:\n')
    data.append(contact)
    show_cart(data)
    if ph_b_model.new_contact_add():
        print('*' * 25)
        print('Готово!\nВозвращаемся в главное меню...')
        time.sleep(1)
    else:
        print('!!!ААА!!!')
        print('Всё пропало!')
        print('Контакт с таким номером телефона уже есь в базе!')
        print('А в нашей базе возможны только уникальные номера телефонов!')
        print('Никак не могу записать такое, сорри!')
        time.sleep(1)



def search_contact():
    data =[]
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
                contact['Name'] = i['Name']
                contact['Surname'] = i['Surname']
                contact['Phone'] = i['Phone']
                contact['Email'] = i['Email']
                contact['Comments'] = i['Comments']
                print(f'№ найденной записи: {k}')
                found_ones.append((i['ID'], k))
                data.append(contact)
                show_cart(data)
                time.sleep(1)

            while True:
                vibor = input("Хотите отредактировать найденную запись? (1 - 'да', 2 - 'нет'): ")
                if vibor == '1':
                    ed_item_input = int(input('Введите номер найденной записи: '))
                    if ed_item_input  not in found_ones[0]: #!!!!!!!!
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
    data =[]
    print('-' * 25)
    datas = ph_b_model.file_load()
    try:
        ed_item = next(x for x in datas if x['ID'] == vibor)
    except StopIteration:
        print('нет такого! не могу редактировать несуществующее!')
        print('-' * 25)
        time.sleep(1)
        return
    print('Добро пожаловать в режим редактирования существующих записей!')
    print('\n')
    print('*' * 25)
    print('Редактирование существующего контакта:\n')
    contact['Name'] = input(f'Имя (сейчас)        : {ed_item['Name']}.  Введите новое имя: ')
    contact['Surname'] = input(f'Фамилия (сейчас)    : {ed_item['Surname']}.  Введите новую фамилию: ')
    contact['Phone'] = input(f'Телефон (сейчас)    : {ed_item['Phone']}.  Введите новый телефон: ')
    contact['Email'] = input(f'Email (сейчас)      : {ed_item['Email']}.  Введите новый Email: ')
    contact['Comments'] = input(f'Комментарии (сейчас): {ed_item['Comments']}.  Введите новые комментарии: ')
    print('*' * 25)
    print('Вы ввели:\n')
    data.append(contact)
    show_cart(data)

    while True:
        ansver = input("Всё верно? сохраняем? ('Да'=1, 'нет'=0):")
        if ansver == '1':
            datas = ph_b_model.file_load()
            temp = next(x for x in datas if x['ID'] == vibor)
            datas = list(filter(lambda x: not x == temp, datas))
            datas.append(contact)
            ph_b_model.file_save(datas)
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
    datas = ph_b_model.file_load()
    if datas == []:
        print('А удалять-то нечего - всё пусто!')
        time.sleep(1)
    else:
        try:
            temp = next(x for x in datas if x['ID'] == del_item)
        except StopIteration:
            print('нет такого! не могу удалить несуществующее!')

        if not temp:
            print('нет такого! не могу удалить несуществующее!')
            time.sleep(1)
            return

        datas.remove(temp)
        ph_b_model.file_save(datas)
        print('*' * 25)
        print('Всё! Хана! Удалили насмерть!')
        print('-' * 25)
        time.sleep(1)
