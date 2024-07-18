print("Hello World")

# Basic TODO

file = open('todos.txt','r')
tasks = file.readlines()
file.close()

def printList(tasks):
    for index, value in enumerate(tasks):
        print(index + 1, value.strip('\n'))


while True:
    prompt = "Add, View, Edit or Delete a Task or type 'exit' to quit: "
    userInput = input(prompt).strip().capitalize()

    match userInput:
        case "Add":
            task = input("Task: ")
            tasks.append(task)
            file = open("todos.txt", 'w')
            file.writelines(tasks)
            file.close()
        case "View":
            printList(tasks)
        case "Edit":
            try:
                index = int(input("Enter the task index to edit: ")) - 1
                if 0 <= index < len(tasks):
                    new_task = input("New Task: ") + "\n"
                    tasks[index] = new_task
                    file = open("todos.txt", 'w')
                    file.writelines(tasks)
                    file.close()
                else:
                    print("Invalid index")
            except ValueError:
                print("Please enter a valid number")
        case "Delete":
            try:
                index = int(input("Enter the task index to delete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    file = open("todos.txt", 'w')
                    file.writelines(tasks)
                    file.close()
                else:
                    print("Invalid index")
            except ValueError:
                print("Please enter a valid number")
        case "Complete":
            try:
                index = int(input("Enter the task index to complete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index] = tasks[index] + " (Completed)"
                else:
                    print("Invalid index")
            except ValueError:
                print("Please enter a valid number")
        case "Exit":
            break
        case _:
            print("Invalid Input")
