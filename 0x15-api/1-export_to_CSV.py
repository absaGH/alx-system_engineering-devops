#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    usrid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(usrid)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": usrid}).json()

    with open("{}.csv".format(usrid), "w", newline="") as csvfl:
        writer = csv.writer(csvfl, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [usrid, username, task.get("completed"), task.get("title")]
        ) for task in todos]
