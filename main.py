import typer
import pyfiglet
import json
import os

# Define file path
FILE_PATH = "to_do_lists.json"

# Initialize the typer app
app = typer.Typer()

## Create a basic CLI structure to handle user inputs

# Load tasks from json file
def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as file:
        return json.load(file)

# Adding a new task
@app.command()
def add(description:str):
    """Add a new task"""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    print(task_id)

# Updating and deleting tasks
@app.command()
def update():
    pass

@app.command()
def delete():
    pass

# Marking a task as in progress or done
@app.command()
def mark_in_progress():
    pass

@app.command()
def mark_done():
    pass

# Listing all tasks
def list():
    pass

# Listing tasks by status
def list_by_status():
    pass

def display_header():
    header = pyfiglet.figlet_format("Task Tracker", font = "bulbhead" )
    typer.echo(header)

if __name__ == "__main__":
    display_header()
    app()