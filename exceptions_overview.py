from typing import final


try:
    database.open()
    x = 13
    z = x + 5
    print(z)
except NameError:
    print("Can't print this because of a name error. The value is not defined")
except Exception:
    print("Some unknown exception")
else:
    print("We have no problems here let's go and print Y now")

finally:
    database.close()

y = "john"
print(y)

