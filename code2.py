def two_positive(a, b, c):
    count_positives = sum(x > 0 for x in [a, b, c])
    return count_positives == 2
print(two_positive(2, 4, -3))  
print(two_positive(-4, 6, 8))  