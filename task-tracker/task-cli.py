#!/usr/bin/env python

import json
import sys
import uuid
from datetime import datetime

command_list = ["add", "update", "delete", "mark-done","mark-in-progress", "list"]

def add_task(task_list, task):
    """task_list add <task_description>"""
    print(f"adding task: {task}")
    # add a new item to the task dictionary
    # create a unique task_id
    # add the task to the task dictionary
    # save the task dictionary to the tasks.json file
    # print the task dictionary
    task_id = str(uuid.uuid4().hex[:6])
    task_list[task_id] = {}
    task_list[task_id]["description"] = task
    task_list[task_id]["status"] = "todo"
    task_list[task_id]["createdAt"] = datetime.now().isoformat()
    task_list[task_id]["updatedAt"] = datetime.now().isoformat()

    with open("tasks.json", "w") as f:
        json.dump(task_list, f, indent=2, sort_keys=True)
    print(f"task added with id: {task_id}")

def update_task(task_list, task_id, task_description):
    """task_list update <task_id> <task_description>"""
    if task_id not in task_list:
        print(f"task with id: {task_id} not found. please provide a valid task_id")
        return
    else:
        task_list[task_id]["description"] = task_description
        task_list[task_id]["updatedAt"] = datetime.now().isoformat()
        print(f"updating task: {task_id} with task: {task_description}")
        return task_list

def delete_task(task_list, task_id):
    """task_list delete <task_id>"""
    if task_id not in task_list:
        print(f"task with id: {task_id} not found")
        return
    else:
        print(f"deleting task: {task_id}")
        del task_list[task_id]
        return task_list

def mark_in_progress(task_list, task_id):
    """task_list mark-complete <task_id>"""
    if task_list[task_id]["status"] == "in-progress":
        print(f"task: {task_id} is already in-progress")
    else:
        print(f"marking task: {task_id} as in-progress")
        task_list[task_id]["status"] = "in-progress"
        task_list[task_id]["updatedAt"] = datetime.now().isoformat()
        return task_list

def mark_done(task_list, task_id):
    """task_list mark-done <task_id>"""
    if task_list[task_id]["status"] == "done":
        print(f"task: {task_id} is already done")
    else:
        print(f"marking task: {task_id} as done")
        task_list[task_id]["status"] = "done"
        task_list[task_id]["updatedAt"] = datetime.now().isoformat()
        return task_list

def list_tasks(task_list, status=None):
    """task_list list [status]"""
    if status is None:
        print(f"listing all tasks:")
    else:
        print(f"listing tasks with status: {status}")
    
    if status:
        filtered_tasks = {
            id: task for id, task in task_list.items()
            if task["status"] == status
        }
    else:
        filtered_tasks = task_list

    if not filtered_tasks:
        print("no tasks found")
        return
    
    print(json.dumps(filtered_tasks, indent=2, sort_keys=True))

def save_tasks(task_list):
    with open('tasks.json', 'w') as f:
        json.dump(task_list, f, indent=2, sort_keys=True)

def main():
    # create the logic sequence to parse the user input based on the actions in command_list
    # check if the user provided 3 or fewer arguments
    if len(sys.argv) > 3:
        print("Please provide 3 or fewer arguments. Here are some example commands:")
        print("task-cli add 'task description'")
        print("task-cli update 'task id' 'task description'")
        print("task-cli delete 'task id'")
        print("task-cli mark-in-progress 'task id'")
        print("task-cli mark-done 'task id'")
        print("task-cli list")
        print("task-cli list done")
        print("task-cli list todo")
        print("task-cli list in-progress")
        sys.exit(1)
    
    if sys.argv[1] not in command_list:
        print(f"Invalid command: {sys.argv[1]}")
        sys.exit(1)

    command = sys.argv[1]

    # create the tasks json file if it doesn't exist
    # if the file exists, open and read it to a dictionary called tasks
    # otherwise just create a new tasks dictionary
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
            print("tasks file exists, reading from it")
    except (FileNotFoundError, json.JSONDecodeError):
        # create a new tasks.json file
        with open("tasks.json", "w") as f:
            tasks = {}
            json.dump(tasks, f)
            print("tasks file did not exist, created a new one")
    
    if command == "add":
        if len(sys.argv) != 3:
            print("'add' command requires a task description")
            sys.exit(1)
        add_task(tasks, sys.argv[2])

    elif sys.argv[1] == "update" and len(sys.argv) == 4:
        task_list = update_task(tasks, sys.argv[2], sys.argv[3])
        save_tasks(task_list)

    elif sys.argv[1] == "delete" and len(sys.argv) == 3:
        task_list = delete_task(tasks, sys.argv[2])
        save_tasks(task_list)

    elif sys.argv[1] == "mark-in-progress" and len(sys.argv) == 3:
        task_list = mark_in_progress(tasks, sys.argv[2])
        save_tasks(task_list)

    elif sys.argv[1] == "mark-done" and len(sys.argv) == 3:
        task_list = mark_done(tasks, sys.argv[2])
        save_tasks(task_list)
        
    elif sys.argv[1] == "list":
        if len(sys.argv) == 2:
            list_tasks(tasks)
        elif sys.argv[2] in ["todo", "in-progress", "done"]:
            list_tasks(tasks, sys.argv[2])
        else:
            print(f"Invalid status: {sys.argv[2]}")
            sys.exit(1)

if __name__ == "__main__":
    main()