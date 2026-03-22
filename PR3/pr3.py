import time

def func_memo(max_cache, policy, ttl):

    def func_decorator(func):
        cache = {}
        usage_count = {}
        creation_time = {}

        def print_current_data():
            #uncomment code below if you need to see internal data in tests
            """ print(f"Current cache entries: {cache}")
            print(f"Current usage count of each entry: {usage_count}")
            print(f"Creation time of each entry: {creation_time}") """

        def lru_eject(cache, *args):
                first_key = next(iter(cache))
                print(f"Cache is full, removing oldest with this key (LRU policy): {first_key}")
                del cache[first_key]
                del usage_count[first_key]
                del creation_time[first_key]

        def lfu_eject(cache, *args):
            lfu = min(usage_count, key=usage_count.get)
            print(f"Cache is full, removing entry with this key (LFU policy): {lfu}")
            del cache[lfu]
            del usage_count[lfu]
            del creation_time[lfu]

        def tbe_eject(cache, *args):
            oldest_entry = min(creation_time, key=creation_time.get)
            print(f"Cache is full, removing entry with this key (TBE policy): {oldest_entry}")
            del cache[oldest_entry]
            del usage_count[oldest_entry]
            del creation_time[oldest_entry]            
        
        policies = {
            'LRU': lru_eject,
            'LFU': lfu_eject,
            'TBE': tbe_eject,
        }
        eject_func = policies.get(policy, policy)

        def func_wrapper(*args):
            if args in cache:
                #always active TBE policy
                current_time = time.time()
                if current_time - creation_time[args] > ttl:
                    print(f"Entry with the key {args} is expired and will be removed")
                    del cache[args]
                    del usage_count[args]
                    del creation_time[args]  
                else:
                    print("Returning from cache:",{cache[args]})

                    result = cache.pop(args)
                    cache[args] = result
                    usage_count[args] += 1

                    print_current_data()

                    return result

            result = func(*args)

            if len(cache) >= max_cache and max_cache != None:
                if callable(eject_func):
                        eject_func(cache, *args)

            cache[args] = result
            usage_count[args] = 1
            creation_time[args] = time.time()

            print_current_data()
            return result
        
        return func_wrapper
    
    return func_decorator


@func_memo(max_cache=2,policy='TBE', ttl=1)
def task(n):
    return n*10

#un-comment code block below if you need to test LRU policy 
#recommended arguments for @func_memo: max_cache=2, policy='LRU' (mandatory), ttl=10 
""" print("---Test for LRU---")
print(f"test 1: {task(1)}")
print(f"test 2: {task(2)}")
print(f"test 3: {task(3)}")
print(f"test 4: {task(4)}") """

#un-comment code block below if you need to test LFU policy 
#recommended arguments for @func_memo: max_cache=2, policy='LFU' (mandatory), ttl=10 
""" print(f"test 1: {task(1)}")
print(f"test 2: {task(1)}")
print(f"test 3: {task(2)}")
print(f"test 4: {task(3)}") """

#un-comment code block below if you need to test Time Based Expiry policy 
#recommended arguments for @func_memo: max_cache=2, policy='TBE' (not mandatory), ttl=1 (less than 2)
#TBE policy is always active but if you want to test it exclusively with different max_cache/ttl args set policy='TBE'
""" print(f"test 1: {task(1)}")
time.sleep(2)
print(f"test 2: {task(1)}")
time.sleep(2)
print(f"test 3: {task(2)}")
print(f"test 4: {task(1)}")
time.sleep(2)
print(f"test 5: {task(2)}")
print(f"test 6: {task(1)}") """
