import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Tiempo de ejecucion de {func.__name__}: {execution_time} segundos')
        return result
    return wrapper