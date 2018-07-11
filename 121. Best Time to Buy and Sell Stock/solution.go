func maxProfit(prices []int) int {
    var profit int
    min := 65535

    for _,price := range(prices) {
        if price < min {
            min = price
            continue
        }

        if profit < price - min {
            profit = price - min
        }
    }

    return profit
}
