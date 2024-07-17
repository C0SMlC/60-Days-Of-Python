print("Hello World")

# Basic TODO

tasks = []

def printList(tasks):
    for index, value in enumerate(tasks):
        print(index + 1, value)

while True:
    prompt = "Add, View, Edit or Delete a Task or type 'exit' to quit: "
    userInput = input(prompt).strip().capitalize()

    match userInput:
        case "Add":
            task = input("Task: ")
            tasks.append(task)
        case "View":
            printList(tasks)
        case "Edit":
            try:
                index = int(input("Enter the task index to edit: ")) - 1
                if 0 <= index < len(tasks):
                    new_task = input("New Task: ")
                    tasks[index] = new_task
                else:
                    print("Invalid index")
            except ValueError:
                print("Please enter a valid number")
        case "Delete":
            try:
                index = int(input("Enter the task index to delete: ")) -1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                else:
                    print("Invalid index")
            except ValueError:
                print("Please enter a valid number")
        case "Exit":
            break
        case _:
            print("Invalid Input")
