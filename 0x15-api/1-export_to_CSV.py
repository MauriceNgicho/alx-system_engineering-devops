#!/usr/bin/python3
"""A bash script that exports to csv"""

import csv
import requests
import sys


def export_to_csv(emplotee_id):
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

    file_name = f"{employee_id}.csv"
    with open(file_name, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                user_name,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Enter employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_to_csv(employee_id)
