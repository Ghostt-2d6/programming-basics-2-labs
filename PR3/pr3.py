import time

def fibonacci_memo(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
           print("Returning from cache:",{cache[args]})
           return cache[args]
        else:
            print("Processing...")
            result = func(*args)
        
        cache[args] = result

        print(f"Current cache entries: {cache}")

        return result
    
    return wrapper


@fibonacci_memo
def task(n):
    time.sleep(1)
    return n*10

print(f"First test: {task(5)}")
print(f"Cache test: {task(5)}")
print(f"Second test: {task(10)}")
print(f"Cache test: {task(10)}")
