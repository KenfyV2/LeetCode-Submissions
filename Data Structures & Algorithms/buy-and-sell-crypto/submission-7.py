class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        cheapest = prices[0]

        for num in prices:
            cheapest = min(cheapest,num)
            profit = num-cheapest
            res = max(res,profit)

        return res