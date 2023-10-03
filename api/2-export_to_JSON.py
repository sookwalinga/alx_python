import requests
import json
import sys

def get_employee_info(employee_id):
    # Define the API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Fetch employee information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    user_id = user_data.get('id')
    username = user_data.get('username')

    # Fetch employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create a JSON object with the required format
    employee_tasks = {
        "USER_ID": [{
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        } for todo in todos_data]
    }

    # Create a JSON file with the user ID as the name
    json_filename = f'{user_id}.json'
    with open(json_filename, 'w') as json_file:
        json.dump(employee_tasks, json_file, indent=4)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
