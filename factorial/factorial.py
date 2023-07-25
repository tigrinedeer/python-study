import math
import threading


def compute_factorial(number, num_threads=2):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if number == 0:
        return 1

    if number <= 2:
        return number

    chunk_size = number // num_threads
    remaining_chunk = number % num_threads

    def factorial_partial(start, end, results):
        result = 1
        for i in range(start, end + 1):
            result *= i
        results.append(result)
        return result

    threads = []
    results = []
    for i in range(num_threads):
        start = i * chunk_size + 1
        end = start + chunk_size - 1 if i < num_threads - 1 else start + chunk_size + remaining_chunk - 1
        thread = threading.Thread(target=factorial_partial, args=(start, end, results))
        threads.append(thread)
        thread.start()

    total_result = 1
    for thread in threads:
        thread.join()
    return math.prod(results)


# Example usage:
num = 1000
result = compute_factorial(num, num_threads=4)
print(f"The factorial of {num} is: {result}")
