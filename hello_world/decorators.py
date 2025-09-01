import time

# Decorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# Applying decorator
@timing_decorator
def slow_function():
    time.sleep(2)
    return "Done"

@timing_decorator
def fast_function():
    return sum(range(10_000))

# Usage
print(slow_function())
print(fast_function())
