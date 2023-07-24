#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID
Records all tasks that are owned by this employee in csv file
"""
import csv
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

    def delete_keys(dic):
        """removes keys from a dictionary"""
        new = {}
        new.update({'USER_ID': dic.get('userId')})
        new.update({'USERNAME': name})
        new.update({'TASK_COMPLETED_STATUS': dic.get('completed')})
        new.update({'TASK_TITLE': dic.get('title')})

        return new

    alter_list = list(map(delete_keys, todo_list))
    fields = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']

    with open(f'{id}.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields, quoting=csv.QUOTE_ALL)
        writer.writerows(alter_list)
