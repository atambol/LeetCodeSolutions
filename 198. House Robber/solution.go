func rob(nums []int) int {
    l := len(nums)
    profit := make([]int, l, l)
    if l == 0 {
        return 0
    } else if l == 1 {
        return nums[0]
    } else if l == 2 {
        return max(nums[0], nums[1]) 
    } 
    
    profit[0] = nums[0]
    profit[1] = nums[1]
    profit[2] = nums[0] + nums[2]
    
    if l == 3 {
        return max(profit[2], profit[1])
    }
    
    for i := 3; i < l; i++ {
        profit[i] = max(profit[i-2], profit[i-3]) + nums[i]
    }
        
    return max(profit[l-2], profit[l-1])
}

func max(a int, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}
