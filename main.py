import requests
import json
import datetime
import time
import csv
from time import sleep  # sleep(1) - заснуть на 1 секунду
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_window_main import Ui_MainWindow
from ui_widget_friends_get import Ui_MainWindow_Friends_Get
from ui_widget_newsfeed_search import Ui_MainWindow_Newsfeed_Search
from ui_widget_photos_search import Ui_MainWindow_Photos_Search
from ui_widget_groups_getMembers import Ui_MainWindow_Groups_GetMembers

global ACCESS_TOKEN, PHOTOS_SEARCH_V, NEWSFEED_SEARCH_V, FRIENDS_GET_V, GROUPS_GETMEMBERS_V, USERS_GET_V, GROUPS_GET_BY_ID_V
ACCESS_TOKEN = open('C:/Google Drive/other/token.txt').read()  # здесь вы указываете путь к своему токену доступа
PHOTOS_SEARCH_V = 5.107
NEWSFEED_SEARCH_V = 5.107
FRIENDS_GET_V = 5.107
GROUPS_GETMEMBERS_V = 5.107
USERS_GET_V = 5.107
GROUPS_GET_BY_ID_V = 5.107

if True:  # здесь свёрнуты функции делегирования
    # опишем фукции кнопок меню, делегирующие задачу в общую функцию с передачей номера окна и типа поиска
    def connect_push_button_find_1():
        searched_object = main_menu.comboBox_what_find_1.currentText()
        if searched_object == 'Newsfeed':
            push_button_find(0, searched_object)
        elif searched_object == 'Photos':
            push_button_find(0, searched_object)
        elif searched_object == 'Friends':
            push_button_find(0, searched_object)
        elif searched_object == 'Groups Members':
            push_button_find(0, searched_object)


    def connect_push_button_find_2():
        searched_object = main_menu.comboBox_what_find_2.currentText()
        if searched_object == 'Newsfeed':
            push_button_find(1, searched_object)
        elif searched_object == 'Photos':
            push_button_find(1, searched_object)
        elif searched_object == 'Friends':
            push_button_find(1, searched_object)
        elif searched_object == 'Groups Members':
            push_button_find(1, searched_object)


    # функционал кнопки "clear"
    def connect_push_button_newsfeed_search_clear_1():
        push_button_something_search_clear(0, 'newsfeed.search')


    def connect_push_button_photos_search_clear_1():
        push_button_something_search_clear(0, 'photos.search')


    def connect_push_button_friends_get_clear_1():
        push_button_something_search_clear(0, 'friends.get')


    def connect_push_button_groups_getMembers_clear_1():
        push_button_something_search_clear(0, 'groups.getMembers')


    def connect_push_button_newsfeed_search_clear_2():
        push_button_something_search_clear(1, 'newsfeed.search')


    def connect_push_button_photos_search_clear_2():
        push_button_something_search_clear(1, 'photos.search')


    def connect_push_button_friends_get_clear_2():
        push_button_something_search_clear(1, 'friends.get')


    def connect_push_button_groups_getMembers_clear_2():
        push_button_something_search_clear(1, 'groups.getMembers')


    # функционал кнопки "load"
    def connect_push_button_newsfeed_search_load_1():
        push_button_something_search_load(0, 'newsfeed.search')


    def connect_push_button_photos_search_load_1():
        push_button_something_search_load(0, 'photos.search')


    def connect_push_button_friends_get_load_1():
        push_button_something_search_load(0, 'friends.get')


    def connect_push_button_groups_getMembers_load_1():
        push_button_something_search_load(0, 'groups.getMembers')


    def connect_push_button_newsfeed_search_load_2():
        push_button_something_search_load(1, 'newsfeed.search')


    def connect_push_button_photos_search_load_2():
        push_button_something_search_load(1, 'photos.search')


    def connect_push_button_friends_get_load_2():
        push_button_something_search_load(1, 'friends.get')


    def connect_push_button_groups_getMembers_load_2():
        push_button_something_search_load(1, 'groups.getMembers')


    # функционал кнопки "save"
    def connect_push_button_newsfeed_search_save_1():
        push_button_something_search_save(0, 'newsfeed.search')


    def connect_push_button_photos_search_save_1():
        push_button_something_search_save(0, 'photos.search')


    def connect_push_button_friends_get_save_1():
        push_button_something_search_save(0, 'friends.get')


    def connect_push_button_groups_getMembers_save_1():
        push_button_something_search_save(0, 'groups.getMembers')


    def connect_push_button_newsfeed_search_save_2():
        push_button_something_search_save(1, 'newsfeed.search')


    def connect_push_button_photos_search_save_2():
        push_button_something_search_save(1, 'photos.search')


    def connect_push_button_friends_get_save_2():
        push_button_something_search_save(1, 'friends.get')


    def connect_push_button_groups_getMembers_save_2():
        push_button_something_search_save(1, 'groups.getMembers')


