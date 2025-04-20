from functools import wraps
from time import time

print("Day 54 - 100 Days of Code.")
print("Welcome to Function's execution time calculator - Decorator.")


def execution_time_calculator_decorator(function_to_check):
    """
    A decorator function to calculate and print the execution time of a given function.

    Args:
        function_to_check (function): The function whose execution time is to be calculated.

    Returns:
        function: A wrapper function that calculates and prints the execution time.
    """

    @wraps(function_to_check)
    def get_execution_time(*args, **kwargs):
        """
        Wrapper function to calculate and print the execution time of the decorated function.
        """
        start_time = time()
        result = function_to_check(*args, **kwargs)
        end_time = time()
        print("Execution time:", end_time - start_time)
        return result

    return get_execution_time


@execution_time_calculator_decorator
def fast_function():
    """
    A sample function that performs a quick computation by summing numbers from 0 to 99.
    """
    value = sum(range(100))
    print("Final value:", value)


@execution_time_calculator_decorator
def slow_function():
    """
    A sample function that performs a slower computation by incrementing a value 100,000 times.
    """
    value = 0
    for _ in range(10000000):
        value += 1
    print("Final value:", value)


fast_function()
slow_function()
