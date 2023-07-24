#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
from urllib.request import urlopen


URL = 'https://jsonplaceholder.typicode.com'


def order_keys(dic_list, name, id):
    """removes keys from a dictionary"""
    user_dic = {}
    new = {}
    task_list = []
    for dic in dic_list:
        new.update({'username': name})
        new.update({'task': dic.get('title')})
        new.update({'completed': dic.get('completed')})
        task_list.append(new)
        new = {}
    user_dic.update({f'{id}': task_list})
    return user_dic


if __name__ == '__main__':
    employees = json.loads(urlopen(f'{URL}/users').read().decode('utf-8'))
    todos = json.loads(urlopen(f'{URL}/todos').read().decode('utf-8'))
    json_list = {}

    for user_data in employees:
        id = user_data.get('id')
        todo_list = list(filter(lambda dic: dic.get('userId') == id, todos))
        json_list.update(order_keys(todo_list, user_data.get("username"), id))

    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_list, file)
