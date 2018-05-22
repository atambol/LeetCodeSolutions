func maxArea(height []int) int {
    area := 0
    var newarea int
    for i := 0; i < len(height); i++ {
        for j := i+1; j < len(height); j++ {
            if height[i] < height[j] {
                newarea = height[i] * (j - i)
            } else {
                newarea = height[j] * (j - i)
            }
            if newarea > area {
                area = newarea
            }
        }
    }
    return area
}
