import time
import tracemalloc
from functools import wraps


def measure_memory_usage(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        snapshot1 = tracemalloc.take_snapshot()
        # Call the original function
        result = func(*args, **kwargs)

        snapshot2 = tracemalloc.take_snapshot()
        stats = snapshot2.compare_to(snapshot1, "filename")

        # Print the top memory-consuming lines
        print(f"Memory usage of {func.__name__}:")
        for stat in stats:
            print(stat)

        # Return the result
        return result

    return wrapper


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        with open('input.txt') as f:
            input_val = f.readline()
        print(f'Function {func.__name__}({input_val.strip()}) took {total_time:.4f} seconds')
        return result

    return timeit_wrapper
