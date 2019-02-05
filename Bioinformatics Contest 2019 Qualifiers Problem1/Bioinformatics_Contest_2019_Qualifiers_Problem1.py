#Bryan Fisk
#2/2/2019
#find the limit of a recursive function given in the problem description

import sys
sys.setrecursionlimit(3000)

#file input from Bioinformatics Contest 2019 (https://bioinf.me/en/contest)
with open('tests.txt', 'r') as file:
    input = list(file.read().split('\n'))
    file.close()

num_samples = int(input.pop(0))
samples = []

for i in range(num_samples):
    temp = list(map(float, input.pop(0).split()))
    samples.append(temp)

#recursive function that recurses iter_n number of times
#mostly to get around stack overflow caused by iterate() recursing too deep
def new_n(n, a, b, iter_n):
    new_iter_n = iter_n - 1
    if iter_n == 0:
        return n
    elif n < 0 or n > sys.float_info.max/1e158:
        return n
    else:
        return new_n(a * n - b * n**2, a, b, new_iter_n)

#recursive function
def iterate(nab):
    percentage_cutoff = 0.0005
    n = nab[0]
    a = nab[1]
    b = nab[2]
    nn = new_n(n, a, b, 2000)

    if nn <= 0.00001:
        return 0
    elif n > 1e50:
        return -1
    elif abs(nn - n) / n < percentage_cutoff:
        return n
    else:
        return iterate([nn, a, b])

[print(iterate(k)) for k in samples]