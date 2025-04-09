#prime fact method for sq root

def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def sqrt_prime_factorization(n):
    if n < 0:
        return "Square root of negative numbers is not defined in real numbers."
    
    factors = prime_factorization(n)
    factor_count = {}
    
    for f in factors:
        factor_count[f] = factor_count.get(f, 0) + 1
    
    sqrt_value = 1
    for factor, count in factor_count.items():
        if count % 2 != 0:
            return "Square root is not a perfect square."
        sqrt_value *= factor ** (count // 2)

    return sqrt_value

num = int(input("Enter a number: "))
print("Square root using prime factorization method:", sqrt_prime_factorization(num))
