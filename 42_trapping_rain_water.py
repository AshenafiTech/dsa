class Solution:
    def trap(self, height: List[int]) -> int:
        
        left, right = 0, len(height)-1
        l_max, right_max = 0, 0
        water = 0

        while left <= right:
            if height[left] < height[right]:
                if height[left] > l_max:
                    l_max = height[left]
                else:
                    water += l_max-height[left]
                left+=1

            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    water += right_max-height[right]
                right-=1

        return water
