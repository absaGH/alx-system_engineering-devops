#!/usr/bin/python3
"""Exports to-do list information of a given employee ID JSON file"""
import json
import requests
import sys

if __name__ == "__main__":
    usrid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(usrid)).json()
    usrname = user.get("username")
    todos = requests.get(url + "todos", params={"userId": usrid}).json()

    with open("{}.json".format(usrid), "w") as jsonfl:
        json.dump({usrid: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": usrname
        } for task in todos]}, jsonfl)
