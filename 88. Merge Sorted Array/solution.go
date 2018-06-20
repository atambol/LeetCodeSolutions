func merge(nums1 []int, m int, nums2 []int, n int)  {
    nums3 := make([]int, m)
    i := 0
    for i < m {
        nums3[i] = nums1[i]
        i++
    }
    
    i = 0
    j := 0
    k := 0
    for i < m && j < n {
        if nums3[i] < nums2[j] {
            nums1[k] = nums3[i]
            i++
        } else {
            nums1[k] = nums2[j]
            j++
        }
        k++
    }
    for i < m {
        nums1[k] = nums3[i]
        i++
        k++
    }
    for j < n {
        nums1[k] = nums2[j]
        j++
        k++
    }
}
