from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from datetime import datetime, timedelta
import time

console = Console()

# Workday activities with durations (in hours)
activities = [
    ("☕ Morning coffee & emails", 0.5),
    ("💼 Team standup meeting", 0.5),
    ("⌨️  Deep work session", 2),
    ("🍽️  Lunch break", 1),
    ("📞 Client call", 1),
    ("⌨️  Coding/Project work", 2),
    ("📊 Status report", 0.5),
    ("📧 End-of-day emails", 0.5),
]

def simulate_workday():
    """
    Real-time workday timer for time management
    Each activity runs for its actual duration
    """
    start_time = datetime.now()
    
    console.print(Panel.fit(
        "[bold cyan]🏢 Workday Timer Starting[/bold cyan]\n"
        f"[dim]Start time: {start_time.strftime('%I:%M %p')}[/dim]\n"
        f"[dim]Total duration: 8 hours[/dim]",
        border_style="cyan"
    ))
    console.print()
    
    total_hours = sum(duration for _, duration in activities)
    total_seconds = total_hours * 3600
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeRemainingColumn(),
        console=console
    ) as progress:
        
        # Overall day progress
        day_task = progress.add_task(
            "[bold cyan]📅 Total WorkDay Progress", 
            total=total_seconds
        )
        
        for activity_name, duration_hours in activities:
            duration_seconds = duration_hours * 3600
            activity_start = datetime.now()
            expected_end = activity_start + timedelta(seconds=duration_seconds)
            
            console.print(f"\n[bold yellow]Starting:[/bold yellow] {activity_name}")
            console.print(f"[dim]Duration: {duration_hours} hours | Expected completion: {expected_end.strftime('%I:%M %p')}[/dim]\n")
            
            # Activity progress
            activity_task = progress.add_task(
                f"[yellow]{activity_name}", 
                total=duration_seconds
            )
            
            # Update every second for smooth progress
            elapsed = 0
            while elapsed < duration_seconds:
                time.sleep(1)
                elapsed += 1
                progress.update(activity_task, advance=1)
                progress.update(day_task, advance=1)
            
            progress.remove_task(activity_task)
            completion_time = datetime.now()
            console.print(f"[green]✓ Completed:[/green] {activity_name} [dim]at {completion_time.strftime('%I:%M %p')}[/dim]")
    
    # Summary
    end_time = datetime.now()
    actual_duration = end_time - start_time
    
    console.print()
    summary = Table(title="📋 Workday Summary", show_header=False)
    summary.add_column("Metric", style="cyan")
    summary.add_column("Value", style="green")
    
    summary.add_row("Start Time", start_time.strftime('%I:%M %p'))
    summary.add_row("End Time", end_time.strftime('%I:%M %p'))
    summary.add_row("Total Hours", f"{total_hours} hours")
    summary.add_row("Activities Completed", f"{len(activities)}")
    summary.add_row("Actual Duration", str(actual_duration).split('.')[0])
    
    console.print()
    console.print(summary)
    console.print(Panel.fit(
        "[bold green]🎉 Workday Complete![/bold green]\n"
        "[dim]Great job staying on track![/dim]",
        border_style="green"
    ))

if __name__ == "__main__":
    console.print("[bold]Press Ctrl+C to stop the timer at any time[/bold]\n")
    try:
        simulate_workday()
    except KeyboardInterrupt:
        console.print("\n[yellow]Timer stopped by user[/yellow]")