# Best Time to Buy and Sell Stock

## Approach
Keep track of the cheapest stock price seen so far.  
For each price, calculate the profit we would make if we sold at the current price after buying at the cheapest previous price.

Update the cheapest price whenever a lower price is found.  
Keep track of the maximum profit found and return it at the end.

## Complexity
Time: O(n), because we go through the prices once.  
Space: O(1), because only a few variables are used.
