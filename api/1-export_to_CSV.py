import csv
import requests
import sys

def get_employee_info(employee_id):
    # Define the API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Fetch employee information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_id = user_data.get('id')
    employee_name = user_data.get('username')

    # Fetch employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create a CSV file to save the tasks
    csv_filename = f'{employee_id}.csv'

    # Write tasks to CSV
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos_data:
            task_completed_status = "Completed" if todo['completed'] else "Not Completed"
            csv_writer.writerow([employee_id, employee_name, task_completed_status, todo['title']])

    print(f"Data has been exported to {csv_filename}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
