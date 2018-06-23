func climbStairs(n int) int {
    var sol int
    // The problem can be thought of permutations of a set of steps that consists of 1 and 2 and the total is n
    for i:=n;i>=0;i=i-2 {
        sol += permutations(n, i)
    }
    return sol
}

func permutations(n int, i int) int {
    j := (n - i)/2
    k := i+j
    var larger, smaller int
    if i < j {
        larger = j
        smaller = i
    } else {
        larger = i
        smaller = j
    }
    
    sol := uint64(1)
    for l := k; l > larger; l-- {
        sol *= uint64(l)
    }
    
    for l := smaller; l > 0; l-- {
        sol /= uint64(l)
    }
    return int(sol)
}
