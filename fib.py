"""
Fibonacci fun.

See "Classic Computer Science Problems in Python" Ch. 1, by David Kopec
"""
import time
from functools import lru_cache

def naive(n):
    """
    Naive recursive implementation of Fibonacci sequence.
    """
    if n < 2:
        return n
    return naive(n - 2) + naive(n - 1)

# Library of previously-computed Fibonacci values, initialized with base
# cases
fib_lib = {0 : 0, 1 : 1}

def explicit_memoization(n):
    """
    Recursive implementation of Fibonacci sequence using memoization.

    Memoization is implemented explicitly with a dict.
    """
    if n not in fib_lib:
        fib_lib[n] = explicit_memoization(n - 2) + explicit_memoization(n - 1)
    return fib_lib[n]
    
@lru_cache(maxsize=None)
def implicit_memoization(n):
    """
    Recursive implementation with implicit memoization using 
    functools.lru_cache.
    """
    if n < 2:
        return n
    return implicit_memoization(n - 2) + implicit_memoization(n - 1)

def iterative(n):
    """
    Iterative implementation of computing fib(n)
    """
    if n < 2:
        return n
    n2, n1 = 0, 1
    for i in range(1, n):
        n2, n1 = n1, n2 + n1
    return n1

def generator(n):
    """
    Generator for producing the entire Fibonacci sequence up to n when iterated
    over.
    """
    # Special cases
    yield 0
    if n > 0: yield 1
    # Initial conditions
    n2 = 0      # fib(0)
    n1 = 1      # fib(1)
    for _ in range(1, n):
        n2, n1 = n1, n2 + n1
        yield n1


def profile(function_to_profile, fib_seq_num=30):
    """
    Dumb Fibonacci function profiling.
    """
    test_range = range(fib_seq_num)
    compute_times = []
    for i in test_range:
        tic = time.time()
        function_to_profile(i)
        toc = time.time()
        compute_times.append(toc - tic)
    return test_range, compute_times

if __name__ == "__main__":
    """
    Profile all implemented fib functions.
    """
    # For displaying profling results
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.set_title("Comparison of Fibonacci Implementations")

    # Profile all implementations of Fibonacci in this file
    import fib
    for item in dir(fib):
        f = getattr(fib, item)
        if callable(f) and item not in ["profile", "lru_cache"]:
            ax.plot(*profile(f), label=f.__name__)

    # Pretty-up plot
    ax.legend()
    ax.set_yscale('log')
    ax.set_ylabel("log(runtime) for fib(n)")
    ax.set_xlabel("n")
    plt.show()
