from functools import wraps
from time import perf_counter
import sys

def memorize(func):
	cache = {}

	@wraps(func)
	def wrapper(*args, **kwargs):
		key = str(args) + str(kwargs)

		if key not in cache:
			cache[key] = func(*args, **kwargs)

		return cache[key]

	return wrapper


@memorize
def fibonacci(n):
	if n < 2:
		return n

	return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
	start = perf_counter()
	f = fibonacci(1)
	end = perf_counter()

	print(f)
	print(f'time: {end - start} seconds')