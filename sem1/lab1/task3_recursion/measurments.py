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

            print(f"Function {func.__name__} took {total_time:.4f} seconds")
            print(f"Peak memory usage: {peak / 1024:.2f} KB")
            print("-" * 50)

            # сбрасываем флаг
            _in_recursion = False

        return result

    return wrapper
