func singleNumber(nums []int) int {
    unique := nums[0]
    for i:=1; i<len(nums); i++ {
        unique ^= nums[i]
    }
    return unique
}
