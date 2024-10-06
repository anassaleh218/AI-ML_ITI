# import numpy as np
# import pandas as pd
#
# # Generate all possible outcomes for three dice
# dice_values = np.arange(1, 7)
#
# # Initialize lists to store results
# products = []
# sums = []
#
# # Iterate through all possible combinations of three dice
# for d1 in dice_values:
#     for d2 in dice_values:
#         for d3 in dice_values:
#             products.append(d1 * d2 * d3)
#             sums.append(d1 + d2 + d3)
#
# # Create a DataFrame with the outcomes
# df = pd.DataFrame({
#     'product': products,
#     'sum': sums
# })
#
# # Create a new column for the condition (half product > sum)
# df['half_product_exceeds_sum'] = (df['product'] / 2) > df['sum']
#
# # Use crosstab to count the occurrences of True and False
# crosstab = pd.crosstab(df['half_product_exceeds_sum'], columns='count')
#
# # Calculate the probability
# probability = crosstab.loc[True, 'count'] / crosstab['count'].sum()
#
# print(probability)

# Task 1
def conditional_probability_simple():
    # Generate outcomes for the sum and product of three dice
    dice_outcomes_sum = {(i, j, k): i + j + k for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)}
    dice_outcomes_product = {(i, j, k): i * j * k for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)}

    # Count outcomes where half the product exceeds the sum
    count_exceeding_sum = sum(1 for outcome in dice_outcomes_sum
                              if 0.5 * dice_outcomes_product[outcome] > dice_outcomes_sum[outcome])


    conditional_probability = count_exceeding_sum / 216

    print(f"Probability that half the product of three dice exceeds their sum: {conditional_probability:.4f}")

conditional_probability_simple()
