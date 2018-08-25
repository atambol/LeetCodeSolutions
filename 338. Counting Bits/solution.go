func countBits(num int) []int {
    if num == 0 {
        return []int{0}
    } 

    if num == 1 {
        return []int{0, 1}
    }
    
    res := make([]int, num+1, num+1)
    res[0] = 0
    res[1] = 1
    diff := 2
    checkpoint := 4
    for i := 2; i <= num; i++ {
        if i == checkpoint {
            diff = checkpoint
            checkpoint = checkpoint * 2
        }
        res[i] = 1 + res[i-diff]
    }
    return res
}
