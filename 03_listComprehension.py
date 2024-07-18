todos = ["1-Hello World", "2-New World", "3-Welcome to JS"]
newTododsWithoutHypen = [item.replace("-", ".") for item in todos]
print(newTododsWithoutHypen)
