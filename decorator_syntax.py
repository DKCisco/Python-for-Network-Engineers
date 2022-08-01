import re
from textwrap import wrap
from rich import print as rprint

def prettify(func):
    def wrapper():
        rprint("[cyan]*******[/cyan]")
        func()
        rprint("[cyan]*******[/cyan]")

    return wrapper

def banner():
    print("Do not access this device unless you are authorized!")

@prettify
def banner():
    print("Do not access this device unless you are authorized!")

banner()

def double_call(func):
    def inner():
        func
        func
    return inner

@double_call
def nuggetlove():
    print("I love CBT Nuggets!")

print(nuggetlove())
    