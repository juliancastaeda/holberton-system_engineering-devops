#!/usr/bin/python3
"""
"""
import requests
import sys
import json

if __name__ == "__main__":

    url_1 = requests.get('https://jsonplaceholder.typicode.com/users').json()
    url_2 = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    res = {}
    for key in url_1:
        titles = []
        for compl in url_2:
            if compl.get('userId') == key.get('id'):
                new_json = {"username": key.get('username'),
                            "titles": compl.get('title'),
                            "completed": compl.get('completed')}
                titles.append(new_json)
        res[key.get('id')] = titles
    file = 'todo_all_employees' + '.json'
    with open(file, mode='w') as fil:
        json.dump(res, fil)
