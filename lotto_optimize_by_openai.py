import pandas as pd

num_3 = input("Enter 3 digit : ")
num_2 = input("Enter 2 digit : ")

first_num = [int(x) for x in str(num_3)]
sum_first = sum(first_num)
sum_second = sum_first + 5

four_digit = [sum_first % 10, (sum_first + 1) % 10, sum_second % 10, (sum_second + 1) % 10]

tree_num = str(num_3)
tree_num_ = [int(x) for x in tree_num]
tree_num_add = [(x + 1) % 10 for x in tree_num_]
tree_num_min = [(x - 1) % 10 for x in tree_num_]

two_num = str(num_2)
two_num_ = [int(x) for x in two_num]
two_num_add = [(x + 1) % 10 for x in two_num_]
two_num_min = [(x - 1) % 10 for x in two_num_]

two_num_.append(two_num_min[0])
two_num_add.insert(0, two_num_min[1])

s_tree = pd.Series(tree_num_)
s_tree_min = pd.Series(tree_num_min)
s_tree_add = pd.Series(tree_num_add)
s_all = zip(s_tree, s_tree_min, s_tree_add)
s_all_ = pd.Series(s_all)

print('='*23)
print(f"{sum_first} + 5 = {sum_second}")
print('='*23)
print("Lotto Cal...")
print("-"*23)
print(num_3, num_2)

df = pd.DataFrame({
    '3 Digit': s_all_,
    '2 Digit': [two_num_, two_num_min, two_num_add]
})

print(df)
print("-"*23)
print("4 Digit : ", four_digit)
print("="*23)

