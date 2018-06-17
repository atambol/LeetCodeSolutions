func getpowers(n int) []int {
    poweroftwo := []int{1}
    var result []int
    prev := 1
    for i:=2; i <= n ; i=i*2 {
        poweroftwo = append(poweroftwo, i)
        if n == i {
            result = append(result, i)
            return result
        }
        prev = i
    }

    result = append(result, prev)
    n = n - prev
    for n > 0 {

        if poweroftwo[len(poweroftwo)-1] <= n {
        result = append(result, poweroftwo[len(poweroftwo)-1])
            n = n - poweroftwo[len(poweroftwo)-1]
        }
        poweroftwo = poweroftwo[:len(poweroftwo)-1]
    }
    return result
}

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
    
    powers := getpowers(n)
    var result float64 = 1
    val := x
    pow := 1

    for len(powers) > 0 {
        if powers[len(powers)-1] == pow {
            powers = powers[:len(powers)-1]
            result = result*float64(val)
        }
        pow = pow*2
        val = val*val
    }
    if isNegative {
        return 1/result
    }
    return result
}
