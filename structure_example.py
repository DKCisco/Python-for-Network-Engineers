import os
from rich import print as rprint

#CONSTANTS
DNS_SERVER = "8.8.8.8"

#Function/Classes
def say_hello():
    print("Hello")

def say_goodbye():
    print("GOODBYE")

class TestOSPF:
    pass

def main():
    say_hello()
    print(f"This DNS server is {DNS_SERVER}")
    say_goodbye()

if __name__ == "__main__":
    main()