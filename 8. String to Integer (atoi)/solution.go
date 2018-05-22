import "regexp"
func myAtoi(str string) int {
    INT_MAX := 2147483647
    INT_MIN := 2147483648
    output := 0
    sign := 1
    initial_whitespaces := true
    for i:=0;i<len(str);i++ {
        char := string(str[i])
        if initial_whitespaces == true && char == " " {
            continue
        }
        if initial_whitespaces == true && (char == "-" || char == "+") {
            initial_whitespaces = false
            if char == "-" {
                sign = -1
            }
            continue
        }
        initial_whitespaces = false
        var atoi int 
        switch char  {
            case "1":
                atoi = 1
            case "2":
                atoi = 2
            case "3":
                atoi = 3
            case "4":
                atoi = 4
            case "5":
                atoi = 5
            case "6":
                atoi = 6
            case "7":
                atoi = 7
            case "8":
                atoi = 8
            case "9":
                atoi = 9
            case "0":
                atoi = 0
            default:
                atoi = -1
        }
        if atoi == -1 {
            break
        }
        output = output*10 + atoi
        if sign == -1 && output > INT_MIN {
            return sign*INT_MIN
        }
        if sign == 1 && output > INT_MAX {
            return INT_MAX
        }
    }
    return output*sign
}
