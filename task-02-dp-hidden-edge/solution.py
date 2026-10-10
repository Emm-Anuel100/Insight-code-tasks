from typing import List, Tuple

def solve_vault(items: List[Tuple[int, int]], max_weight: int, threshold: int, penalty: int) -> int:
    """
    Solve the Vault problem using Dynamic Programming.
    State: dp[w][count] = max value for weight w using exactly 'count' items.
    
    This is necessary because the penalty depends on both the total weight 
    AND the number of items.
    """
    n = len(items)
    # dp[weight][item_count]
    dp = [[-float('inf')] * (n + 1) for _ in range(max_weight + 1)]
    dp[0][0] = 0

    for val, weight in items:
        # Iterate backwards to avoid using the same item twice (0/1 Knapsack)
        for w in range(max_weight, weight - 1, -1):
            for count in range(n, 0, -1):
                if dp[w - weight][count - 1] != -float('inf'):
                    dp[w][count] = max(dp[w][count], dp[w - weight][count - 1] + val)

    max_val = 0
    for w in range(max_weight + 1):
        for count in range(n + 1):
            if dp[w][count] == -float('inf'):
                continue
            
            current_val = dp[w][count]
            # Apply penalty if weight is over threshold
            if w > threshold:
                current_val -= (count * penalty)
            
            max_val = max(max_val, current_val)

    return max(0, max_val)
