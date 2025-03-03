import json
import csv


def load_tasks(file_path):
    with open(file_path, 'r') as file:
        tasks = json.load(file)
    return tasks


def display_tasks(tasks):
    print("ID | Task Name       | Completed | Priority")
    print("-------------------------------------------")
    for task in tasks:
        print(f"{task['id']}  | {task['task']} | {task['completed']} | {task['priority']}")


def save_tasks(file_path, tasks):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)


def calculate_stats(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task['completed'])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks > 0 else 0

    print("\nTask Completion Stats:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")


def convert_to_csv(tasks, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Task', 'Completed', 'Priority']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in tasks:
            writer.writerow(
                {'ID': task['id'], 'Task': task['task'], 'Completed': task['completed'], 'Priority': task['priority']})



if __name__ == "__main__":
    json_file = 'tasks.json'
    csv_file = 'tasks.csv'
    tasks = load_tasks(json_file)
    display_tasks(tasks)
    calculate_stats(tasks)
    convert_to_csv(tasks, csv_file)
    save_tasks(json_file, tasks)
