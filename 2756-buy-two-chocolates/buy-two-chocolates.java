class Solution {
    public int buyChoco(int[] prices, int money) {
        int cho = 0, temp = money;

        Arrays.sort(prices);
        for (int i=0 ;i < prices.length;i++){
            if (prices[i] <= temp && temp > -1 && cho < 2 ){
                cho++;
                temp-=prices[i];  
            }
            if(cho == 2 && temp > -1){
                return temp;
            }
        }
        return money;
        
    }
}