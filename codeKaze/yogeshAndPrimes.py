
def sieve(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
 
primes = list(sieve(1000100))
primeIndexes = dict()

for idx, number in enumerate(primes):
    primeIndexes[number] = idx

# print(len(primes))

q = int(input())
ans = []

for i in range(q):

    a, b, k = list(map(int, input().split(' ')))
    startPrime = a
    while startPrime not in primeIndexes and startPrime <= b:
        startPrime += 1
    if startPrime > b:
        ans.append("-1")
    else:
        startIdx = primeIndexes[startPrime]
        if startIdx+k-1 >= len(primes):
            ans.append("-1")
        else:
            lastPrime = primes[startIdx + k - 1]
            if lastPrime <= b:
                ans.append(lastPrime)
            else:
                ans.append("-1")         

for x in ans:
    print(x)