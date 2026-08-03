class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxP = 0;
        int l = 0;
        int r = 1;

        while (r < prices.size()) {
            int profit = prices[r] - prices[l];
            maxP = std::max(maxP, profit);

            if (prices[r] < prices[l]) {
                l = r;
            }

            r++;
        }

        return maxP;
    }
};
