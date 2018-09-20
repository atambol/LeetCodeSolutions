func isPowerOfTwo(n int) bool {
    if n < 0 {
        return false
    }
    
    bitMask := 1
    countOfOne := 0

    for i:=0; i<32; i++ {
        lastBit := bitMask & n
        n = n >> 1
        countOfOne += lastBit
    }
    
    if countOfOne == 1 {
        return true
    } else {
        return false
    }
}
