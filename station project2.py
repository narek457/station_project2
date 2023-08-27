import random

die1 = [1, 2, 3, 4, 5, 6]
die2 = [1, 2, 3, 4, 5, 6]

value_of_throw1 = random.choice(die1)
value_of_throw2 = random.choice(die2)
overall_value = value_of_throw1 + value_of_throw2

print("The total value of the two dice is {} + {} = {}".format(value_of_throw1, value_of_throw2, overall_value))

if overall_value in [7, 11]:
    print("You won ❇")
elif overall_value in [2, 3, 12]:
    print("You lost ˙◠ ˙")
elif overall_value in [4, 5, 6, 8, 9, 10]:
    new_goal = overall_value
    print("Now Your goal number ⌖ is", new_goal)
    overall_value = None
    while overall_value != new_goal and overall_value != 7:
        value_of_throw1 = random.choice(die1)
        value_of_throw2 = random.choice(die2)
        overall_value = value_of_throw1 + value_of_throw2
        print("The total value of the two dice is {} + {} = {}".format(value_of_throw1, value_of_throw2, overall_value))
    if overall_value == new_goal:
        print("You won ❇")
    elif overall_value == 7:
        print("You lost ˙◠ ˙")
        