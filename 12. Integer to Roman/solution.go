var mymap = map[int]string{1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}

func intToRoman(num int) string {
    roman := ""
    for divisor:= 1000; divisor >= 1; divisor /= 10 {
        quotient := num / divisor
        remainder := num % divisor
        if remainder != num {
            roman += convert(divisor, quotient)
            num = remainder
        }
    }
    return roman
}

func convert(optionA int, quo int) string {
    optionB := optionA*5
    switch quo {
        case 1:
            return mymap[optionA]
        case 2:
            return mymap[optionA] + mymap[optionA]
        case 3:
            return mymap[optionA] + mymap[optionA] + mymap[optionA]
        case 4:
            return mymap[optionA] + mymap[optionB]
        case 5:
            return mymap[optionB]
        case 6:
            return mymap[optionB] + mymap[optionA]
        case 7:
            return mymap[optionB] + mymap[optionA] + mymap[optionA]
        case 8:
            return mymap[optionB] + mymap[optionA] + mymap[optionA] + mymap[optionA]
        case 9:
            return mymap[optionA] + mymap[optionA*10]
    }
    return ""
}


