import json
print("sdf")
# tasks = [{'task' , 'status', 'deadline'}]
def load_task():
    try:
        with open("tasks.txt", "r") as file:
            content = file.read().strip()
            if not content:   # file is empty
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    
def save_data(task):
    with open('tasks.txt' , 'w') as file:
        json.dump(task , file)

def view_task(task):
    for i , tsk in enumerate(task , start=1):
        print(f"{i}. Task: {tsk['task']} , Status: {tsk['status']} , Deadline: {tsk['deadline']}")

def delete_task(task):
    view_task(task)
    try:
        index = int(input("Enter task to be delete: ")) - 1
        if 0 <= index < len(task):
            task.pop(index)
            save_data(task)
        else:
            print("Invalid index.")
    except ValueError:
        print("Enter valid number.")


def change_status(task):
    view_task(task)
    try:
        idx = int(input("Enter task number to change status: ")) - 1
        if 0 <= idx < len(task):
            new_status = input("Enter new current status: ")
            task[idx]['status'] = new_status
            save_data(task)
        else:
            print("Enter valid index.")
    except ValueError:
        print("Enter valid number.")


def add_task(task):
    tsk = input("Enter task: ")
    status = input("Enter current status: ")
    deadline = input("Enter Deadline of the task(DD-MM-YYYY): ")
    temp_task = {'task': tsk , 'status' : status , 'deadline' : deadline}
    task.append(temp_task)
    save_data(task)

def main():
    while True:
        tasks = load_task()
        print("\n=====WELCOME TO YOUR TODO LIST=====")
        print("1. View all task")
        print("2. Add new task")
        print("3. Change status")
        print("4. Delete task ")
        print("5. Exit")
        print("==================================")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                view_task(tasks)
            case 2:
                add_task(tasks)
            case 3:
                change_status(tasks)
            case 4:
                delete_task(tasks)
            case 5:
                break
            case _:
                print("Invalid choice. ")


if __name__ == "__main__":
    main()
# main()