#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
from urllib.request import urlopen
from sys import argv, exit
import json


URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':
    try:
        id = int(argv[1])
    except ValueError:
        exit(1)
    user_data = json.loads(urlopen(f'{URL}/users/{id}').read().decode('utf-8'))
    todos = json.loads(urlopen(f'{URL}/todos').read().decode('utf-8'))
    todo_list = list(filter(lambda dictionary: dictionary.get('userId') == id, todos))
    task_done = list(filter(lambda dic: dic.get('completed') == True, todo_list))
    print(f'Employee {user_data.get("name")} is done with tasks({len(task_done)}/{len(todo_list)}):')
    for dic in task_done:
        print('\t', dic.get('title'))
