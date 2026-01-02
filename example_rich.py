"""
Rich CRM Demo - Terminal UI library
Rich provides rich text and beautiful formatting in the terminal
Note: Rich is a library, not a full GUI framework, so this is a simplified demo
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.progress import Progress, BarColumn, TextColumn
from rich.prompt import Prompt, Confirm
from rich import box
import time

console = Console()

def show_dashboard():
    """Display performance dashboard."""
    console.clear()
    
    # Header
    console.print(Panel.fit("[bold cyan]Enterprise Data Overview[/bold cyan]", border_style="cyan"))
    console.print()
    
    # Metrics
    metrics_table = Table.grid(padding=2)
    metrics_table.add_column(style="cyan", justify="center")
    metrics_table.add_column(style="green", justify="center")
    metrics_table.add_column(style="red", justify="center")
    
    metrics_table.add_row(
        "[bold]Global Sales[/bold]\n$1.28M",
        "[bold]Conversion[/bold]\n18.4%",
        "[bold]Pending Tasks[/bold]\n14"
    )
    
    console.print(metrics_table)
    console.print()
    
    # Progress bar
    console.print("[bold]System Synchronization State[/bold]")
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("Synchronizing...", total=100)
        progress.update(task, completed=72)
    
    console.print()

def show_customer_registry():
    """Display customer registry."""
    console.clear()
    console.print(Panel.fit("[bold cyan]Customer Registry[/bold cyan]", border_style="cyan"))
    console.print()
    
    # Create table
    table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("ID", style="cyan", width=6)
    table.add_column("Organization", style="green", width=20)
    table.add_column("Sector", style="yellow", width=10)
    table.add_column("Revenue", style="blue", width=12)
    table.add_column("Score", style="red", width=8)
    
    # Add rows
    for i in range(1, 16):
        table.add_row(
            str(100 + i),
            f"Client {i} Corp",
            "Tech",
            f"${i*10}k",
            f"{70+i}%"
        )
    
    console.print(table)
    console.print()

def show_admin_form():
    """Display admin form."""
    console.clear()
    console.print(Panel.fit("[bold cyan]System Administration[/bold cyan]", border_style="cyan"))
    console.print()
    console.print("[bold]Global Client Registry Entry[/bold]")
    console.print()
    
    # Form fields (simulated)
    org_name = Prompt.ask("[cyan]Organization Lead Name[/cyan]")
    notes = Prompt.ask("[cyan]Relationship History / Notes[/cyan]")
    industry = Prompt.ask(
        "[cyan]Industry Vertical[/cyan]",
        choices=["Finance", "Healthcare", "Tech", "Education"],
        default="Tech"
    )
    strategy = Prompt.ask(
        "[cyan]Market Strategy[/cyan]",
        choices=["B2B (Enterprise)", "B2C (Retail)"],
        default="B2B (Enterprise)"
    )
    billing = Confirm.ask("[cyan]Enable Advanced Billing Tier[/cyan]", default=False)
    web_visible = Confirm.ask("[cyan]ACCOUNT VISIBLE ON WEB PORTAL[/cyan]", default=False)
    priority = Prompt.ask("[cyan]Engagement Priority (0-100)[/cyan]", default="50")
    seats = Prompt.ask("[cyan]Dedicated Seat Count[/cyan]", default="10")
    contract_date = Prompt.ask("[cyan]Contract Start Date (YYYY-MM-DD)[/cyan]")
    meeting_time = Prompt.ask("[cyan]Preferred Meeting Time (HH:MM)[/cyan]")
    
    console.print()
    console.print(Panel.fit(
        f"[green]Entry Submitted Successfully![/green]\n\n"
        f"Organization: {org_name}\n"
        f"Industry: {industry}\n"
        f"Strategy: {strategy}\n"
        f"Priority: {priority}\n"
        f"Seats: {seats}",
        title="Success",
        border_style="green"
    ))

def main():
    """Main menu."""
    while True:
        console.clear()
        console.print(Panel.fit(
            "[bold cyan]Rich CRM Demo[/bold cyan]\n"
            "[dim]Terminal UI Library - Simplified Demo[/dim]",
            border_style="cyan"
        ))
        console.print()
        console.print("[1] Performance Dashboard")
        console.print("[2] Customer Registry")
        console.print("[3] System Administration")
        console.print("[q] Quit")
        console.print()
        
        choice = Prompt.ask("[cyan]Select option[/cyan]", choices=["1", "2", "3", "q"], default="1")
        
        if choice == "1":
            show_dashboard()
            Prompt.ask("\n[dim]Press Enter to continue...[/dim]")
        elif choice == "2":
            show_customer_registry()
            Prompt.ask("\n[dim]Press Enter to continue...[/dim]")
        elif choice == "3":
            show_admin_form()
            Prompt.ask("\n[dim]Press Enter to continue...[/dim]")
        elif choice == "q":
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Exiting...[/yellow]")