def push_button_find(i: int, searched_object: str):
    """i - widget number,
    searched_object - what we will looking for"""
    if searched_object == 'Newsfeed':
        WidgetNewsfeedSearch[i].show()
    elif searched_object == 'Photos':
        WidgetPhotosSearch[i].show()
    elif searched_object == 'Friends':
        WidgetFriendsGet[i].show()
    elif searched_object == 'Groups Members':
        WidgetGroupsGetMembers[i].show()


def push_button_something_search_load(i: int, request_type: str):
    """i - widget number
    request_type - type of search"""
    request_status = False
    data[i][request_type] = []
    max_one_count = {  # максимальное количество в запросе за раз
        'newsfeed.search': 200,
        'photos.search': 1000,
        'friends.get': 10000,
        'groups.getMembers': 1000,
    }

    total_max_count = {  # максимальное количество запросов вообще
        'newsfeed.search': 1000,
        'photos.search': 3000,
        'friends.get': 10000,  # больше 10000 не бывает
        'groups.getMembers': None,  # нет ограничений?
    }

    params = {'access_token': ACCESS_TOKEN}  # создадим словарь, котоырй будет содержать параметры запросы
    # не надо делать так. Делай формиование списка параметров под одним условием
    if request_type == 'newsfeed.search':
        q = newsfeed_search[i].lineEdit_newsfeed_search_q.text()
        if q != '':  # в запросе обязательно должен быть текст
            q = str(q)
            params.update({'q': q})
            params.update({'v': NEWSFEED_SEARCH_V})
            params.update({'extended': 1})  # 1, если необходимо получить информацию о пользователе или сообществе

            latitude = newsfeed_search[i].lineEdit_newsfeed_search_latitude.text()
            longitude = newsfeed_search[i].lineEdit_newsfeed_search_longitude.text()
            if latitude != '' and longitude != '':
                latitude = float(latitude)
                longitude = float(longitude)
                params.update({'latitude': latitude})  # северная широта
                params.update({'longitude': longitude})  # восточная долгота

            start_time_day = newsfeed_search[i].lineEdit_newsfeed_search_start_time_day.text()
            start_time_month = newsfeed_search[i].lineEdit_newsfeed_search_start_time_month.text()
            start_time_year = newsfeed_search[i].lineEdit_newsfeed_search_start_time_year.text()
            if start_time_day != '' and start_time_month != '' and start_time_year != '':
                start_time_day = int(start_time_day)
                start_time_month = int(start_time_month)
                start_time_year = int(start_time_year)
                start_time = y_m_d_to_unix(start_time_year, start_time_month, start_time_day)
                params.update({'start_time': start_time})

            end_time_day = newsfeed_search[i].lineEdit_newsfeed_search_end_time_day.text()
            end_time_month = newsfeed_search[i].lineEdit_newsfeed_search_end_time_month.text()
            end_time_year = newsfeed_search[i].lineEdit_newsfeed_search_end_time_year.text()
            if end_time_day != '' and end_time_month != '' and end_time_year != '':
                end_time_day = int(end_time_day)
                end_time_month = int(end_time_month)
                end_time_year = int(end_time_year)
                end_time = y_m_d_to_unix(end_time_year, end_time_month, end_time_day)
                params.update({'end_time': end_time})
            request_status = True
            newsfeed_search[i].lineEdit_newsfeed_search_status.setText('Данные выгружены')
        else:
            newsfeed_search[i].lineEdit_newsfeed_search_status.setText('Ошибка запроса')
            main_menu.textBrowser.append('Для поиска по постам необходимо указать текст запроса')

    elif request_type == 'photos.search':
        q = photos_search[i].lineEdit_photos_search_q.text()
        latitude = photos_search[i].lineEdit_photos_search_lat.text()
        longitude = photos_search[i].lineEdit_photos_search_long.text()
        if q != '' or (latitude != '' and longitude != ''):  # в запросе обязательно должен быть текст или координаты
            q = str(q)
            params.update({'q': q})
            params.update({'offset': 0})  # изначальное смещение относительно первого результата
            params.update({'v': PHOTOS_SEARCH_V})
            params.update({'extended': 1})  # 1, если необходимо получить информацию о пользователе или сообществе

            latitude = photos_search[i].lineEdit_photos_search_lat.text()
            longitude = photos_search[i].lineEdit_photos_search_long.text()
            if latitude != '' and longitude != '':
                latitude = float(latitude)
                longitude = float(longitude)
                params.update({'latitude': latitude})  # северная широта
                params.update({'longitude': longitude})  # восточная долгота

            radius = photos_search[i].lineEdit_photos_search_radius.text()
            if radius != '':
                radius = int(radius)
                params.update({'radius': radius})

            start_time_day = photos_search[i].lineEdit_photos_search_start_time_day.text()
            start_time_month = photos_search[i].lineEdit_photos_search_start_time_month.text()
            start_time_year = photos_search[i].lineEdit_photos_search_start_time_year.text()
            if start_time_day != '' and start_time_month != '' and start_time_year != '':
                start_time_day = int(start_time_day)
                start_time_month = int(start_time_month)
                start_time_year = int(start_time_year)
                start_time = y_m_d_to_unix(start_time_year, start_time_month, start_time_day)
                params.update({'start_time': start_time})

            end_time_day = photos_search[i].lineEdit_photos_search_end_time_day.text()
            end_time_month = photos_search[i].lineEdit_photos_search_end_time_month.text()
            end_time_year = photos_search[i].lineEdit_photos_search_end_time_year.text()
            if end_time_day != '' and end_time_month != '' and end_time_year != '':
                end_time_day = int(end_time_day)
                end_time_month = int(end_time_month)
                end_time_year = int(end_time_year)
                end_time = y_m_d_to_unix(end_time_year, end_time_month, end_time_day)
                params.update({'end_time': end_time})

            sort = int(photos_search[i].radioButton_photos_search_sort.isChecked())  # 1 - по лайкам, 0 - по дате
            params.update({'radius': sort})

            request_status = True
            photos_search[i].lineEdit_photos_search_status.setText('Данные выгружены')
        else:
            photos_search[i].lineEdit_photos_search_status.setText('Ошибка запроса')
            main_menu.textBrowser.append('Для поиска по фото необходимо указать текст запроса или координаты')

    elif request_type == 'friends.get':
        user_id = friends_get[i].lineEdit_friends_get_id.text()
        if user_id != '':
            user_id = int(user_id)
            params.update({'user_id': user_id})
            params.update({'v': FRIENDS_GET_V})
            request_status = True
            friends_get[i].lineEdit_friends_get_status.setText('Данные выгружены')
        else:
            main_menu.textBrowser.append('Для поиска по друзьям необходимо указать ID пользователя')
            friends_get[i].lineEdit_friends_get_status.setText('Ошибка запроса')

    elif request_type == 'groups.getMembers':
        group_id = groups_getMembers[i].lineEdit_groups_getMembers_id.text()
        if group_id != '':
            group_id = int(group_id)
            params.update({'group_id': group_id})
            params.update({'v': GROUPS_GETMEMBERS_V})
            request_status = True
            groups_getMembers[i].lineEdit_groups_getMembers_status.setText('Данные выгружены')
        else:
            groups_getMembers[i].lineEdit_groups_getMembers_status.setText('Ошибка запроса')
            main_menu.textBrowser.append('Для поиска по группам необходимо указать ID группы')

    # сформируем сам запрос
    if request_status:
        # ответ имеет параметр "count", по которому можно определить количество резльтатов вообще,
        # и на основании этого и total_max_count (потолка по API) нужно выбрать "count" и локальный потолок
        params.update({'count': 1})  # сделаем тестовый запрос на 1
        # сколько вообще необходимо получить?
        sleep(0.34)
        one_request = requests.get(f"https://api.vk.com/method/{request_type}?", params=params).json()
        main_menu.textBrowser.append(f"Найдено {one_request['response']['count']} результатов '{request_type}'")
        # выбираем, какой взять верхний предел. Ограничение API или ограничение результатов
        this_total_max_count = one_request['response']['count'] if (total_max_count[request_type] is None) or (
                one_request['response']['count'] <= total_max_count[request_type]) else total_max_count[
            request_type]
        main_menu.textBrowser.append(
            f"С учётом глобального ограничения запросов будет загружено {this_total_max_count} результатов '{request_type}'")
        # один запрос равен "потолку API", если колчиство доступных результатов больше потолка API,
        # а если доступных результатов меньше потолка API, то равен количеству доступных результатов
        count = max_one_count[request_type] if this_total_max_count >= max_one_count[
            request_type] else this_total_max_count
        params.update({'count': count})
        offset = 0  # первый сдвиг равен 0, далее он будет расти на размер запроса
        while this_total_max_count > 0:
            sleep(0.34)
            request_json = requests.get(f"https://api.vk.com/method/{request_type}?", params=params).json()
            offset = offset + count
            if request_type == 'newsfeed.search':
                params.update({'start_from': offset})
            else:
                params.update({'offset': offset})
            main_menu.textBrowser.append(f"Осталось загрузить {this_total_max_count} результатов")
            this_total_max_count = this_total_max_count - count
            # записываем данные в переменную
            if request_type == 'newsfeed.search':
                for profile in request_json['response']['profiles']:
                    data[i][request_type].append(str(profile['id']).replace('-', ''))

            elif request_type == 'photos.search':
                for item in request_json['response']['items']:
                    data[i][request_type].append(str(item['owner_id']).replace('-', ''))

            elif request_type == 'friends.get' or request_type == 'groups.getMembers':
                for item in request_json['response']['items']:
                    data[i][request_type].append(str(item).replace('-', ''))
        main_menu.textBrowser.append(
            f"{len(data[i][request_type])} id пользователей без доп.материалов готово к сохранению")


