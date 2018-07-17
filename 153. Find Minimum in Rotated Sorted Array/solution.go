func findMin(nums []int) int {
    // Assumes there will be atleast one element
    if len(nums) == 1 {
        return nums[0]
    }
    
    // Get the Pivot's index
    pivot := getPivot(nums, 0, len(nums)-1)
    return nums[pivot]
}

func getPivot(nums []int, i int, j int) int {
    if i == j - 1 {
        if nums[i] > nums[j] {
            return j
        } else {
            return i
        }
    } else {
        mid := (i + j)/2
        if nums[i] < nums[mid] && nums[mid] < nums[j] {
            return i
        } else if nums[i] > nums[mid] {
            return getPivot(nums, i, mid)
        } else {
            return getPivot(nums, mid, j)
        }
    }
}
