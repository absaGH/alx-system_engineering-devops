#!/usr/bin/python3
"""Exports todo list information of all employees to JSON file"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfl:
        json.dump({
            emp.get("id"): [{
                "task": j.get("title"),
                "completed": j.get("completed"),
                "username": emp.get("username")
            } for j in requests.get(url + "todos",
                                    params={"userId": emp.get("id")}).json()]
            for emp in users}, jsonfl)
