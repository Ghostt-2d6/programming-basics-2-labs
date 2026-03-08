from fib_lib.generator import fibonacci
from fib_lib.iterator import timeout_iterator

gen = fibonacci()
timeout_iterator(5,gen)