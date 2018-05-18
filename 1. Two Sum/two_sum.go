func twoSum(nums []int, target int) []int {
    var x int
    for i, num1 := range nums {
        diff := target - num1
        found := false
        
        for j, num2 := range nums[i+1:] {
            if num2 == diff {
                found = true
                x = j + i + 1
            } 
        }

        if found == true {
            return []int{i,x}
        }
    }
    return []int{}
}
