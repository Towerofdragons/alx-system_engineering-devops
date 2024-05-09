#!/usr/bin/python3

"""
Return information on specified employee TODO list and export to CSV.
Uses Emplyee ID
"""

if __name__ == "__main__":

    import csv
    import json
    import requests
    import sys
    

    URL = 'https://jsonplaceholder.typicode.com'
    path = '/users'

    e_ID = sys.argv[1]

    resp = requests.get(URL+path+"/"+e_ID)
    resp =  resp.json()

    EMPLOYEE_NAME = resp.get("name")
    USERNAME = resp.get("username")

    path = f'/todos?userId={e_ID}'
    resp = requests.get(URL+path)
    resp = resp.json()

    num = 0
    i = 0 

    while i < len(resp):
        if resp[i].get("completed"):
            num += 1 

        i += 1;

    NUMBER_OF_DONE_TASKS = num
    TOTAL_NUMBER_OF_TASKS = len(resp)

    print(f'Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS})')


    for task in resp:
        if task.get("completed"):
         print("\t " + task["title"])

    with open(f"{e_ID}.csv", mode = "a") as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        for task in resp:
            row = [task.get("userId"), USERNAME, task.get("completed"), task.get("title")]
            # print(row)
            writer.writerow(row)

