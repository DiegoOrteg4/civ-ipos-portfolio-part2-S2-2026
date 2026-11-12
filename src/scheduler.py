import schedule
import time
import threading
from datetime import datetime
from rich.console import Console 

console = Console()

def check_due_tasks(tasks):
    """
    Check tasks that are due.

    """
    print("\nChecking scheduled tasks...")

    today = datetime.now().strftime("%d-%m-%Y")

    for task in tasks:
        if task.due_date <= today and task.status != "Completed":
            console.print(f"Reminder: [bold red] {task.title} [/bold red] is due today!")

        else:
            console.print(f"[bold green] No overdue tasks found! Keep it up champ!")


def run_scheduler():
    """
    Run scheduled tasks in the background.
    """
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_scheduler(tasks):
    """
    Start the scheduler in a separate thread.
    """
    schedule.every(10).seconds.do(check_due_tasks, tasks)

    thread = threading.Thread(
        target=run_scheduler,
        daemon=True
    )

    thread.start()