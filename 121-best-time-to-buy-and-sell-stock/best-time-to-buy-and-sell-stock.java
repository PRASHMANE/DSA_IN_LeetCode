class Solution {
    public int maxProfit(int[] prices) {
        int profit =0;
        int n = prices.length;
        int buy = 0 ,sell = 1;

        while (sell < n){
            if(prices[sell] > prices[buy]){
                profit = Math.max(profit,prices[sell]-prices[buy]);
            }
            else{
                buy=sell;
            }
            sell++;
        }

        return profit;
        
    }
}