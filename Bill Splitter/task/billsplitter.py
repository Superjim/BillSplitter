import random

num_friends = int(input("Enter the number of friends joining (including you):\n"))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    friends_dict = {}
    print("\nEnter the name of every friend (including you), each on a new line:\n")
    for friend in range(num_friends):
        name = input()
        friends_dict[name] = 0

if num_friends > 0:
    print("\n", "Enter the total bill value:")
    bill = int(input())
    split_bill = round((bill / num_friends), 2)
    for friend in friends_dict:
        friends_dict[friend] = split_bill

    print("\n", 'Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input().lower()

    if lucky == "no":
        print("No one is going to be lucky")

    if lucky == "yes":
        lucky_index = random.randint(0, num_friends - 1)
        lucky_friend = list(friends_dict.keys())[lucky_index]
        print(f"\n{lucky_friend} is the lucky one!")

        if num_friends > 1:
            friends_dict[lucky_friend] = 0
            updated_num_friends = num_friends - 1
            updated_split_bill = round((bill / updated_num_friends), 2)

            for friend in friends_dict:
                if friend != lucky_friend:
                    friends_dict[friend] = updated_split_bill

    print(friends_dict)
