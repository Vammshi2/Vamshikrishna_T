def generate_odd_recursive(a, current=1, result=None):
    if result is None:
        result = []
    limit = a if a % 2 == 1 else a - 1
    if current > limit:
        return result
    result.append(current)
    return generate_odd_recursive(a, current + 2, result)

a = int(input("Enter a number: "))
print(", ".join(map(str, generate_odd_recursive(a))))
