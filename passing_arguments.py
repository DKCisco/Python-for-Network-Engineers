from rich import print as rprint

def politeness(func):
    def wrapper():
        rprint("[yellow]Hello, thank you for using my code! [/yellow]")
        func()
        rprint("[green]Thanks again! See you soon! [/green]")
    return wrapper

