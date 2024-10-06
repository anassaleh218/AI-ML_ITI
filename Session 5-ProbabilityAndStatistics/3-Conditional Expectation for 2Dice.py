def ConditionExpectation():
    outcomes = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    even_first_die_outcomes = [(i, j) for i, j in outcomes if i % 2 == 0]
    conditional_expectation = sum([(i + j) * (1 / 36) for i, j in even_first_die_outcomes])
    print("Conditional Expectation:", conditional_expectation)
ConditionExpectation()