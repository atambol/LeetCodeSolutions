func rotate(matrix [][]int) {
    N := len(matrix) - 1
    for i:=0; i<len(matrix)/2; i++ {
        upperLimit := N-i
        lowerLimit := i

        for j:=lowerLimit; j < upperLimit; j++ {
            diff := j - i
            tmp := matrix[i][j]
            matrix[i][j] = matrix[upperLimit-diff][i]
            matrix[upperLimit-diff][i] = matrix[upperLimit][upperLimit-diff]
            matrix[upperLimit][upperLimit-diff] = matrix[j][upperLimit]
            matrix[j][upperLimit] = tmp
        }
    }
}
