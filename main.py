from src.task_manager import add_task, delete_task, list_tasks
from src.file_handler import load_tasks
from rich import print 
from rich.table import Table
from rich.console import Console
from rich.pretty import Pretty


def main():
    tasks = load_tasks()
    console = Console()
    while True:
        table = Table(title="Task Manager CLI")

        table.add_column("No.", style="blue")
        table.add_column("Task Option", style="")
        
        table.add_row("1", "Add Task", style="green")
        table.add_row("2", "Delete Task",style="red")
        table.add_row("3", "List Tasks", style="blue")
        table.add_row("4", "Exit", style="yellow")

        console.print(table)

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (DD-MM-YYYY): ")
            add_task(tasks, title, description, due_date)
        elif choice == "2":
            title = input("Title of the task to delete: ")
            if delete_task(tasks, title):
                print(f"[bold green]""Task deleted successfully.")
            else:
                print(f"[bold red]""Task not found.")
        elif choice == "3":
            list_tasks(tasks)
        elif choice == "4":
            print(f"[bold magenta]""Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
