import matplotlib.pyplot as plt
import timeit

def slow_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return slow_fib(n-1) + slow_fib(n-2)

def fast_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a,b,c=0,1,0
    for i in range(n-1):
        c = a + b
        a = b
        b = c

    return b

timeslow = []
timefast = []
for i in range(30):
    start_time = timeit.default_timer();slow_fib(i);timeslow.append(timeit.default_timer() - start_time)
    start_time = timeit.default_timer();fast_fib(i);timefast.append(timeit.default_timer() - start_time)

plt.plot(range(30),timeslow,'r--')
plt.plot(range(30),timefast,'g--')
plt.show()