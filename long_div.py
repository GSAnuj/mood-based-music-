

#using long division method

def sqrt_long_division(n):
    if n < 0:
        return "Square root of negative numbers is not defined in real numbers."
    
    n_str = str(n)
    if '.' in n_str:
        int_part, dec_part = n_str.split('.')
        n_str = int_part + dec_part
        decimal_places = len(dec_part)
    else:
        decimal_places = 0
    
    n = int(n_str)
    pairs = []
    while n > 0:
        pairs.append(n % 100)
        n //= 100
    pairs.reverse()

    root = 0
    remainder = 0
    for pair in pairs:
        remainder = remainder * 100 + pair
        x = 0
        while (20 * root + x) * x <= remainder:
            x += 1
        x -= 1
        root = root * 10 + x
        remainder -= (20 * root + x) * x

    if decimal_places > 0:
        root /= 10 ** (decimal_places // 2)

    return root

num = int(input("Enter a number: "))
print("Square root using long division method:", sqrt_long_division(num))
