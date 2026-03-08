import time

def timeout_iterator(t, fibonacci_generator):
    start_time = time.time()
    total = 0
    for n in fibonacci_generator:
        current_time = time.time()
        elapsed = current_time - start_time
        if elapsed >= t:
            print(total)
            break
        else:
            print(n)
            total += n
            time.sleep(0.5)
            continue