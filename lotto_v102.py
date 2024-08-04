import pandas as pd
from tabulate import tabulate

# while for do something and ask for exit
while True:
    # print("Hello")
    # get input 3 digit and 2 digit
    user_input = input("Please enter 3 digit and 2 digit: ")
    # split 3 digit and 2 digit
    three_digit = user_input[:3]
    two_digit = user_input[3:]
    # two_digit remove ' '
    two_digit = two_digit.replace(" ", "")
    # print 3 digit and 2 digit
    # print("3 digit:", three_digit)
    # print("2 digit:", two_digit)

    # convert 3 digit to list
    three_digit_list = list(three_digit)
    # convert 2 digit to list
    two_digit_list = list(two_digit)
    # print 3 digit list and 2 digit list
    # print("3 digit list:", three_digit_list)
    # print("2 digit list:", two_digit_list)

    # sum of 3 digit
    three_digit_sum = 0
    for i in three_digit_list:
        three_digit_sum += int(i)
    # print sum of 3 digit
    # print("Sum of 3 digit:", three_digit_sum)

    # sum of 3 digit + 5
    three_digit_sum_plus_five = three_digit_sum + 5
    # print sum of 3 digit + 5
    # print("Sum of 3 digit + 5:", three_digit_sum_plus_five)

    # four_digit = [three_digit_sum[-1]%10, three_digit_sum[-1]+1 % 10,
    # three_digit_sum_plus_five[-1]%10, three_digit_sum_plus_five[-1]+1 % 10]
    four_digit = [three_digit_sum % 10, (three_digit_sum + 1) % 10,
                  three_digit_sum_plus_five % 10, (three_digit_sum_plus_five + 1) % 10]
    # print four digit
    # print("4 digit:", four_digit)

    # if num in three_digit_list+1 < 10 append to list else %10 before append
    three_digit_list_plus_one = []
    for i in three_digit_list:
        if int(i) + 1 < 10:
            three_digit_list_plus_one.append(int(i) + 1)
        else:
            three_digit_list_plus_one.append((int(i) + 1) % 10)
    # print three_digit_list_plus_one
    # print("3 digit list + 1:", three_digit_list_plus_one)

    # if num in three_digit_list == 0 append 10 - 1 to list else append num - 1
    # to list
    three_digit_list_minus_one = []
    for i in three_digit_list:
        if int(i) == 0:
            three_digit_list_minus_one.append(10 - 1)
        else:
            three_digit_list_minus_one.append(int(i) - 1)
    # print three_digit_list_minus_one
    # print("3 digit list - 1:", three_digit_list_minus_one)

    # if num in two_digit_list+1 < 10 append to list else %10 before append
    two_digit_list_plus_one = []
    for i in two_digit_list:
        if int(i) + 1 < 10:
            two_digit_list_plus_one.append(int(i) + 1)
        else:
            two_digit_list_plus_one.append((int(i) + 1) % 10)
    # print two_digit_list_plus_one
    # print("2 digit list + 1:", two_digit_list_plus_one)
    # if num in two_digit_list == 0 append 10 - 1 to list else append num - 1
    # to list
    two_digit_list_minus_one = []
    for i in two_digit_list:
        if int(i) == 0:
            two_digit_list_minus_one.append(10 - 1)
        else:
            two_digit_list_minus_one.append(int(i) - 1)
    # print two_digit_list_minus_one
    # print("2 digit list - 1:", two_digit_list_minus_one)

    # append two_digit_list_minus_one[0] to two_digit_list and insert
    # two_digit_list_minus_one to two_digit_list_plus_one[0]
    two_digit_list.append(two_digit_list_minus_one[0])
    two_digit_list_plus_one.insert(0, two_digit_list_minus_one[1])
    # print two_digit_list
    # print("2 digit list:", two_digit_list)
    # print two_digit_list_plus_one
    # print("2 digit list + 1:", two_digit_list_plus_one)

    # datas = three_digit_list, three_digit_list_minus_one,
    # three_digit_list_plus_one, two_digit_list, two_digit_list_plus_one colums
    # is -- , - , ** , +, ++ to DataFrame
    data = {
        '<<': three_digit_list,
        '<': three_digit_list_minus_one,
        '**': three_digit_list_plus_one,
        '>': two_digit_list,
        '>>': two_digit_list_plus_one
    }
    df1 = pd.DataFrame(data)
    # print(df1)

    # list abs(num - 5) for num in three_digit_list
    min_list = [abs(int(num) - 5) for num in three_digit_list]
    # append sum in min_list%10 to min_list
    min_list.append(sum(min_list) % 10)
    # print("Minus first list:", min_list)

    # list for num in three_digit_list if num == 8 append 8 elif
    # num == 7 append 5 else append (num+5)%10
    plus_list = [8 if int(num) == 8 else 5 if int(num) == 7 else (
        int(num) + 5) % 10 for num in three_digit_list]
    # append sum in plus_list%10 to plus_list
    plus_list.append(sum(plus_list) % 10)
    # print("Plus first list:", plus_list)

    # sum_list = (min_list[i] + plus_list)%10
    sum_list = [((min_list[i] + plus_list[i]) % 10)
                for i in range(len(min_list))]
    # print("Sum of two lists:", sum_list)

    # datas = min_list, plus_list, sum_list  columns = 1 2 3
    df2 = pd.DataFrame(list(zip(min_list, plus_list, sum_list)),
                       columns=['<<', '**', '>>'])
    # print(df2)

    # make banner Lotto Calculator by 0x4c
    print("="*23)
    print("Lotto Calculator by 0x4c")
    print("="*23)

    print('\n\n', three_digit, two_digit, '==', four_digit)
    print("="*23)

    # print df1 and jusify text center
    # print(df1.to_string(index=False))
    print(tabulate(df1, showindex=False, headers=df1.columns))
    print("="*23)
    # print df2 and jusify text center
    # print(df2.to_string(index=False))
    print(tabulate(df2, showindex=False, headers=df2.columns))
    print("="*23)

    user_input = input("\nDo you want to exit? (y/n) : ")
    if user_input == 'y':
        break
