from collections import defaultdict

def count_multiples_hashmap(nums):
    freq = defaultdict(int)
    for i in range(1, 10):
        freq[i] = sum(1 for num in nums if num % i == 0)
    return dict(freq)

input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples_hashmap(input_list))

