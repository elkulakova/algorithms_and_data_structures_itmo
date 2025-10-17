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
        #with open('input.txt') as f:
            #input_val = f.readline()
        print(f'Function {func.__name__} took {total_time:.4f} seconds')
        return result

    return timeit_wrapper

import time
import tracemalloc
from functools import wraps

# глобальные переменные, чтобы понимать, что мы входим/выходим из рекурсии
_in_recursion = False
_start_time = None


def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global _in_recursion, _start_time

        is_outer_call = not _in_recursion
        if is_outer_call:
            # запускаем мониторинг только при первом входе в рекурсию
            _in_recursion = True
            _start_time = time.perf_counter()
            tracemalloc.start()

        # выполняем рекурсивную функцию
        result = func(*args, **kwargs)

        if is_outer_call:
            # замеряем время и память только при выходе из внешнего уровня
            end_time = time.perf_counter()
            total_time = end_time - _start_time

            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            with open('input.txt') as f:
                data = f.readlines()

            lngth = int(data[0])
            print(f"Function {func.__name__}({lngth}) took {total_time:.4f} seconds")
            print(f"Peak memory usage: {peak / 1024:.2f} KB")
            print("-" * 50)

            # сбрасываем флаг
            _in_recursion = False

        return result

    return wrapper

import os
import psutil
import time
import threading
from functools import wraps


def measure_base_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global _in_recursion
        is_outer_call = not _in_recursion
        if is_outer_call:
            _in_recursion = True

            process = psutil.Process(os.getpid())
            peak = [process.memory_info().rss]
            running = [True]

            # фоновый поток, который замеряет пик каждые 10 мс
            def monitor():
                while running[0]:
                    mem = process.memory_info().rss
                    if mem > peak[0]:
                        peak[0] = mem
                    time.sleep(0.01)

            t = threading.Thread(target=monitor)
            t.start()

            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()

            running[0] = False
            t.join()

            mem_after = process.memory_info().rss
            peak_usage = peak[0] / 1024#max(0, peak[0] - mem_after) / 1024

            print(f"Function {func.__name__}\nTime taken: {end_time - start_time:.4f} s\n"
                  f"Peak memory: {peak_usage:.2f} KB")

            _in_recursion = False
            return result

        else:
            return func(*args, **kwargs)

    return wrapper
