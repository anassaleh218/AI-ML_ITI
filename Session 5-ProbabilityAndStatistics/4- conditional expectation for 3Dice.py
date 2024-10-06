# Task 3
def conditional_probability_simple():
    # Generate outcomes for the sum and product of three dice
    dice_outcomes = {(i, j, k) for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)}

    event_A = [(i, j, k) for i, j, k in dice_outcomes if i + j > 8]
    event_B = [(i, j, k) for i, j, k in dice_outcomes if k % 2 != 2]
    event_A_and_B = [(i, j, k) for i, j, k in event_A if k % 2 != 0]

    # Count outcomes where half the product exceeds the sum
    point1_prob = sum(i + j + k for i, j, k in event_A) / len(event_A)
    point2_prob = sum(i + j + k for i, j, k in event_A_and_B) / len(event_A_and_B)

    print(f"A: {point1_prob:.4f}")
    print(f"B: {point2_prob:.4f}")


conditional_probability_simple()
