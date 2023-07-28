def read_file():
    with open('my_file.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    return data

def write_file(strstr):
    with open('my_file.txt', 'w', encoding='utf-8') as file:
        file.write(strstr)

def print_info(data):
    if data == "":
        print("")
    else:
        from prettytable import PrettyTable
        x = PrettyTable()
        ar = data.split('|')
        x.field_names = ["ИД", "Ф", "И", "О", "Телефон"]
        for i in range(len(ar)):
            x.add_row([str(i)] + ar[i].split(';'))
        print(x)

def print_for_ind(ar_ind, data):
    from prettytable import PrettyTable
    x = PrettyTable()
    ar = data.split('|')
    x.field_names = ["ИД", "Ф", "И", "О", "Телефон"]
    for i in ar_ind:
            x.add_row([str(i)] + ar[i].split(';'))
    print(x)

def add_contact(data):
    new_contact = input('Формат: Ф;И;О;телефон\n')
    if data == "":
        write_file(new_contact)
    else:
        ar = data.split('|')
        ar.append(new_contact)
        strstr = "|".join(ar)
        write_file(strstr)

def search_contact(data):
    search_val = input('Введите значение для поиска: ')
    found_ind = []
    ar = data.split('|')
    for i in range(len(ar)):
        tmp_ar = ar[i].split(';')
        for j in range(len(tmp_ar)):
            if(tmp_ar[j] == search_val):
                found_ind.append(i)
                break
    return found_ind

def change_contact(data):
    id = int(input('Введите ИД изменяемого контакта: '))
    ar = data.split('|')
    old_val = ar[id]
    print("Старое значение:")
    print(old_val)
    new_val = input('Новое значение:\n')
    ar1 = []
    for i in range(len(ar)):
        if i == id:
            ar1.append(new_val)
        else:
            ar1.append(ar[i])
    strstr = "|".join(ar1)
    write_file(strstr)

def delete_contact(data):
    id = int(input('Введите ИД контакта для удаления: '))
    ar = data.split('|')
    delete_val = ar[id]
    print("Удаленное значение:")
    print(delete_val)
    ar1 = []
    for i in range(len(ar)):
        if i != id:
            ar1.append(ar[i])
    if len(ar1) >= 2:
        strstr = "|".join(ar1)
    else:
        strstr = ""
    write_file(strstr)

def menu():
    data = read_file()
    while True:
        print('Выберите действие: ')
        print('1 - вывести всё')
        print('2 - ввести новый контакт')
        print('3 - поиск')
        print('4 - изменить контакт по ИД')
        print('5 - удалить контакт по ИД')
        print('0 - выход из программы')
        n = int(input('Ваш выбор: '))
        if n == 0:
            break
        elif n == 1:
            print_info(data)
        elif n == 2:
            add_contact(data)
            data = read_file()
        elif n == 3:
            found_ind = search_contact(data)
            print(found_ind)
            print_for_ind(found_ind, data)
        elif n == 4:
            change_contact(data)
            data = read_file()
            print_for_ind(found_ind, data)
        elif n == 5:
            delete_contact(data)
            data = read_file()

if __name__ == '__main__':
    menu()
