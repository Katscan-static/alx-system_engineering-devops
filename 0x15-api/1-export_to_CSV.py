#!/usr/bin/python3
"""
    this module accesses an api and retrieves the data
"""

import csv
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
    print(todos_data)
    csv_filename = "{}.csv".format(user_data["id"])
    with open(csv_filename, mode='w', newline="") as csv_file:
        fieldnames = ["USER_ID",
                      "USERNAME",
                      "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for task in todos_data:
            writer.writerow({
                "USER_ID": user_data["id"],
                "USERNAME": user_data["username"],
                "TASK_COMPLETED_STATUS": task["completed"],
                "TASK_TITLE": task["title"]
                })
