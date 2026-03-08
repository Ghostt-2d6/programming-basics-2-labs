from fib_lib.generator import fibonacci
from fib_lib.iterator import timeout_iterator

#Демонстрація роботи бібліотеки fib_lib
gen = fibonacci()
#Запуск ітератора на 5 секунд
timeout_iterator(5,gen)