def load_todos():
	with open('todos.txt', 'r') as file:
		return [line.strip().split('|') for line in file.readlines()]

def save_todos(todos):
	with open('todos.txt', 'w') as file:
		for todo in todos:
			file.write(f"{todo[0]}|{todo[1]}\n")

def show_todos(todos):
	if not todos:
		print("No tasks found!")
		return
	print("\nYour TODO List:")
	for i, todo in enumerate(todos, 1):
		status = "✓" if todo[1] == "completed" else " "
		print(f"{i}. [{status}] {todo[0]}")

def add_todo(todos):
	task = input("Enter new task: ")
	todos.append([task, "pending"])
	save_todos(todos)
	print("Task added successfully!")

def change_state(todos):
	show_todos(todos)
	if not todos:
		return
	index = int(input("Enter task number to toggle status: ")) - 1
	todos[index][1] = "completed" if todos[index][1] == "pending" else "pending"
	save_todos(todos)
	print("Task status updated!")

def remove_todo(todos):
	show_todos(todos)
	if not todos:
		return
	index = int(input("Enter task number to remove: ")) - 1
	removed_task = todos.pop(index)
	save_todos(todos)
	print(f"Removed task: {removed_task[0]}")

todos = load_todos()
while True:
	print("\n=== TODO App ===")
	print("1. Show tasks")
	print("2. Add task")
	print("3. Toggle task status")
	print("4. Remove task")
	print("5. Exit")
	
	choice = input("Enter your choice (1-5): ")
	
	if choice == '1':
		show_todos(todos)
	elif choice == '2':
		add_todo(todos)
	elif choice == '3':
		change_state(todos)
	elif choice == '4':
		remove_todo(todos)
	elif choice == '5':
		print("Goodbye!")
		break
	else:
		print("Invalid choice! Please try again.")