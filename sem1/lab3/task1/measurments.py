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

def measure_base_performance(func):
    from functools import wraps
    import time, psutil, os, threading
    _flag = {'in_rec': False}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if _flag['in_rec']:
            return func(*args, **kwargs)

        _flag['in_rec'] = True
        proc = psutil.Process(os.getpid())
        peak = [proc.memory_info().rss]
        running = [True]

        def monitor():
            while running[0]:
                m = proc.memory_info().rss
                if m > peak[0]:
                    peak[0] = m
                time.perf_counter(); time.sleep(0.01)

        t = threading.Thread(target=monitor, daemon=True)
        t.start()
        t0 = time.perf_counter()
        try:
            res = func(*args, **kwargs)
        finally:
            running[0] = False
            t.join()
        dt = time.perf_counter() - t0
        kb = peak[0] / 1024
        print(f"Function {func.__name__}\nTime taken: {dt:.4f} s\nPeak memory: {kb/1024:.2f} MB ({kb:.2f} KB)")
        _flag['in_rec'] = False
        return res
    return wrapper
