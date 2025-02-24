**Roadmap.sh Project URL**: [https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

# Task CLI

A command-line interface tool for tracking tasks.

## Features

- Mark tasks as complete/incomplete
- List tasks by status
- Update task descriptions and statuses
- Simple and intuitive command-line interface
- Task list stored as a json file on your 

## Installation

1. Clone the repository
2. Make sure the `task-cli.py` file is executable

```bash
chmod +x task-cli.py
```

## Usage

### Basic Commands

```bash
./task-cli.py add "Task Description"
./task-cli.py update <task_id> <task_description>
./task-cli.py delete <task_id>
./task-cli.py mark-in-progress <task_id>
./task-cli.py mark-done <task_id>
./task-cli.py list
./task-cli.py list <status==todo|in-progress|done>
```

### Task States

- `todo`: Task is pending
- `in-progress`: Task is currently being worked on
- `done`: Task is complete

### Data Storage

The task list is stored in a json file called `tasks.json`. This file is created when the tool is first run.
Each tasks cntains:
- Unique ID (6-character hex)
- Description
- Status
- Creation timestamp
- Last update timestamp

## Example Task JSON Structure

```bash
./task-cli.py list
```

```json
tasks file exists, reading from it
listing all tasks:
{
  "22a579": {
    "createdAt": "2025-02-24T10:38:13.820441",
    "description": "another task",
    "status": "todo",
    "updatedAt": "2025-02-24T10:38:13.820447"
  },
  "31c732": {
    "createdAt": "2025-02-24T10:28:59.370397",
    "description": "new task 3",
    "status": "todo",
    "updatedAt": "2025-02-24T10:28:59.370403"
  },
  "586f2e": {
    "createdAt": "2025-02-24T10:38:17.210688",
    "description": "another new task",
    "status": "todo",
    "updatedAt": "2025-02-24T10:38:17.210694"
  }
}
```