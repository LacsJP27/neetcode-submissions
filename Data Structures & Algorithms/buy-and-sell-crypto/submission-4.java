class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 1;
        int maxGains = 0;

        while(r < prices.length) {
            if(prices[l] < prices[r]) {
                maxGains = Math.max(maxGains, prices[r] - prices[l]);
            } else {
                l = r;
            }
            ++r;
        }
        return maxGains;
    }
}
