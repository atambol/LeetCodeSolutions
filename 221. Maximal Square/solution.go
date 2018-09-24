func min(x, y, z int) int {
    if x < y {
        if x < z {
            return x
        } else {
            return z
        }
    } else {
        if y < z {
            return y
        } else {
            return z
        }
    }
}

func maximalSquare(matrix [][]byte) int {    
    // initialise the helper matrix
    l1 := len(matrix)
    if l1 == 0 {
        return 0
    }
    l2 := len(matrix[0])
    if l2 == 0 {
        return 0
    }
    
    dp := make([][]int, l1+1, l1+1)
    for i := 0; i < l1+1; i++ {
        dp[i] = make([]int, l2+1, l2+1)
    }
    
    // store the square areas
    max := 0
    for i:=0; i<l1; i++ {
        for j:=0; j<l2; j++ {
            if matrix[i][j] == 49 {
                // get the minimum
                dp[i+1][j+1] = 1 + min(dp[i][j], dp[i][j+1], dp[i+1][j])
                
                // update the max side length
                if max < dp[i+1][j+1] {
                    max = dp[i+1][j+1]
                }
            }
        }
    }
    fmt.Println(dp)
    return max*max
}
