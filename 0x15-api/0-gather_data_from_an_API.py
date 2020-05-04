#!/usr/bin/python3
"""
"""
import requests
import sys
from sys import argv

#if __name__ == " __main__":
    
names_ = argv[1]
url = 'https://jsonplaceholder.typicode.com/users/{}'.format(names_)
response_1 = requests.get(url)
jsonRes_1 = response_1.json()
url = 'https://jsonplaceholder.typicode.com/todos'
response_2 = requests.get(url, params={'userId': argv[1]}).json()
titles = []

for compl in response_2:
    if compl.get('completed') is True:
        titles.append(compl.get('title'))
lentitles = len(titles)
lenresponse_2 = len(response_2)
print('Employee {} is done with tasks({}/{}):'.format(jsonRes_1['name'],    lentitles, lenresponse_2))
      
for tit in titles:
    print('\t {}'.format(tit))
