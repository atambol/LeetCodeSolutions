// O(n) time complexity, O(1) space complexity (in-place swapping)
func rotate(nums []int, k int)  {
    count := 0
    index := 0
    l := len(nums)
    for count < l {
        seen := false
        prev := nums[index]
        for pos:=index; pos != index || seen == false; pos = (pos+k)%l {
            seen = true
            next_pos := (pos+k)%l
            curr := nums[next_pos]
            nums[next_pos] = prev
            prev = curr
            count++
        }
        index++
    }
}
