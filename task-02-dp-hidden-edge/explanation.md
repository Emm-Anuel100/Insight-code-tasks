# Why LLMs Fail: The Volatile Vault

## The Trap
Standard knapsack problems follow the "Optimal Substructure" property where `dp[w]` only cares about the maximum value for weight `w`. 

However, in this problem, the final value depends on the **number of items used**, but only **conditionally** (if weight > threshold).

## Common LLM Failures
1. **Simple DP:** Most LLMs will try a standard `dp[weight]` array. They will realize they need the penalty, but they won't know how many items were used to reach that `dp[weight]`.
2. **Greedy Attempt:** Some might try to subtract the penalty from each item's value beforehand. This fails because the penalty *only* applies if the *total* weight is over the threshold. An item might be "worth it" in one combination but "not worth it" in another.
3. **State Collapse:** If they do add a second dimension for item count, they often mess up the loops or the base cases, failing to handle the "exactly count items" logic correctly.

## Human-like Explanation
I designed this to break the assumption that "value is additive." Here, value is a function of the entire set's weight property. It forces the developer (or AI) to expand the state space of the DP table, which is a classic test of algorithmic depth.
