func getRow(rowIndex int) []int {
    if rowIndex == 0 {
        var sol = []int{1}
        return sol
    } else if rowIndex == 1 {
        var sol = []int{1,1}
        return sol
    }
    var prev = []int{1,1}

    for i:=1; i<rowIndex; i++ {
        var curr = []int{1}
        for j:=0; j<len(prev)-1; j++ {
            curr = append(curr, prev[j] + prev[j+1])
        }
        curr = append(curr, 1)
        prev = curr
    }
    return prev
}