def push_button_something_search_clear(i: int, request_type: str):
    """i - widget number
    request_type - type of search"""
    if request_type == 'newsfeed.search':
        newsfeed_search[i].lineEdit_newsfeed_search_status.setText('Данных нет')
        clearing_lines = [
            newsfeed_search[i].lineEdit_newsfeed_search_q,

            newsfeed_search[i].lineEdit_newsfeed_search_latitude,
            newsfeed_search[i].lineEdit_newsfeed_search_longitude,

            newsfeed_search[i].lineEdit_newsfeed_search_start_time_day,
            newsfeed_search[i].lineEdit_newsfeed_search_start_time_month,
            newsfeed_search[i].lineEdit_newsfeed_search_start_time_year,

            newsfeed_search[i].lineEdit_newsfeed_search_end_time_day,
            newsfeed_search[i].lineEdit_newsfeed_search_end_time_month,
            newsfeed_search[i].lineEdit_newsfeed_search_end_time_year,
        ]
    elif request_type == 'photos.search':
        photos_search[i].lineEdit_photos_search_status.setText('Данных нет')
        clearing_lines = [
            photos_search[i].lineEdit_photos_search_q,

            photos_search[i].lineEdit_photos_search_lat,
            photos_search[i].lineEdit_photos_search_long,
            photos_search[i].lineEdit_photos_search_radius,

            photos_search[i].lineEdit_photos_search_start_time_day,
            photos_search[i].lineEdit_photos_search_start_time_month,
            photos_search[i].lineEdit_photos_search_start_time_year,

            photos_search[i].lineEdit_photos_search_end_time_day,
            photos_search[i].lineEdit_photos_search_end_time_month,
            photos_search[i].lineEdit_photos_search_end_time_year,
        ]
    elif request_type == 'friends.get':
        friends_get[i].lineEdit_friends_get_status.setText('Данных нет')
        clearing_lines = [
            friends_get[i].lineEdit_friends_get_id,
        ]
    elif request_type == 'groups.getMembers':
        groups_getMembers[i].lineEdit_groups_getMembers_status.setText('Данных нет')
        clearing_lines = [
            groups_getMembers[i].lineEdit_groups_getMembers_id,
        ]
    data[i][request_type] = []
    for line in clearing_lines:
        line.clear()


