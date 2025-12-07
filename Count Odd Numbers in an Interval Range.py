class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if (high - low + 1) % 2 == 0:
            return (high - low + 1) // 2
        else:
            if low % 2 == 1 and high % 2 == 1:
                return (high - low + 1) // 2 + 1
            else:
                return (high - low + 1) // 2      
