import requests
import csv
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

    # Create a CSV file with the user ID as the name
    csv_filename = f'{user_id}.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write tasks to the CSV file
        for todo in todos_data:
            task_completed_status = "True" if todo['completed'] else "False"
            csv_writer.writerow([user_id, username, task_completed_status, todo['title']])

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
