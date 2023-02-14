import pandas as pd

num_3 = input("Enter 3 digit : ")
num_2 = input("Enter 2 digit : ")

first_num = [int(x) for x in str(num_3[0])]

sum_first = sum(first_num)
s_ = str(sum_first)
sum_second = sum_first + 5
s__ = str(sum_second)
# print(s_, '+ 5 =', s__)
# four_digit = [int(s_[1]), int(s_[1])+1, int(s__[1]), int(s__[1])+1]
four_digit = []
if sum_first < 10:
    four_digit = [int(s_[0]), int(s_[0])+1, int(s__[0]), int(s__[0])+1]
else:
    four_digit = [int(s_[1]), int(s_[1])+1, int(s__[1]), int(s__[1])+1]
tree_num = str(num_3)
tree_num_ = [int(x) for x in tree_num]
tree_num_add = [int(x)+1 for x in tree_num_]
# tree_num_add
# tree_num_min = [abs(int(x)-1) for x in tree_num_]
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
two_num_add = [int(x)+1 for x in two_num_]
two_num_min = [abs(int(x)-1) for x in two_num_]
# for x in two_num_:
    # a = x
    # if a < 10:
        # two_num_min.append(a)
    # else:
        # a_s = str(a)
        # two_num_min.append(int(a_s[1]))
# print(two_num_,  two_num_min, two_num_add)
two_num_.append(two_num_min[0])
two_num_add.insert(0, two_num_min[1])

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
    'tree_num': tree_num_,
    'min': tree_num_min,
    'add': tree_num_add,
    'two_1': two_num_,
    'two_2': two_num_add,
}
# cols = ['pre', '-', '+' , '2', '2']
df = pd.DataFrame(datas)

min_first = [abs(int(x) - 5) for x in tree_num_]

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

add_two = []
for x, y in zip(min_first, add_first):
    a = int(x) + int(y)
    if a < 10:
        add_two.append(a)
    else:
        a_s = str(a)
        add_two.append(int(a_s[1]))

sum_min = sum(min_first)
if sum_min < 10:
    min_first.append(sum_min)
else:
    sum_min_s = str(sum_min)
    min_first.append(int(sum_min_s[1]))

sum_add1 = sum(add_first)
if sum_add1 < 10:
    add_first.append(sum_add1)
else:
    sum_add1_s = str(sum_add1)
    add_first.append(int(sum_add1_s[1]))

sum_add2 = sum(add_two)
if sum_add2 < 10:
    add_two.append(sum_add2)
else:
    sum_add2_s = str(sum_add2)
    add_two.append(int(sum_add2_s[1]))

data2 = {
    '-': min_first,
    '+': add_first,
    'sum': add_two,
}

df2 = pd.DataFrame(data2)

print('='*23)
print('4 digit =', four_digit)
print('='*23)
print(df.to_string(index=False))
print('='*23)
print(df2.to_string(index=False))
