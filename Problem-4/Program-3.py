def count_multiples_functional(nums):
    return {i: sum(map(lambda x: x % i == 0, nums)) for i in range(1, 10)}

input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples_functional(input_list))