def push_button_something_search_save(i: int, request_type: str):
    """i - widget number
    request_type - type of search"""
    status_line = {
        'newsfeed.search': newsfeed_search[i].lineEdit_newsfeed_search_status,
        'photos.search': photos_search[i].lineEdit_photos_search_status,
        'friends.get': friends_get[i].lineEdit_friends_get_status,
        'groups.getMembers': groups_getMembers[i].lineEdit_groups_getMembers_status,
    }
    if len(data[i][request_type]) > 0:
        csv_name = {
            'newsfeed.search': newsfeed_search[i].lineEdit_newsfeed_search_file_name.text(),
            'photos.search': photos_search[i].lineEdit_photos_search_file_name.text(),
            'friends.get': friends_get[i].lineEdit_friends_get_file_name.text(),
            'groups.getMembers': groups_getMembers[i].lineEdit_groups_getMembers_file_name.text(),
        }
        # создаём/открываем файл .csv:
        this_name = f"{csv_name[request_type]}_{str(i)}{request_type.replace('.', '')}.csv"
        with open(this_name, 'w') as file:
            for id in data[i][request_type]:
                file.write(id + '\n')
        status_line[request_type].setText('Записано в файл')
        main_menu.textBrowser.append(f"В файл '{this_name}' сохранено {len(data[i][request_type])} id")
    else:
        push_button_something_search_load(i, request_type)


