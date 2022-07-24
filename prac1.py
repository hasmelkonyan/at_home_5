def bin_search(lst, key):
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def binary_search_help(lst, key, start, end):
    if end >= start:
        mid = (start + end) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            return binary_search_help(lst, key, start, mid - 1)
        else:
            return binary_search_help(lst, key, mid + 1, end)
    else:
        return -1


def binary_search_rec(lst, key):
    return binary_search_help(lst, key, start=0, end=len(lst))


def div_by_index(lst):
    quan = 0
    for i in range(1, len(lst)):
        if lst[i] % i == 0:
            quan += 1
    return quan


print(div_by_index([1, 2, 3, 4, 5, 6, 7, 14, 8]))


def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


print(sum_digits(123456))


def dif_mul_and_sum(num):
    mul, sum = 1, 0
    while num > 0:
        mul *= num % 10
        sum += num % 10
        num //= 10
    return mul - sum


print(dif_mul_and_sum(1234))


def fib_rec(n):
    if n in (1, 2):
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


print(fib_rec(5))
