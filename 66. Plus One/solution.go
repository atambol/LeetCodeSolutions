func plusOne(digits []int) []int {
    carry := 1
    for i := len(digits)-1; i >= 0; i-- {
        num := carry + digits[i]
        digits[i] = num % 10
        if digits[i] == num {
            return digits
        } else {
            carry = 1
        }
    }
    return append([]int{carry}, digits...)
    
}
