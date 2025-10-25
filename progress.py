from rich.console import Console
from rich.progress import track

console = Console()

console.print("[bold cyan]Day Progress[/bold cyan]")

for step in track(range(28800),
description="Processing..."):
    # Simulate some work with a sleep
    import time
    time.sleep(1)
    pass
console.print("[bold green]Processing complete![/bold green]")
