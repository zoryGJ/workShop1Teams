import random
from Exercise10 import timer

@timer
def sort_numbers(numbers):
    sorted_numbers = sorted(numbers)
    print('Lista ordenana:', sorted_numbers)

numbers = [random.randint(1, 100) for _ in range(10)]
sort_numbers(numbers)