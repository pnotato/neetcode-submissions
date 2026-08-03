class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int profitMax = 0;
        for (int r = 0; r < prices.size(); r++) {
            if (prices[r] < prices[l]) {
                l = r;
            }
            else {
                int profit = prices[r] - prices[l];
                profitMax = profitMax > profit ? profitMax : profit;
            }
        }

        return profitMax;
    }
};
