func permute(nums []int) [][]int {
    if len(nums) == 1 {
        return [][]int{nums}
    }
    var sol [][]int
    for i:=0;i<len(nums);i++{
        num0 := []int{nums[i]}
        
        // Split the slice around the current index and create a new slice without the current element
        a1, a2 := split(nums, i)
        nums1 := append(a1, a2...)
        
        // Get all permuations of the new slice
        nums2 := permute(nums1)
        
        // Prepend the current element to the permutations
        for j:=0;j<len(nums2);j++{
            sol = append(sol, append(num0, nums2[j]...))
        }
    }
    return sol
}

func split(nums []int, k int) ([]int, []int) {
    var a1 []int
    var a2 []int
    for i:=0;i<len(nums);i++ {
        if i < k {
            a1 = append(a1, nums[i])
        } else if i > k {
            a2 = append(a2, nums[i])
        }
    }
    return a1, a2
}
