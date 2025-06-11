def sum_values(*nums):
    total = sum(nums)
    print("Sum =", total)

user_input = input("Enter numbers separated by spaces: ")

num_list = list(map(int, user_input.split()))

sum_values(*num_list)
