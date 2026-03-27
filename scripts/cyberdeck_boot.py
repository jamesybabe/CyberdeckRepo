from time import sleep
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.live import Live
from rich.layout import Layout
from rich.text import Text


console = Console()


def boot_sequence() -> None:
    steps = [
        "Initialising cyberdeck core",
        "Checking power systems",
        "Mounting local storage",
        "Scanning wireless interfaces",
        "Loading navigation tools",
        "Establishing terminal environment",
        "System ready",
    ]

    console.clear()
    console.rule("[bold green]CYBERDECK BOOT")

    for step in steps:
        console.print(f"[green]>[/green] {step} ... [bold green]OK[/bold green]")
        sleep(0.6)

    sleep(0.8)


def make_layout() -> Layout:
    layout = Layout()

    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main"),
        Layout(name="footer", size=3),
    )

    layout["main"].split_row(
        Layout(name="left"),
        Layout(name="right"),
    )

    return layout


def render_header() -> Panel:
    title = Text("RASPBERRY PI CYBERDECK", style="bold green")
    return Panel(Align.center(title), border_style="green")


def render_left_panel(current_time: str) -> Panel:
    table = Table.grid(padding=(0, 1))
    table.add_row("Status", "[bold green]ONLINE[/bold green]")
    table.add_row("User", "pi")
    table.add_row("Mode", "Field Prototype")
    table.add_row("Time", current_time)
    table.add_row("GPS", "No Fix")
    table.add_row("Wi-Fi", "Connected")
    table.add_row("Battery", "87%")

    return Panel(table, title="System", border_style="green")


def render_right_panel() -> Panel:
    art = Text()
    art.append("      _____________\n", style="green")
    art.append("     /  CYBERDECK  \\\n", style="green")
    art.append("    /_______________\\\n", style="green")
    art.append("    |  [====] [==] |\n", style="green")
    art.append("    |  TERMINAL    |\n", style="green")
    art.append("    |  NAV   COMMS |\n", style="green")
    art.append("    |______________|\n", style="green")
    art.append("       /   /\\   \\\n", style="green")
    art.append("      /___/  \\___\\\n", style="green")

    return Panel(Align.center(art), title="Visual", border_style="green")


def render_footer() -> Panel:
    text = "[bold green]Tip:[/bold green] This is your first repo-to-VM test run."
    return Panel(Align.center(text), border_style="green")


def run_dashboard() -> None:
    layout = make_layout()

    with Live(layout, refresh_per_second=2, screen=True):
        for _ in range(60):
            current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            layout["header"].update(render_header())
            layout["left"].update(render_left_panel(current_time))
            layout["right"].update(render_right_panel())
            layout["footer"].update(render_footer())
            sleep(0.5)


if __name__ == "__main__":
    boot_sequence()
    run_dashboard()
    console.clear()
    console.print(Panel.fit("[bold green]Session ended[/bold green]", border_style="green"))