#!/usr/bin/python3
"""
"""
import json
import requests
import sys

if __name__ == "__main__":

    names_ = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(names_)
    response_1 = requests.get(url)
    jsonRes_1 = response_1.json()
    url = 'https://jsonplaceholder.typicode.com/todos'
    response_2 = requests.get(url, params={'userId': sys.argv[1]}).json()
    result = {}
    completed = []

    for compl in response_2:
        if compl.get('userId') == int(names_):
            new_json = {"task": compl.get('title'),
                        "completed": compl.get('completed'),
                        "username": jsonRes_1.get('username')}
            completed.append(new_json)
    result[names_] = completed

    file = names_ + '.json'
    with open(file, mode='w') as fil:
        json.dump(result, fil)
