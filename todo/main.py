import json
from datetime import datetime
# creating the json file
def writer(todo):
        with open("exp.json","w") as file:
            json.dump(todo,file,indent=4)
# getting data from file
def reader():
    try:
        with open("exp.json","r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError,json.JSONDecodeError):
        return []
# add todo
def addTodo():
    print(f'''
========================
    Add Todo
========================
''')
    while True :
        task = input("Enter the task or 'q' to quit: ").strip().lower()
        if task.lower() == "q":
            print("Todo cancelled.")
            return
        elif task == "":
            print("Task can not be empty")
        else:
            break

    while True:
        priority = input("Enter the priority or 'q' to quit: ").strip().lower()
        if priority.lower() == "q":
            print("Todo cancelled.")
            return
        elif priority == "":
            print("Priority can not be empty")
        elif priority != "high" and priority != "low" and priority != "mid":
            print("invalid priority('high','low','mid')")
        else:
            break
    while True:
        due_date = input("Enter due date(DD-MM-YYYY) or 'q' to quit: ").strip()
        if due_date.lower() == 'q':
            print("Todo cancelled")
            return
        try:
            due_date = datetime.strptime(due_date,"%d-%m-%Y")
            today = datetime.now()
            if due_date.date() < today.date():
                print("Due date cannot be in the past.")
                continue
            due_date = due_date.strftime("%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date. Use DD-MM-YYYY.")

    prev_todo = reader()
    todo = {
        "id":max((todo.get("id") for todo in prev_todo),default=0) + 1 ,
        "task":task,
        "priority":priority,
        "status":"pending",
        "due_date":due_date,
        "craeted_at":datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }
    prev_todo.append(todo)
    writer(prev_todo)
    print(f"todo {max(todo["id"] for todo in prev_todo) + 1} successfully added")
# exit||continue
def continue_or_exit():
    while True:
        choice = input("Do you want to continue? (y/n): ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Please enter y or n")
# view todo
def view_todo():
    todos = reader()
    print(f'''
========================
    All Tasks
========================
''')
    check_todo(todos)
    print(
    f"{'ID':<5}"
    f"{'Task':<25}"
    f"{'Priority':<12}"
    f"{'Status':<12}"
    f"{'Due Date':<15}"
)
    print("-" * 69)
    for todo in todos:
        print(
            f"{todo['id']:<5}"
            f"{todo['task']:<25}"
            f"{todo['priority']:<12}"
            f"{todo['status']:<12}"
            f"{todo['due_date']:<15}"
        )
# check expense
def check_todo(exp):
    if len(exp) < 1:
        print("You have no expense")
# complete task
def complete_task():
    todos = reader()
    pending_task = [todo for todo in todos if todo["status"] == "pending" ]
    if not pending_task:
        print("all tasks are completed")
        return
    for tasks in pending_task:
        print(f"============{tasks["id"]}===========")
        print(f"Task: {tasks["task"]}")
        print(f"Priority: {tasks["priority"]}")
        print(f"status: {tasks["status"]}")
        print(f"due_date: {tasks["due_date"]}\n")
    while True:
        user_input = input("Enter the id you want to mark as complete  or 'q' to quit: ").strip()
        if user_input.lower() == "q":
            print("Expense cancelled.")
            return
        try:
            input_id = int(user_input)
            break
        except ValueError:
            print("id should be a number.")
    for todo in todos:
        if todo["id"] == input_id:
            todo["status"] = "completed"
    writer(todos)
# edit task
def edit_todo():
    todos = reader()
    if len(todos) < 1:
        check_todo(todos)
        return
    id = []
    print(
    f"{'ID':<5}"
    f"{'Task':<25}"
    f"{'Priority':<12}"
    f"{'Status':<12}"
    f"{'Due Date':<15}"
)
    print("-" * 69)
    for todo in todos:
        id.append(todo["id"])
        print(
            f"{todo['id']:<5}"
            f"{todo['task']:<25}"
            f"{todo['priority']:<12}"
            f"{todo['status']:<12}"
            f"{todo['due_date']:<15}"
        )
    while True: 
        userInput = input("select the expense you want to edit or (e) to exit ").strip().lower()
        if userInput == "e":
            return
        try:
            userInput = int(userInput)
        except ValueError:
            print("Please enter a number or 'e'.")
            continue
        if userInput not in id:
            print("select from the above id")
            edit_todo()
            return
        while True :
            task = input("Enter the task or 'q' to quit: ").strip().lower()
            if task.lower() == "q":
                print("Todo cancelled.")
                return
            else:
                break

        while True:
            priority = input("Enter the priority or 'q' to quit: ").strip().lower()
            if priority.lower() == "q":
                print("Todo cancelled.")
                return
            elif priority != "high" and priority != "low" and priority != "mid":
                print("invalid priority('high','low','mid')")
            else:
                break

        while True:
            due_date = input("Enter due date(DD-MM-YYYY) or 'q' to quit: ").strip()
            if due_date.lower() == 'q':
                print("Todo cancelled")
                return
            try:
                due_date = datetime.strptime(due_date,"%d-%m-%Y")
                today = datetime.now()
                if due_date.date() < today.date():
                    print("Due date cannot be in the past.")
                    continue
                due_date = due_date.strftime("%d-%m-%Y")
                break
            except ValueError:
                print("Invalid date. Use DD-MM-YYYY.")

        while True:
            status = input("Enter the status or 'q' to quit: ").strip().lower()
            if status == 'q':
                print("edit canclled")
            elif status != "completed" and status != "pending" and status != "cancelled":
                print("invalid status('completed','pending','cancelled')")
            else:
                break

        for todo in todos:
            if userInput == todo["id"]:
                if task == "":
                    todo["task"] = todo["task"]
                else :
                    todo["task"] = task
                if priority == "":
                    todo["priority"] = todo["priority"]
                else:
                    todo["priority"] = priority
                if due_date == "":
                    todo["due_date"] = todo["due_date"]
                else:
                    todo["due_date"] = due_date
                if status == "":
                    todo["status"] = todo["status"]
                else:
                    todo["status"] = status
        
        writer(todos)
        print(f"todo {userInput} Successfully edited")
        break
# delete Expense 
def delete_todo():
    todos = reader()
    if len(todos) < 1:
        check_todo(todos)
        return
    id = []
    check_todo(todos)
    print(
    f"{'ID':<5}"
    f"{'Task':<25}"
    f"{'Priority':<12}"
    f"{'Status':<12}"
    f"{'Due Date':<15}"
)
    print("-" * 69)
    for todo in todos:
        id.append(todo["id"])
        print(
            f"{todo['id']:<5}"
            f"{todo['task']:<25}"
            f"{todo['priority']:<12}"
            f"{todo['status']:<12}"
            f"{todo['due_date']:<15}"
        )
    while True:
        userInput = input("enter the value you want to delete of (e) to quit ")
        if userInput == "e":
            return
        try:
            userInput = int(userInput)
        except ValueError:
            print("Please enter a number or 'e'.")
            continue
        if userInput not in id:
            print("select from the above id")
            delete_todo()
            return
        for index,todo in enumerate(todos):
            if userInput == todo["id"]:
                del todos[index]
                writer(todos)
                return
# filter task
def filter_todo():
    todos = reader()
    if len(todos) < 1:
        check_todo(todos)
        return
    while True:
        print(f'''
=======================
    Select Filter
=======================

[1] single filter
[2] multiple filter
''')
        userInput = input(
            "Select from the option above or (q) to quit: "
        ).strip().lower()
        if userInput == "q":
            return
        try:
            userInput = int(userInput)
        except ValueError:
            print("your input must be between the above list")
            continue
        # SINGLE FILTER
        if userInput == 1:
            print(f'''
=======================
    Single Filter
=======================

[1] priority filter
[2] status filter
''')
            userInput = input(
                "Select from the option above or (q) to quit: "
            ).strip().lower()
            if userInput == "q":
                return
            try:
                userInput = int(userInput)
            except ValueError:
                print("your input must be between the above list")
                continue
            if userInput == 1:
                priority_input = input(
                    "Enter the priority name or (q) to quit: "
                ).strip().lower()
                if priority_input == "q":
                    return
                if priority_input.isalpha():
                    single_filter(
                        todos,
                        filter_type="priority",
                        user_input=priority_input
                    )
                    break
                else:
                    print("Invalid priority name")
                    continue
            elif userInput == 2:
                status_input = input(
                    "Enter the status or (q) to quit: "
                ).strip().lower()
                if status_input == "q":
                    return
                single_filter(
                    todos,
                    filter_type="status",
                    user_input=status_input
                )
                break
        # MULTIPLE FILTER
        elif userInput == 2:
            print(f'''
=======================
    Multiple Filter
=======================
[1] priority and status
''')
            userInput = input(
                "Select from the option above or (q) to quit: "
            ).strip().lower()
            if userInput == "q":
                return
            try:
                userInput = int(userInput)
            except ValueError:
                print("your input must be between the above list")
                continue
            if userInput == 1:
                print("Usage:")
                print("priority,status")
                print("high,completed")
                print("low,pending")
                try:
                    multiple_filter_priority, multiple_filter_status = (
                        input(
                            "Enter priority and status: "
                        ).strip().lower().split(",")
                    )
                    multiple_filter(
                        todos,
                        multiple_filter_priority,
                        multiple_filter_status
                    )
                    return
                except ValueError:
                    print("Expected: priority,amount")
                    continue
            else:
                print("Invalid list number")
# single filter
def single_filter(todos, filter_type, user_input):
    if filter_type == "priority":
        priority = {todo["priority"] for todo in todos}
        if user_input not in priority:
            print("Invalid priority name")
            print("Available priority:")
            for prio in priority:
                print(prio)
            return
        print(
            f"{'ID':<5}"
            f"{'Task':<25}"
            f"{'Priority':<12}"
            f"{'Status':<12}"
            f"{'Due Date':<15}"
        )
        print("-" * 69)
        for todo in todos:
            if user_input == todo["priority"]:
                print(
                    f"{todo['id']:<5}"
                    f"{todo['task']:<25}"
                    f"{todo['priority']:<12}"
                    f"{todo['status']:<12}"
                    f"{todo['due_date']:<15}"
                )
    elif filter_type == "status":
        status = {todo["status"] for todo in todos}
        if user_input not in status:
            print("Invalid status")
            print("Available status:")
            for stat in status:
                print(stat)
            return
        print(
            f"{'ID':<5}"
            f"{'Task':<25}"
            f"{'Priority':<12}"
            f"{'Status':<12}"
            f"{'Due Date':<15}"
        )
        print("-" * 69)
        for todo in todos:
            if user_input == todo["status"]:
                print(
                    f"{todo['id']:<5}"
                    f"{todo['task']:<25}"
                    f"{todo['priority']:<12}"
                    f"{todo['status']:<12}"
                    f"{todo['due_date']:<15}"
                )
# multiple filter
def multiple_filter(todos, priority, status):
    priorities = {todo["priority"] for todo in todos}
    statuses = {todo["status"] for todo in todos}
    if priority not in priorities:
        print("Invalid priority")
        print("Available priorities:")
        for prio in priorities:
            print(prio)
        return
    if status not in statuses:
        print("Invalid status")
        print("Available statuses:")
        for stat in statuses:
            print(stat)
        return
    print(
        f"{'ID':<5}"
        f"{'Task':<25}"
        f"{'Priority':<12}"
        f"{'Status':<12}"
        f"{'Due Date':<15}"
    )
    print("-" * 69)
    found = False
    for todo in todos:
        if (
            todo["priority"] == priority
            and todo["status"] == status
        ):
            found = True
            print(
                f"{todo['id']:<5}"
                f"{todo['task']:<25}"
                f"{todo['priority']:<12}"
                f"{todo['status']:<12}"
                f"{todo['due_date']:<15}"
            )
    if not found:
        print("No todo matches both filters.")
# main
def main():
    while True:
        print(
'''
========================
    Todo CLI
========================
[1] Add task
[2] View tasks
[3] Complete task
[4] Edit task
[5] Delete task
[6] Filter tasks
[7] Exit

'''
        )

        try:
            userInput = int(input("Select an option: "))

        except ValueError:
            print("\nPlease enter a number.")
            continue
        if userInput == 7:
            return
        elif userInput == 1:
            addTodo()
        elif userInput == 2:
            view_todo()
        elif userInput == 3:
            complete_task()
        elif userInput == 4:
            edit_todo()
        elif userInput == 5:
            delete_todo()
        elif userInput == 6:
            filter_todo()
        else:
            print("select from the listed options")

        if not continue_or_exit():
            print("Goodbye!")
            return

if __name__ == "__main__":
    main()