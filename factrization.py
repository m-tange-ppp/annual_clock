import math
from collections import defaultdict

def prime_factorization(n):
    primes = defaultdict(int)
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            primes[i] += 1
            n //= i
    if n > 1:
        primes[n] += 1
    return primes

if __name__ == "__main__":
    N = 120
    result = prime_factorization(N)
    for p, num in result.items():
        print(f"{p}^{num}", end = " ")