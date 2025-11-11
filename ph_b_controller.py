import time
import ph_b_view

try:
    with open('contact.json', 'r') as file:
        tmp = file.read()
except FileNotFoundError:
    with open('contact.json', 'w') as file:
        pass

print('-' * 25)
print('Добро пожаловать в лучший телефонный справочник на этом компьютере!')

while True:
    ph_b_view.menu()
    m_vibor = input('Ваш выбор: ')
    if m_vibor == '1':
        ph_b_view.show_all_contacts()
    elif m_vibor == '2':
        ph_b_view.new_contact()
    elif m_vibor == '3':
        ph_b_view.select_edit()
    elif m_vibor == '4':
        ph_b_view.search_contact()
    elif m_vibor == '5':
        ph_b_view.delete_contact()
    elif m_vibor == '6':
        break
    else:
        print('ваш выбор пока не реализован в справочнике, попробуйте выбрать что-то другое.\n')
        time.sleep(2)
        ph_b_view.menu()
