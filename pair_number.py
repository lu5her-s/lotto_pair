from itertools import combinations

# while loop until user exit = y
while True:
    # get input from user and split to list digit
    user_input = input("Enter a list of digits: ")
    # list_input = user_input.split()
    list_input = list(user_input)
    # remove " " from list_input
    list_input = [x for x in list_input if x != " "]
    # check if user input is empty
    if len(list_input) == 0:
        print("Input is empty")
        continue
    # check if user input is not digit
    for i in list_input:
        if not i.isdigit():
            print("Input is not digit")
            continue

    # get all combinations of length 2
    comb_2_digit = combinations(list_input, 2)
    # get all combinations of length 3
    comb_3_digit = combinations(list_input, 3)

    # get length of comb_2_digit
    # length_2 = len(list(comb_2_digit))
    # get length of comb_3_digit
    # length_3 = len(list(comb_3_digit))

    # print length of combinations
    # print('='*23)
    # print("Length of combinations of length 2: ", length_2)
    # print("Length of combinations of length 3: ", length_3)

    # print all combinations of length 2
    print('='*23)
    print("Combinations of length 2: ")
    length_2 = 0
    for i in list(comb_2_digit):
        print(i)
        length_2 += 1
    # print('-'*23)
    # print len of comb_2_digit

    # print all combinations of length 3
    print('='*23)
    print("Combinations of length 3: ")
    length_3 = 0
    for i in list(comb_3_digit):
        print(i)
        length_3 += 1
    print('-'*23)
    # print len of length_2, length_3
    print("Length of combinations of length 2: ", length_2)
    print("Length of combinations of length 3: ", length_3)

    print('='*23)

    # ask user to exit or continue
    exit = input("\nDo you want to exit? (y/n): ")
    if exit == 'y':
        break
