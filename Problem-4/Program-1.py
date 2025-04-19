def count_multiples_basic(nums):
    result = {}
    for i in range(1, 10):
        count = 0
        for num in nums:
            if num % i == 0:
                count += 1
        result[i] = count
    return result

input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples_basic(input_list))
