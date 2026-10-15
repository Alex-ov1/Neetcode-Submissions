class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = []
        for i in range(len(prices)):
            moins = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    moins = prices[j]
                    break

            l.append(prices[i] - moins)
        return l