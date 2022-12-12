n = int(input())
prime = 2
answer = []
while prime ** 2 <= n:
    while n % prime == 0:
        n //= prime
        answer.append(prime)
    prime += 1
if n > 1:
    answer.append(n)
print('\n'.join(map(str, answer)))
