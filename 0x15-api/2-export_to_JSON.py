#!/usr/bin/python3
"""A bash script that exports to json"""

import json
import requests
import sys


def export_to_json(emplotee_id):
    # Get URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = ("https://jsonplaceholder.typicode.com/todos?"
                f"userId={employee_id}")

    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("user not found")
        sys.exit(1)
    user_data = user_response.json()
    user_name = user_data.get("username").strip()

    # Fetch todo data
    todos_response = requests.get(todo_url)
    if todos_response.status_code != 200:
        print("user not found")
        sys.exit(1)
    todos_data = todos_response.json()

    # Json format
    task_list = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user_name
        }
        task_list.append(task_dict)

    # Create final JSON dictionary
    json_data = {str(employee_id): task_list}

    # Write to JSON file
    file_name = f"{employee_id}.json"
    with open(file_name, "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Enter employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_to_json(employee_id)
