func maxProfit(prices []int) int {
    var profit int
    min := 65535

    for i:=0; i<len(prices)-1; i++ {
        if min > prices[i] {
            min = prices[i]
        } else {
            continue
        }
        
        for j := i+1; j<len(prices); j++ {
            curr_profit := prices[j] - prices[i]
            if profit < curr_profit {
                profit = curr_profit
            }
        }
    }
    
    return profit
}
