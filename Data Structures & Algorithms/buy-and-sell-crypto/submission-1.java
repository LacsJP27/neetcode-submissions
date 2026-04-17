class Solution {
    public int maxProfit(int[] prices) {
        int ptr1 = 0;
        int ptr2 = prices.length - 1;
        int maxProfit = 0;

        while(ptr1 < ptr2){
            while(ptr1 < ptr2){
                int profit = prices[ptr2] - prices[ptr1];
                if( profit > maxProfit){
                    maxProfit = profit;
                }
                --ptr2;
            }
            ++ptr1;
            ptr2 = prices.length - 1;
        }

        return maxProfit;
            
    }
}
