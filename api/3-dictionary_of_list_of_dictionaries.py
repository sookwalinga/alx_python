import json
import requests

def get_all_employees_tasks():
    # Define the API endpoints
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Fetch all user data
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Fetch all tasks
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create a dictionary to organize tasks by user
    all_employees_tasks = {}

    for user in users_data:
        user_id = user['id']
        username = user['username']

        # Filter tasks for the current user
        user_tasks = [{
            "username": username,
            "task": todo['title'],
            "completed": todo['completed']
        } for todo in todos_data if todo['userId'] == user_id]

        # Add user tasks to the dictionary
        all_employees_tasks[user_id] = user_tasks

    # Create a JSON file with all employees' tasks
    json_filename = 'todo_all_employees.json'
    with open(json_filename, 'w') as json_file:
        json.dump(all_employees_tasks, json_file, indent=4)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    get_all_employees_tasks()
