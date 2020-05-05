#!/usr/bin/python3
"""
"""
import requests
import sys
import csv

if __name__ == "__main__":

    names_ = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(names_)
    response_1 = requests.get(url)
    jsonRes_1 = response_1.json()
    url = 'https://jsonplaceholder.typicode.com/todos'
    response_2 = requests.get(url, params={'userId': sys.argv[1]}).json()
    with open('{}.csv'.format(names_), 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
               quoting=csv.QUOTE_ALL)
        for compl in response_2:
            writer.writerow([names_, jsonRes_1.get('username'),
                             compl.get('completed'), compl.get('title')])
