from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.layout import Layout
from datetime import datetime, timedelta
import time
import threading

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

# Global variables for display
current_time_str = ""
current_date_str = ""
current_greeting = ""
workday_complete = False
completion_stats = None

def get_greeting(current_hour):
    """Return greeting based on time of day"""
    if 6 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 17:
        return "Good Afternoon"
    elif 17 <= current_hour < 20:
        return "Good Evening"
    else:
        return "Good Night"

def update_time_display():
    """Continuously update time and date display"""
    global current_time_str, current_date_str, current_greeting
    while True:
        now = datetime.now()
        # Use #d for Windows compatibility (removes leading zero)
        day = now.day
        current_date_str = now.strftime(f"%A, {day} %B %Y")
        current_time_str = now.strftime("%I:%M:%S %p")
        current_greeting = get_greeting(now.hour)
        time.sleep(1)

def print_header():
    """Print the date, time, and greeting header"""
    console.clear()
    console.print(f"[bold cyan]{current_date_str}[/bold cyan]")
    console.print(f"[bold yellow]{current_time_str}[/bold yellow] [dim]-[/dim] [bold green]{current_greeting}[/bold green]")
    console.print()

def run_workday_timer():
    """
    Real-time workday timer for time management
    Each activity runs for its actual duration
    """
    global workday_complete, completion_stats
    
    start_time = datetime.now()
    
    print_header()
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
            "[bold cyan]📅 Total Day Progress", 
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
    
    workday_complete = True
    completion_stats = {
        'start_time': start_time,
        'end_time': end_time,
        'total_hours': total_hours,
        'activities': len(activities),
        'duration': actual_duration
    }

def display_completion_stats():
    """Display previous workday completion stats"""
    if completion_stats:
        print_header()
        console.print(Panel.fit(
            "[bold green]Previous Workday Complete[/bold green]\n"
            f"[dim]Completed on {completion_stats['end_time'].strftime('%A, ')}{completion_stats['end_time'].day} {completion_stats['end_time'].strftime('%B %Y')}[/dim]",
            border_style="green"
        ))
        console.print()
        
        summary = Table(title="📋 Last Workday Summary", show_header=False)
        summary.add_column("Metric", style="cyan")
        summary.add_column("Value", style="green")
        
        summary.add_row("Start Time", completion_stats['start_time'].strftime('%I:%M %p'))
        summary.add_row("End Time", completion_stats['end_time'].strftime('%I:%M %p'))
        summary.add_row("Total Hours", f"{completion_stats['total_hours']} hours")
        summary.add_row("Activities Completed", f"{completion_stats['activities']}")
        summary.add_row("Actual Duration", str(completion_stats['duration']).split('.')[0])
        
        console.print(summary)
        console.print()
        console.print("[dim]Workday timer will start at 8:00 AM[/dim]")

def main():
    """Main program loop"""
    global workday_complete, completion_stats
    
    # Start time display thread
    time_thread = threading.Thread(target=update_time_display, daemon=True)
    time_thread.start()
    
    # Wait for time display to initialize
    time.sleep(1)
    
    console.print("[bold]Workday Timer - Press Ctrl+C to exit[/bold]\n")
    
    try:
        while True:
            now = datetime.now()
            current_hour = now.hour
            current_minute = now.minute
            weekday = now.weekday()  # 0=Monday, 6=Sunday
            
            # Saturday (5) or Sunday (6)
            if weekday in [5, 6]:
                print_header()
                day = now.day
                console.print(Panel.fit(
                    f"[bold cyan]Weekend Day - {now.strftime('%A')}[/bold cyan]",
                    border_style="cyan"
                ))
                console.print()
                
                response = console.input("[bold yellow]Shall I run the workday timer? (Y or N):[/bold yellow] ").strip().upper()
                
                if response == 'Y':
                    console.print("[green]Starting workday timer now...[/green]\n")
                    time.sleep(2)
                    run_workday_timer()
                    
                    # After completion, display stats and wait
                    while True:
                        now = datetime.now()
                        if now.hour == 7 and now.minute == 55:
                            workday_complete = False
                            break
                        display_completion_stats()
                        time.sleep(30)
                else:
                    console.print("[yellow]Workday timer will not run today.[/yellow]")
                    console.print("[dim]Waiting for next check...[/dim]\n")
                    time.sleep(60)
            
            # Weekday - check if it's time to start (8:00 AM)
            elif current_hour == 8 and current_minute == 0 and not workday_complete:
                run_workday_timer()
            
            # Before 7:55 AM and workday was completed yesterday
            elif current_hour < 7 or (current_hour == 7 and current_minute < 55):
                if workday_complete:
                    display_completion_stats()
                    time.sleep(30)
                else:
                    print_header()
                    console.print(f"[dim]Workday timer will start at 8:00 AM[/dim]\n")
                    time.sleep(30)
            
            # At 7:55 AM, reset for new day
            elif current_hour == 7 and current_minute == 55:
                workday_complete = False
                completion_stats = None
                print_header()
                console.print("[yellow]New workday starting soon...[/yellow]\n")
                time.sleep(60)
            
            # Between 7:55 AM and 8:00 AM
            elif current_hour == 7 and current_minute > 55:
                print_header()
                console.print("[yellow]Workday timer starting soon at 8:00 AM...[/yellow]\n")
                time.sleep(30)
            
            # After 8:00 AM but before completion
            else:
                print_header()
                console.print("[dim]Waiting for workday timer...[/dim]\n")
                time.sleep(30)
    
    except KeyboardInterrupt:
        console.print("\n[yellow]Timer stopped by user[/yellow]")

if __name__ == "__main__":
    main()