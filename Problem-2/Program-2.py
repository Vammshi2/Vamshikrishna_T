def generate_odd_recursive(n, i=0, result=None):
    if result is None:
        result = []
    if i == n:
        return result
    result.append(2 * i + 1)
    return generate_odd_recursive(n, i + 1, result)

a = int(input("Enter a number: "))
print(", ".join(map(str, generate_odd_recursive(a))))

