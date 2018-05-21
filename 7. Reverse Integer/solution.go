func reverse(x int) int {
    rev := 0
    sign := 1
    if x < 0 {
        sign = -1
        x *= -1
    }
    for x != 0 {
        rev = rev*10 + x%10
        x = x/10
    }
    rev = sign*rev
    if rev != int(int32(rev)) {
        return 0
    }
    return rev
}
