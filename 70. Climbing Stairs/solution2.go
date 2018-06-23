func climbStairs(n int) int {
    // The problem is a fibonacci series
    if n == 1 {
        return 1
    } else if n == 2 {
        return 2
    }
    prev1 := 1
    prev2 := 2
    for i := 3; i <= n; i++ {
        tmp := prev1 + prev2
        prev1 = prev2
        prev2 = tmp
    }
    return prev2
}
