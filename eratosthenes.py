# 에라토스테네스의 체 - n 이하 소수 구하기
import math

n = int(input())
is_prime = [False, False] + [True] * (n - 1)
for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

primes = [i for i in range(2, n + 1) if is_prime[i]]
print(primes)

# O(log(logn))
