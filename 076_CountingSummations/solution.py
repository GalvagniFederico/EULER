def partition_count(n):
    # Create a table to store results of subproblems
    ways = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case
    for i in range(n + 1):
        ways[0][i] = 1  # There's 1 way to partition 0
    
    # Fill the table using the recurrence
    for i in range(1, n + 1):  # Target sum
        for j in range(1, n + 1):  # Max number in partition
            if j > i:
                ways[i][j] = ways[i][j-1]
            else:
                ways[i][j] = ways[i-j][j] + ways[i][j-1]
    
    return ways[n][n-1]  # Exclude n itself as a valid single partition

# Solve for 100
print(partition_count(5))
