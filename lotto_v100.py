import pandas as pd

# get input 3 digit and 2 digit
num_3 = input("Enter 3 digit : ")
num_2 = input("Enter 2 digit : ")

# convert 3 digit to list
first_num = [int(x) for x in str(num_3)]

# first_num

sum_first = sum(first_num)
s_ = str(sum_first)
# s_
sum_second = sum_first + 5
s__ = str(sum_second)
# print('='*23)
# print(s_, '+ 5 =', s__)
print('='*23)
print("Lotto Calculator")
print("\tby Danail")
# print("-"*23)
# print(num_3, num_2)

# s_

# if sum_first < 10:
four_digit = [int(s_[-1]) % 10, (int(s_[-1])+1) %
              10, int(s__[-1]) % 10, (int(s__[-1])+1) % 10]
# else:
# four_digit = [int(s_[1]), int(s_[1])+1, int(s__[1]), int(s__[-1])+1]
# four_digit

tree_num = str(num_3)
tree_num_ = [int(x) for x in tree_num]
# tree_num_add = [int(x)+1 for x in tree_num_]
tree_num_add = []
for x in tree_num_:
    a = int(x) + 1
    if a < 10:
        # a_s = str(a)
        tree_num_add.append(a)
    else:
        a_s = str(a)
        tree_num_add.append(int(a_s[1]))

# tree_num_add
# tree_num_min = [(int(x)-1) for x in tree_num_]
tree_num_min = []
for x in tree_num_:
    if x == 0:
        x = abs(10 - 1)
        tree_num_min.append(x)
    else:
        x = x - 1
        tree_num_min.append(x)
# print(tree_num_, tree_num_min, tree_num_add)

two_num = str(num_2)
two_num_ = [int(x) for x in two_num]
# two_num_add = [int(x)+1 for x in two_num_]
two_num_add = []
for x in two_num_:
    x_sum = int(x) + 1
    if x_sum < 10:
        two_num_add.append(x_sum)
    else:
        x_s = str(x_sum)
        two_num_add.append(int(x_s[1]))
# two_num_min = [abs(int(x)-1) for x in two_num_]
two_num_min = []
for x in two_num_:
    if x == 0:
        two_num_min.append(int(9))
    else:
        two_num_min.append(int(x)-1)
# print(two_num_,  two_num_min, two_num_add)

# import pandas as pd

two_num_.append(two_num_min[0])
two_num_add.insert(0, two_num_min[1])

# two_num_add

s_tree = pd.Series(tree_num_)
s_tree_min = pd.Series(tree_num_min)
s_tree_add = pd.Series(tree_num_add)
s_all = zip(s_tree, s_tree_min, s_tree_add)
s_all_ = pd.Series(s_all)
# l_all = zip(tree_num_, tree_num_min, tree_num_add, two_num, two_num_min, two_num_add)
# df = pd.DataFrame(s_all_)
# df
# two_num_.append(two_num_min[0])
# two_num_add.insert(0, two_num_min[1])
datas = {
    '--': tree_num_,
    '-': tree_num_min,
    '***': tree_num_add,
    '+': two_num_,
    '++': two_num_add,
}
# cols = ['pre', '-', '+' , '2', '2']
df = pd.DataFrame(datas)
# df

# table 12 field
# min first group
min_first = [abs(int(x) - 5) for x in tree_num_]
# min_first

# add first group
# add_first = [int(x) + 5 for x in tree_num_]
add_first = []
for x in tree_num_:
    if x == 8:
        add_first.append(8)
    elif x == 7:
        add_first.append(5)
    else:
        if int(x) + 5 < 10:
            add_first.append(int(x)+5)
        else:
            s_x = str(int(x)+5)
            add_first.append(int(s_x[1]))

# add_first

# add_two = [int(x) + int(y) for x,y in zip(min_first, add_first)]
# add_two.clear()
add_two = []
for x, y in zip(min_first, add_first):
    a = int(x) + int(y)
    if a < 10:
        add_two.append(a)
    else:
        a_s = str(a)
        add_two.append(int(a_s[1]))

# add_two

sum_min = sum(min_first)
if sum_min < 10:
    min_first.append(sum_min)
else:
    sum_min_s = str(sum_min)
    min_first.append(int(sum_min_s[1]))

# min_first

sum_add1 = sum(add_first)
if sum_add1 < 10:
    add_first.append(sum_add1)
else:
    sum_add1_s = str(sum_add1)
    add_first.append(int(sum_add1_s[1]))

# add_first

sum_add2 = sum(add_two)
if sum_add2 < 10:
    add_two.append(sum_add2)
else:
    sum_add2_s = str(sum_add2)
    add_two.append(int(sum_add2_s[1]))

# add_two

# four_digit

data2 = {
    '-': min_first,
    '+': add_first,
    '=': add_two,
}
df2 = pd.DataFrame(data2)

# df2

print('='*23)
print(num_3, num_2, '=>', four_digit)
print('='*23)
print(df.to_string(index=False))
print('='*23)
print(df2.to_string(index=False))
print('='*23)
