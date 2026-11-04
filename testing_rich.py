# Install rich first if needed:
# pip install rich

from rich import print
from rich.table import Table
from rich.console import Console
from rich.pretty import Pretty

# Create a console object for advanced printing
console = Console()

# Example variables
name = "Alice"
age = 30
balance = 1234.56
skills = ["Python", "Data Analysis", "Machine Learning"]

# 1. Simple rich print with colors
print(f"[bold green]Name:[/bold green] {name}")
print(f"[cyan]Age:[/cyan] {age}")
print(f"[yellow]Balance:[/yellow] ${balance:,.2f}")

# 2. Pretty print complex variables
console.print(Pretty(skills), style="magenta")

# 3. Display variables in a table
table = Table(title="User Profile")

table.add_column("Field", style="bold blue")
table.add_column("Value", style="bold white")

table.add_row("Name", name)
table.add_row("Age", str(age))
table.add_row("Balance", f"${balance:,.2f}")
table.add_row("Skills", ", ".join(skills))

console.print(table)

# 4. Syntax-highlighted code showing variable values
code_snippet = f"""
name = "{name}"
age = {age}
balance = {balance}
skills = {skills}
"""
console.print(code_snippet, style="bold white on black")