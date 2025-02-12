# %%
def bigo_n(n):
    for i in range(0, n):
        print(i)


bigo_n(5)


# %%
def bigo_nsquare(n):
    for i in range(0, n):
        for j in range(0, n):
            print(i, j)


bigo_nsquare(5)


# %%
def bigo_ncube(n):
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                print(i, j, k)


bigo_ncube(5)

# %%
import math


def log_n(n):
    while n > 1:
        n = math.floor(n / 2)
        print(n)


log_n(8)


# %%
def nlog_n(n):
    lim = n
    while n > 1:
        n = math.floor(n / 2)
        for i in range(1, lim):
            print(i)


nlog_n(8)


# %%
def n_factorial(n):
    if n == 0:
        print("1")
        return
    else:
        for i in range(0, n):
            print(i)
            n_factorial(n - 1)  # recursive


n_factorial(3)