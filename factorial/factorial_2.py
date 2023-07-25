import threading
import math

def compute_factorial(number):
    """
    Calculate the factorial of a given number using multiple threads.

    Parameters:
        number (int): The number whose factorial needs to be computed.

    Returns:
        int: The factorial of the given number.
    """

    # Define a shared variable to store the result
    result = 1

    # Define a lock to synchronize access to the shared result variable
    lock = threading.Lock()

    # Define a function to calculate the factorial of a given range of numbers
    def calculate_range_factorial(start, end):
        nonlocal result
        for num in range(start, end):
            # Calculate factorial for the current number and update the result
            with lock:
                result *= num

    # Define the number of threads to use
    num_threads = 4

    # Calculate the range of numbers each thread will handle
    chunk_size = math.ceil(number / num_threads)
    ranges = [(i, min(i + chunk_size, number + 1)) for i in range(1, number + 1, chunk_size)]

    # Create and start the threads
    threads = []
    for start, end in ranges:
        thread = threading.Thread(target=calculate_range_factorial, args=(start, end))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return result


number = 1000
result = compute_factorial(number)
print(f"The factorial of {number} is: {result}")