def push_button_get_group_id():
    if main_menu.lineEdit_get_group_id_txt_id.text() != '':
        params = {
            'access_token': ACCESS_TOKEN,
            'v': GROUPS_GET_BY_ID_V,
            'group_ids': main_menu.lineEdit_get_group_id_txt_id.text()
        }
        sleep(0.34)
        main_menu.lineEdit_get_group_id_id.setText(str(requests.get(f"https://api.vk.com/method/groups.getById?",
                                                                    params=params).json()['response'][0]['id']))


def push_button_get_user_id():
    if main_menu.lineEdit_get_user_id_txt_id.text() != '':
        params = {
            'access_token': ACCESS_TOKEN,
            'v': USERS_GET_V,
            'user_ids': main_menu.lineEdit_get_user_id_txt_id.text()
        }
        sleep(0.34)
        main_menu.lineEdit_get_user_id_id.setText(str(requests.get(f"https://api.vk.com/method/users.get?",
                                                                   params=params).json()['response'][0]['id']))


def push_button_find_intersections_find():
    first_file_name = main_menu.lineEdit_find_intersections_file_1.text()
    second_file_name = main_menu.lineEdit_find_intersections_file_2.text()
    if first_file_name != '' and second_file_name != '':
        with open(first_file_name) as first_file:
            first_set = set()
            for line in first_file:
                first_set.add(line[0:-2])
        with open(second_file_name) as second_file:
            second_set = set()
            for line in second_file:
                second_set.add(line[0:-2])
        this_black_list = set()
        with open('black_list.csv', 'r') as black_list_file:
            for item in black_list_file:
                ignor_item = item.replace('\n', '')
                this_black_list.add(ignor_item)
        global intersection_set
        intersection_set = (first_set & second_set) - this_black_list
        main_menu.textBrowser.append(f"В '{first_file_name}' и '{second_file_name}' найдено {len(intersection_set)} "
                                     f"пересечений с учётом игнорируемых id из 'black_list.csv'")
        main_menu.lineEdit_find_intersections_status.setText('Отфильтрованно')
    else:
        main_menu.lineEdit_find_intersections_status.setText('Укажите файлы!')


