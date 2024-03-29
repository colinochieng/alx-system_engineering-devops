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
    task_done = list(filter(lambda dic: dic.get('completed'), todo_list))
    name = user_data.get("name")
    ratio = [len(task_done), len(todo_list)]
    print(f'Employee {name} is done with tasks({ratio[0]}/{ratio[1]}):')
    for dic in task_done:
        print('\t', dic.get('title'))
