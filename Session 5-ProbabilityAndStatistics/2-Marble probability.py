# Task 2
def ConditionExpectation():

    total_red = 5
    total_green = 3

    total_marbles = total_red + total_green

    # 1.
    prob_red_first = total_red / total_marbles
    prob_red_second_given_red_first = (total_red - 1) / (total_marbles - 1)
    prob_red_first_and_red_second = prob_red_first * prob_red_second_given_red_first

    # 2.
    prob_green_first = total_green / total_marbles
    prob_red_second_given_green_first = total_red / (total_marbles - 1)

    # 3.
    prob_red_first = total_red / total_marbles
    prob_green_second_given_red_first = total_green / (total_marbles - 1)

    print(f"1. : {prob_red_first_and_red_second:.4f}")
    print(f"2. : {prob_red_second_given_green_first:.4f}")
    print(f"3. : {prob_green_second_given_red_first:.4f}")

ConditionExpectation()