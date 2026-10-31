# генератор бесконечной последовательности

# №1
"""
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"You lose: {end_time - start_time} seconds")
        return result
    return wrapper

@time_decorator
def function():
    for i in range(0,100):
        print(i)

print(function())
"""
# №2

def fib():
    q, w = 0, 1
    while 1 > 0:
        q, w = w, q + w
        yield q

for i in fib():
    print(i)
