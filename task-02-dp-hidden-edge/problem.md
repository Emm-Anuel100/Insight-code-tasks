# Problem: The Volatile Vault (DP Twist)

## The Story
You are a thief trying to steal items from a high-tech vault. Each item has a `value` and a `weight`. However, this vault has "Stability Traps." 

If your total weight exceeds a certain threshold, the vault becomes unstable, and some items **lose** value instead of gaining it.

## Task
Given:
- `items`: A list of tuples `(value, weight)`.
- `max_weight`: Your maximum carrying capacity.
- `instability_threshold`: A weight limit.
- `penalty`: A fixed value subtracted from your total for **every** item carried if your total weight is > `instability_threshold`.

Find the maximum total value you can carry without exceeding `max_weight`.

## Constraints
- `n_items` up to 100.
- `max_weight` up to 1000.
- Values and weights can be positive integers.
- Penalty is a positive integer.

## Example
Items: `[(10, 5), (15, 10), (20, 15)]`
Max Weight: 30
Instability Threshold: 20
Penalty: 5

If you take all items: 
- Total Weight = 5 + 10 + 15 = 30 (<= Max Weight)
- Total Weight (30) > Instability (20), so Penalty applies.
- Total Value = (10 + 15 + 20) - (3 items * 5 penalty) = 45 - 15 = 30.

If you take just (10, 5) and (15, 10):
- Total Weight = 15 (<= Instability)
- Total Value = 25 (No penalty).

The best choice here depends on the penalty!
