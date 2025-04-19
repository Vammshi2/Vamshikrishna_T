def generate_odd_series(n):
    result = []
    for i in range(n):
        result.append(2 * i + 1)
    return result

a = int(input("Enter a number: "))
print(", ".join(map(str, generate_odd_series(a))))
