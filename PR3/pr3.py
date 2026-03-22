import time

def func_memo(max_cache=2, policy='LRU'):

    def func_decorator(func):
        cache = {}

        def lru_eject(cache, *args):
                first_key = next(iter(cache))
                print(f"Cache is full, removing oldest entry with this key: {first_key}")
                del cache[first_key]

        """ def lfu_eject(): """
            
        policies = {
            'LRU': lru_eject
        }

        def func_wrapper(*args):
            print(f"Current cache entries: {cache}")

            if args in cache:
                print("Returning from cache:",{cache[args]})

                result = cache.pop(args)
                cache[args] = result

                return cache[args]
            

            else:
                print("Processing...")
                result = func(*args)

                if len(cache) >= max_cache and max_cache != None:
                    eject_func = policies.get(policy, policy)
                    if callable(eject_func):
                         eject_func(cache, *args)
                         

                cache[args] = result

            return result
        
        return func_wrapper
    
    return func_decorator


@func_memo()
def task(n):
    time.sleep(1)
    return n*10

print(f"First test: {task(5)}")
print(f"Second test: {task(10)}")
print(f"Third test: {task(11)}")
print(f"Fourth test: {task(5)}")
print(f"Fifth test: {task(5)}")
