#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import sys
from urllib.request import urlopen


URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    try:
        id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    user_data = json.loads(urlopen(f'{URL}/users/{id}').read().decode('utf-8'))
    todos = json.loads(urlopen(f'{URL}/todos').read().decode('utf-8'))
    todo_list = list(filter(lambda dic: dic.get('userId') == id, todos))
    name = user_data.get("username")

    def order_keys(dic_list):
        """removes keys from a dictionary"""
        user_dic = {}
        new = {}
        task_list = []
        for dic in dic_list:
            new.update({'task': dic.get('title')})
            new.update({'completed': dic.get('completed')})
            new.update({'username': name})
            task_list.append(new)
            new = {}
        user_dic.update({f'{user_data.get("id")}': task_list})
        return user_dic

    with open(f'{id}.json', 'w') as file:
        json.dump(order_keys(todo_list), file)
