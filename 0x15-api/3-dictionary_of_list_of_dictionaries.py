#!/usr/bin/python3

"""
Return information on specified employee TODO list.
Uses Emplyee ID
"""

if __name__ == "__main__":

    import json
    import requests
    import sys


    URL = 'https://jsonplaceholder.typicode.com'

    # Create new dictionary for all employees
    employee_dict = {}

    # For Each employee, access, format and append task to task list
    for e_ID in range(1,11):
        # Create task list per employee
        # print(e_ID)
        employee_dict[str(e_ID)] = []
        
        path = '/users'
        full_URL = URL + path + "/" + str(e_ID)    
        resp = requests.get(full_URL)
        # print(URL + path + "/" + str(e_ID))
        resp =  resp.json()

        # print(resp)
        # print("----")
        # EMPLOYEE_NAME = resp["name"]
        USERNAME = resp.get("username")
        # print(USERNAME)

        path = f'/todos?userId={e_ID}'
        resp = requests.get(URL+path)
        resp = resp.json()

        # print(resp)

        for task in resp:
            # Format task 
            task_dict = {
                        "username"   : USERNAME,
                        "task"      : task.get("title"),
                        "completed" : task.get("completed")
                    }

            # Append Task to list
            # print(task_dict)
            employee_dict[str(e_ID)].append(task_dict)
        # print(employee_dict[str(e_ID)])

# print("--complete list--")
# print(employee_dict)

# Open file
with open("todo_all_employees.json", "w") as f:
    # Dump dictionary into json and write to file
    f.write(json.dumps(employee_dict))

