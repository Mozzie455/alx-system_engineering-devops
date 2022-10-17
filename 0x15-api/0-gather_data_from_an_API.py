#!/usr/bin/python3
"""Get data from api"""
import requests
from sys import argv


if __name__ == "__main__":

    users = requests.get(
        "https://jsonplaceholder.typicode.com/users?id=" + argv[1])
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1])

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        users.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
