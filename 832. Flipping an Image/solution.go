func flipAndInvertImage(A [][]int) [][]int {
    flip := make(map[int]int)
    flip[0] = 1
    flip[1] = 0
    
    for n := 0; n < len(A); n++ {
        i := 0
        j := len(A[n]) - 1
        
        for i < j {
            A[n][i], A[n][j] = flip[A[n][j]], flip[A[n][i]]
            i++
            j--
        }
        if i == j {
            A[n][j] = flip[A[n][j]]
        }
    }
    
    return A
}
