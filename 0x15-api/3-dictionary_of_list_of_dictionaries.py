#!/usr/bin/python3
"""A script to export all employees data in json format"""


import json
import requests


def fetch_data():
    """Fetch user and task data from the API"""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_data = requests.get(users_url).json()
    todos_data = requests.get(todos_url).json()

    # Dict to store all user data
    all_tasks = {}

    # Get user data
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        user_tasks = [
            {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            for todo in todos_data if todo.get("userId") == user_id
        ]

        # Storage format
        all_tasks[str(user_id)] = user_tasks

    return all_tasks


def save_to_json(data, filename="todo_all_employees.json"):
    """Save data to a JSON file"""
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == "__main__":
    """Main script execution"""
    all_tasks = fetch_data()  # Fetch data from API
    save_to_json(all_tasks)  # Save data to JSON file
