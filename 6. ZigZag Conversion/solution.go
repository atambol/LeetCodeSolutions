func convert(s string, numRows int) string {
    zigzag := make([]string, numRows)
    l := len(s)
    if l < 2 || numRows == 1 {
        return s
    }

    width := numRows * 2 - 2
    columns := l / width
    
    if l % width != 0 {
        columns++
    }

    for i := 0; i < columns; i++ {
        iByColumns := i * width
        j := 0
        for j < numRows {
            k := iByColumns + j
            if k >= l {
                break
            }
            zigzag[j] += s[k:k+1]
            j++
        }

        for j < width {
            k := iByColumns + j
            if k >= l {
                break
            }
            zigzag[width - j] += s[k:k+1]
            j++
        }
    }

    output := ""
    for i := 0; i< numRows; i++ {
        output += zigzag[i]
    }
    return output
}