def push_button_find_intersections_save():
    push_button_find_intersections_find()

    global intersection_set
    if intersection_set:
        this_name = f"{main_menu.lineEdit_file_name.text()}_intersections.csv"
        with open(this_name, 'w') as file:
            for id in intersection_set:
                file.write(str(id).replace('-', '') + '\n')
        main_menu.textBrowser.append(f"{len(intersection_set)} id сохранено в '{this_name}'")
    else:
        main_menu.textBrowser.append(f"Впишите имена csv-файлов для поиска их пересечений")
        main_menu.lineEdit_find_intersections_status.setText('Нет данных!')


def push_button_find_intersections_clear():
    main_menu.lineEdit_find_intersections_file_1.clear()
    main_menu.lineEdit_find_intersections_file_2.clear()
    global intersection_set
    intersection_set = set()


def push_button_black_list_add():
    ignored_object = main_menu.lineEdit_black_list_object.text()
    if ignored_object != '':
        with open('black_list.csv', 'r') as old_black_list_file:
            if (ignored_object + '\n') not in old_black_list_file:
                with open('black_list.csv', 'r') as old_black_list_file:
                    new_black_list = set()
                    new_black_list.add(ignored_object+'\n')
                    for item in old_black_list_file:
                        new_black_list.add(item)
                with open('black_list.csv', 'w') as new_black_list_file:
                    for writing_item in new_black_list:
                        new_black_list_file.write(writing_item)
                    main_menu.textBrowser.append(f"{ignored_object} добавлен в 'black_list.csv'")
            else:
                main_menu.textBrowser.append(f"'black_list.csv' уже содержит в себе {ignored_object}")
    else:
        main_menu.textBrowser.append(f"Впишите, что вы хотите добавить в 'black_list.csv'")


def push_button_black_list_seize():
    disignored_object = main_menu.lineEdit_black_list_object.text()
    if disignored_object != '':
        with open('black_list.csv', 'r') as old_black_list_file:
            if (disignored_object + '\n') in old_black_list_file:
                with open('black_list.csv', 'r') as old_black_list_file:
                    new_black_list = set()
                    for item in old_black_list_file:
                        if item.replace('\n', '') != '\n' and item.replace('\n', '') != disignored_object:
                            new_black_list.add(item)
                with open('black_list.csv', 'w') as new_black_list_file:
                    for writing_item in new_black_list:
                        new_black_list_file.write(writing_item)
                main_menu.textBrowser.append(f"{disignored_object} изъят из 'black_list.csv'")
            else:
                main_menu.textBrowser.append(f"'black_list.csv' не содержит в себе {disignored_object}")
    else:
        main_menu.textBrowser.append(f"Впишите, что вы хотите изъять 'black_list.csv'")


