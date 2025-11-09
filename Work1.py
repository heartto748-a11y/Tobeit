def sum(numbers):
    total = 0
    for n in numbers:
        if n % 2 == 0:
            total += n
    return total
print(sum([1, 2, 3, 4, 5, 6]))
print(sum([7, 9, 11]))
print(sum([10, -2, 8]))