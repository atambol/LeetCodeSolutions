func maxProfit(prices []int) int {
    var profit int
    for i:=1; i< len(prices); i++ {
        if prices[i] > prices[i-1] {
            profit += prices[i] - prices[i-1] 
        }
    }
    return profit
}
