# TODO App

A simple command-line TODO application written in Python. This app allows users to manage their tasks by adding, viewing, updating, and removing tasks. The tasks and their statuses are saved in a text file (`todos.txt`) for persistence.

---

## Features
1. **Show Tasks**: Display all tasks with their statuses (pending or completed).
2. **Add Task**: Add a new task to the TODO list.
3. **Toggle Task Status**: Mark a task as completed or set it back to pending.
4. **Remove Task**: Delete a task from the list.
5. **Persistent Storage**: Tasks are saved in a `todos.txt` file and loaded each time the app runs.

---

## Prerequisites
- Python 3.x installed on your system.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/todo-app.git
   ```
2. Navigate to the project folder:
   ```bash
   cd todo-app
   ```
3. Create a `todos.txt` file in the same directory if it does not already exist:
   ```bash
   touch todos.txt
   ```

---

## Usage
1. Run the script:
   ```bash
   python todo_app.py
   ```
2. Follow the on-screen menu to manage your tasks:
   - Press `1` to view tasks.
   - Press `2` to add a task.
   - Press `3` to toggle a task's status (pending/completed).
   - Press `4` to remove a task.
   - Press `5` to exit the application.

---

## File Format
Tasks are stored in the `todos.txt` file. Each line represents a task and its status in the following format:

```
Task Description|status
```

- `Task Description`: The task you have added.
- `status`: Either `pending` or `completed`.

Example:
```
Buy groceries|pending
Pay bills|completed
```

---

## Example Interaction
```plaintext
=== TODO App ===
1. Show tasks
2. Add task
3. Toggle task status
4. Remove task
5. Exit
Enter your choice (1-5): 1

Your TODO List:
0. [ ] Buy groceries
1. [✓] Pay bills

Enter your choice (1-5): 2
Enter new task: Call the plumber
Task added successfully!

Enter your choice (1-5): 1

Your TODO List:
0. [ ] Buy groceries
1. [✓] Pay bills
2. [ ] Call the plumber

Enter your choice (1-5): 3
Enter task number to toggle status: 2
Task status updated!

Enter your choice (1-5): 1

Your TODO List:
0. [ ] Buy groceries
1. [✓] Pay bills
2. [✓] Call the plumber

Enter your choice (1-5): 5
Goodbye!
```

---

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
