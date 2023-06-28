import re
import csv

fio_patt = r"^(\w+)( |,)(\w+)( |,)(\w+|),(,+|)(,,,|[А-Яа-я]+)"
fio_repl = r"\1,\3,\5,\7"
phone_patt = r'(\+\d|\d)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})'
phone_repl = r'+7(\3)\4-\5-\6'
add_phone_patt = r'\(доб\.\s(\d+)\)*'
add_phone_repl = r'доп.\1'


def sub_data(list_data) -> str:
    list_sub = []
    for line in list_data:
        update1 = re.sub(fio_patt, fio_repl, line)
        update2 = re.sub(phone_patt, phone_repl, update1)
        update3 = re.sub(add_phone_patt, add_phone_repl, update2)
        list_sub.append(update3)
    return list_sub


def remove_dubl(list_lines) -> dict:
    res_dict = {}
    for line in list_lines:
        name = line.split(',')
        if name[0] in res_dict:
            for i, element in enumerate(res_dict[name[0]]):
                if element == '':
                    res_dict[name[0][i]] = name[i+1]
        else:
            res_dict[name[0]] = name[0:]
    return res_dict


def dict_to_list(dict_data) -> list:
    final_list = []
    for key, values in dict_data.items():
        for i in values:
            final_list.append(i)
    return final_list


def open_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.readlines()


def write_file(file):
    with open('phonebook.csv', 'w+', encoding='utf-8') as f:
        return f.write(file)


if __name__ == '__main__':
    fin_list = dict_to_list(remove_dubl(sub_data(open_file('phonebook_raw.csv'))))
    write_file(' '.join(fin_list))