def push_button_black_list_display():
    with open('black_list.csv', 'r') as file:
        what_len = set()
        for item in file:
            what_len.add(item)
    main_menu.textBrowser.append(f"'black_list.csv' содержит {len(what_len)} элементов:")
    with open('black_list.csv', 'r') as file:
        for item in file:
            main_menu.textBrowser.append(item.replace('\n', ''))


def unix_to_y_m_d(unix: int) -> dict:
    """Функция получет на вход время в unix-формате, возвращает словарь с годом, месяцем и днём"""
    return {'y': datetime.datetime.fromtimestamp(unix).strftime('%Y'),
            'm': datetime.datetime.fromtimestamp(unix).strftime('%m'),
            'd': datetime.datetime.fromtimestamp(unix).strftime('%d')}


def y_m_d_to_unix(y: int, m: int, d: int) -> str:
    """Функция получет на вход дату (год, месяц и день) возвращает дату в unix-формате"""
    time_tuple = (y, m, d, 0, 0, 0, 0, 0, 0)
    return repr(time.mktime(time_tuple))


def write_json_in_file(data):
    """функция получет json-данные и записывает их в файл data.json"""
    with open('data.json', 'w') as file:  # создаём/открываем файл data
        # и сохраняем данные файла в переменную file
        json.dump(data, file, indent=2, ensure_ascii=False)


def test():
    this_max = min(params_count, total_max)
    while this_max > 0:
        this_max = this_max - max_count
        print(this_max)


