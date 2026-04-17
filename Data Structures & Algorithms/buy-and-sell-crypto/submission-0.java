class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int maxProfit = 0;
        for(int i = 0; i < prices.length; ++i){
            for(int j = i; j < prices.length; ++j){
                profit = prices[j] - prices[i]; 
                if(profit > maxProfit){
                    maxProfit = profit;
                }
            }
        }
        return maxProfit;
    }
}
