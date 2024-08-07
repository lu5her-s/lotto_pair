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
    # for i in three_digit_list:
    #     three_digit_sum += int(i)
    all_list = three_digit_list + two_digit_list
    for i in all_list:
        three_digit_sum += int(i)
    # print sum of 3 digit
    # print("Sum of 3 digit:", three_digit_sum)

    # sum of 3 digit + 5
    three_digit_sum_plus_five = three_digit_sum + 5
    # print sum of 3 digit + 5
    # print("Sum of 3 digit + 5:", three_digit_sum_plus_five)

    # four_digit = [three_digit_sum[-1]%10, three_digit_sum[-1]+1 % 10,
    # three_digit_sum_plus_five[-1]%10, three_digit_sum_plus_five[-1]+1 % 10]
    four_digit = [
        three_digit_sum % 10,
        (three_digit_sum + 1) % 10,
        three_digit_sum_plus_five % 10,
        (three_digit_sum_plus_five + 1) % 10,
    ]
    # print four digit
    # print("4 digit:", four_digit)

    # make banner Lotto Calculator by 0x4c
    print("=" * 23)
    print("Lotto Calculator by 0x4c")
    print("=" * 23)
    print("Sum : ", three_digit_sum)
    print("-" * 23)
    print(three_digit, two_digit, "==", four_digit)
    print("=" * 23)

    user_input = input("\nDo you want to exit? (y/n) : ")
    if user_input == "y":
        break
