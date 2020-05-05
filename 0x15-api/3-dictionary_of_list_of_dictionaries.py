#!/usr/bin/python3
"""
"""
import json
import requests
import sys

if __name__ == "__main__":

    url_1 = requests.get('https://jsonplaceholder.typicode.com/users').json()
    url_2 = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    res = {}
    for key in url_1:
        titles = []
        for compl in url_2:
            if compl.get('userId') == key.get('id'):
                new_json = {"username": key.get('username'),
                            "task": compl.get('title'),
                            "completed": compl.get('completed')}
                titles.append(new_json)
        res[key.get('id')] = titles
    file = 'todo_all_employees' + '.json'
    with open(file, mode='w') as fil:
        json.dump(res, fil)