def main():
    global data, main_menu, friends_get, newsfeed_search, photos_search, groups_getMembers, WidgetFriendsGet, WidgetNewsfeedSearch, WidgetPhotosSearch, WidgetGroupsGetMembers, intersection_set

    data = [  # данные, полученные в запросе. i - номер виджета, ключ словаря - тип запроса.
        {'newsfeed.search': [], 'photos.search': [], 'friends.get': [], 'groups.getMembers': [], },
        {'newsfeed.search': [], 'photos.search': [], 'friends.get': [], 'groups.getMembers': [], }
    ]
    intersection_set = set()
    app = QtWidgets.QApplication(sys.argv)  # Create application - инициализация приложения
    MainWindow = QtWidgets.QMainWindow()  # Create form main menu создание формы окна главного меню

    friends_get = []
    newsfeed_search = []
    photos_search = []
    groups_getMembers = []

    WidgetFriendsGet = []
    WidgetNewsfeedSearch = []
    WidgetPhotosSearch = []
    WidgetGroupsGetMembers = []

    for i in range(0, 2):  # создаём виджеты NPC от 0 до 1 (две штуки), возможно, потом понадобится больше.
        friends_get.append(Ui_MainWindow_Friends_Get())
        newsfeed_search.append(Ui_MainWindow_Newsfeed_Search())
        photos_search.append(Ui_MainWindow_Photos_Search())
        groups_getMembers.append(Ui_MainWindow_Groups_GetMembers())

        WidgetFriendsGet.append(QtWidgets.QMainWindow())
        WidgetNewsfeedSearch.append(QtWidgets.QMainWindow())
        WidgetPhotosSearch.append(QtWidgets.QMainWindow())
        WidgetGroupsGetMembers.append(QtWidgets.QMainWindow())

        friends_get[i].setupUi(WidgetFriendsGet[i])
        newsfeed_search[i].setupUi(WidgetNewsfeedSearch[i])
        photos_search[i].setupUi(WidgetPhotosSearch[i])
        groups_getMembers[i].setupUi(WidgetGroupsGetMembers[i])

    main_menu = Ui_MainWindow()
    main_menu.setupUi(MainWindow)
    MainWindow.show()

    main_menu.pushButton_get_group_id.clicked.connect(push_button_get_group_id)
    main_menu.pushButton_get_user_id.clicked.connect(push_button_get_user_id)
    main_menu.pushButton_find_1.clicked.connect(connect_push_button_find_1)
    main_menu.pushButton_find_2.clicked.connect(connect_push_button_find_2)

    main_menu.pushButton_find_intersections_find.clicked.connect(push_button_find_intersections_find)
    main_menu.pushButton_find_intersections_clear.clicked.connect(push_button_find_intersections_clear)
    main_menu.pushButton_find_intersections_save.clicked.connect(push_button_find_intersections_save)

    main_menu.pushButton_black_list_add.clicked.connect(push_button_black_list_add)
    main_menu.pushButton_black_list_seize.clicked.connect(push_button_black_list_seize)
    main_menu.pushButton_black_list_display.clicked.connect(push_button_black_list_display)

    newsfeed_search[0].pushButton_newsfeed_search_load.clicked.connect(connect_push_button_newsfeed_search_load_1)
    newsfeed_search[0].pushButton_newsfeed_search_clear.clicked.connect(connect_push_button_newsfeed_search_clear_1)
    newsfeed_search[0].pushButton_newsfeed_search_save.clicked.connect(connect_push_button_newsfeed_search_save_1)
    newsfeed_search[1].pushButton_newsfeed_search_load.clicked.connect(connect_push_button_newsfeed_search_load_2)
    newsfeed_search[1].pushButton_newsfeed_search_clear.clicked.connect(connect_push_button_newsfeed_search_clear_2)
    newsfeed_search[1].pushButton_newsfeed_search_save.clicked.connect(connect_push_button_newsfeed_search_save_2)

    photos_search[0].pushButton_photos_search_load.clicked.connect(connect_push_button_photos_search_load_1)
    photos_search[0].pushButton_photos_search_clear.clicked.connect(connect_push_button_photos_search_clear_1)
    photos_search[0].pushButton_photos_search_save.clicked.connect(connect_push_button_photos_search_save_1)
    photos_search[1].pushButton_photos_search_load.clicked.connect(connect_push_button_photos_search_load_2)
    photos_search[1].pushButton_photos_search_clear.clicked.connect(connect_push_button_photos_search_clear_2)
    photos_search[1].pushButton_photos_search_save.clicked.connect(connect_push_button_photos_search_save_2)

    friends_get[0].pushButton_friends_get_load.clicked.connect(connect_push_button_friends_get_load_1)
    friends_get[0].pushButton_friends_get_clear.clicked.connect(connect_push_button_friends_get_clear_1)
    friends_get[0].pushButton_friends_get_save.clicked.connect(connect_push_button_friends_get_save_1)
    friends_get[1].pushButton_friends_get_load.clicked.connect(connect_push_button_friends_get_load_2)
    friends_get[1].pushButton_friends_get_clear.clicked.connect(connect_push_button_friends_get_clear_2)
    friends_get[1].pushButton_friends_get_save.clicked.connect(connect_push_button_friends_get_save_2)

    groups_getMembers[0].pushButton_groups_getMembers_load.clicked.connect(connect_push_button_groups_getMembers_load_1)
    groups_getMembers[0].pushButton_groups_getMembers_clear.clicked.connect(
        connect_push_button_groups_getMembers_clear_1)
    groups_getMembers[0].pushButton_groups_getMembers_save.clicked.connect(connect_push_button_groups_getMembers_save_1)
    groups_getMembers[1].pushButton_groups_getMembers_load.clicked.connect(connect_push_button_groups_getMembers_load_2)
    groups_getMembers[1].pushButton_groups_getMembers_clear.clicked.connect(
        connect_push_button_groups_getMembers_clear_2)
    groups_getMembers[1].pushButton_groups_getMembers_save.clicked.connect(connect_push_button_groups_getMembers_save_2)
    main_menu.textBrowser.append('Програма иницирована и готова к использованию')
    sys.exit(app.exec_())  # Run main loop


if __name__ == '__main__':
    main()
    # test()