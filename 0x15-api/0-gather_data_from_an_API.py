#!/usr/bin/python3
"""A bash script to gather data from an API"""

import requests
import sys


def fetch_employee_data(employee_id):
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
    user_name = user_data.get("name").strip()

    # Fetch todo data
    todos_response = requests.get(todo_url)
    if todos_response.status_code != 200:
        print("user not found")
        sys.exit(1)
    todos_data = todos_response.json()

    total_task = len(todos_data)
    completed = []
    for todo in todos_data:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    # Print the output
    print(f"Employee {user_name} is done with "
          f"task({len(completed)}/{total_task}): ")
    for complete in completed:
        print(f"\t {complete}")


if __name__ == "__main__":
    employee_id = sys.argv[1]
    fetch_employee_data(employee_id)
