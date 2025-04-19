def generate_odd_upto_a(a):
    if a % 2 == 0:
        a -= 1
    result = []
    for i in range(1, a + 1, 2):
        result.append(i)
    return result

a = int(input("Enter a number: "))
print(", ".join(map(str, generate_odd_upto_a(a))))
