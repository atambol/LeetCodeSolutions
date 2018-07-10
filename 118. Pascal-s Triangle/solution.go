func generate(numRows int) [][]int {
    if numRows == 0 {
        var sol = [][]int{}
        return sol
    } else if numRows == 1 {
        var sol = [][]int{{1}}
        return sol
    } else if numRows == 2 {
            var sol = [][]int{{1},{1,1}}
        return sol
    }
    var sol = [][]int{{1},{1,1}}

    for i:=2; i<numRows; i++ {
        var sol2 = []int{1}
        for j:=0; j<len(sol[i-1])-1; j++ {
            sol2 = append(sol2, sol[i-1][j] + sol[i-1][j+1])
        }
        sol2 = append(sol2, 1)
        sol = append(sol, sol2)
    }
    return sol
}
