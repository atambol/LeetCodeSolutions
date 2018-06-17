func myPow(x float64, n int) float64 {
    var isNegative bool
    if n == 0 {
        return 1
    } else if n == 1 {
        return x
    } else if n < 0 {
        isNegative = true
        n = n * -1
    } else {
        isNegative = false
    }
    
    var result float64 = 1
    val := x

    for n > 0 {
        if n&1 > 0 {
            result = result*val
        }
        val = val*val
        n = n>>1
    }
    if isNegative {
        return 1/result
    }
    return result
}
