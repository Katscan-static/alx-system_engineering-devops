#!/usr/bin/python3
"""
    this module accesses an api and retrieves the data
"""

import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get("{}/users/{}".format(base_url, employee_id))
    user_data = user_response.json()

    if "id" not in user_data:
        sys.exit(1)

    todos_response = requests.get("{}/todos?userId={}".format(base_url,
                                  employee_id))
    todos_data = todos_response.json()
    total_todos = len(todos_data)
    completed_tasks = [todo for todo in todos_data if todo["completed"]]
    num_ct = len(completed_tasks)
    print("Employee {} is done with tasks({}/{}):".format(user_data["name"],
          num_ct,
          total_todos))
    for task in completed_tasks:
        print("\t {}".format(task["title"]))
