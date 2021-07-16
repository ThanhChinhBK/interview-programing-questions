def trip_planing(self, days):
    days = set(days)
    costs = [700, 1400, 1900, 2300]
    durations = [1, 7, 14, 30]
    dp = [0 for i in range(max(days) + 1)]
    for i in range(max(days) + 1):
        if i not in days:
            dp[i] = dp[i-1]
        else:
            dp[i] = min(
                [dp[max(0, i - duration)] + cost
                 for duration, cost in zip(durations, costs)]
            )
    return dp[-1]
