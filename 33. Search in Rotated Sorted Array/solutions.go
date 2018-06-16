func search(nums []int, target int) int {
    end := len(nums) - 1
    start := 0

    for end >= start {
        mid := (end+start)/2
        fmt.Println(mid)
        if nums[mid] == target {
            return mid
        } else {
            if nums[mid] > nums[start] || nums[mid] > nums[end] {
                if target >= nums[start] && target < nums[mid] {
                    end = mid - 1
                } else {
                    start = mid + 1
                }
            } else {
                if target > nums[mid] && target <= nums[end] {
                    start = mid + 1
                } else {
                    end = mid - 1
                }
            }
        }
    }
    return -1
}
