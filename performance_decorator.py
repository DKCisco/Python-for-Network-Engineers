from time import perf_counter
from turtle import st

print(perf_counter())

start = perf_counter()

finish = perf_counter()

print(start)
print(finish)

performance = finish - start

print(performance)

def performance_test(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        finish = perf_counter()
        performance = finish - start
        print(f"Execution time: {performance}")

    return wrapper

@performance_test
def print_some_numbers(num):
    for i in range (0, num):
        print(i)

print_some_numbers(1000000)
