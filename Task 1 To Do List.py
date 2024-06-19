import json

class TodoItem:
    def __init__(self, title, description='', status='pending'):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"[{self.status}] {self.title}: {self.description}"

    def mark_done(self):
        self.status = 'done'

    def mark_pending(self):
        self.status = 'pending'

def load_from_file(filename='todo_list.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [TodoItem(**item) for item in data]
    except FileNotFoundError:
        return []

def save_to_file(todo_list, filename='todo_list.json'):
    with open(filename, 'w') as file:
        json.dump([task.__dict__ for task in todo_list], file, indent=4)

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")
    print("Choose an option: ", end='')

def add_task(todo_list):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    todo_list.append(TodoItem(title, description))

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks available.")
    else:
        for idx, todo in enumerate(todo_list, 1):
            print(f"{idx}. {todo}")

def update_task(todo_list):
    view_tasks(todo_list)
    if todo_list:
        try:
            task_num = int(input("Enter task number to update: ")) - 1
            if 0 <= task_num < len(todo_list):
                task = todo_list[task_num]
                print("1. Mark as done")
                print("2. Mark as pending")
                print("3. Edit task")
                option = int(input("Choose an option: "))
                if option == 1:
                    task.mark_done()
                elif option == 2:
                    task.mark_pending()
                elif option == 3:
                    task.title = input("Enter new title: ")
                    task.description = input("Enter new description: ")
                else:
                    print("Invalid option. Returning to menu.")
            else:
                print("Invalid task number. Returning to menu.")
        except ValueError:
            print("Invalid input. Returning to menu.")

def delete_task(todo_list):
    view_tasks(todo_list)
    if todo_list:
        try:
            task_num = int(input("Enter task number to delete: ")) - 1
            if 0 <= task_num < len(todo_list):
                del todo_list[task_num]
            else:
                print("Invalid task number. Returning to menu.")
        except ValueError:
            print("Invalid input. Returning to menu.")

def main():
    todo_list = load_from_file()
    
    while True:
        display_menu()
        try:
            choice = int(input())
            if choice == 1:
                add_task(todo_list)
            elif choice == 2:
                view_tasks(todo_list)
            elif choice == 3:
                update_task(todo_list)
            elif choice == 4:
                delete_task(todo_list)
            elif choice == 5:
                save_to_file(todo_list)
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Exiting...")

if __name__ == "__main__":
    main()
