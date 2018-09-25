func findDuplicate(nums []int) int {
    n := len(nums)
    for i := 1; i < n+1; i++ {
        count := 0
        for j := 0; j < n; j++ {
            if nums[j] == i {
                count++
            }
        }
        if count > 1 {
            return i
        }
    }
    return 1
}
