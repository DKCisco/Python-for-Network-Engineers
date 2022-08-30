"""
Fixing example of what not to do for pylint

"""
import os
import ntp_stuff

MY_CONSTANT = 7

def capital_function():
    """This function prints stuff"""
    print("bad function")

print("This is a really really really really really really really really really really really really really really really really really really really long line")
print(MY_CONSTANT)
ntp_stuff.ntp_server()

class BetterClass:
    """Demo docstring"""