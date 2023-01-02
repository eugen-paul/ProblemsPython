from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        max_height = 0
        end_right = 0

        #in outer loop I go from linsks to right. For each element the largest area is searched.
        for start in range(len(height)-1):
            if height[start] == 0 or height[start] <= max_height:
                continue
            
            max_height = height[start]

            if max_area == 0:
                start_delta = 1
            else:
                start_delta = max_area // height[start]

            #In inner loop I go from right to left.
            #The end of the inner loop depends on previously found maximum area.
            current = len(height)-1-end_right
            end = start+start_delta
            while current >= end:
                area = (current - start) * min(height[start], height[current])
                #Move the end if new maximum area was found.
                if max_area < area:
                    max_area = area
                    start_delta = max_area // height[start]
                    end = start+start_delta
                if height[current] >= height[start]:
                    break
                current-=1

            #Additionally, after checking, you can move the beginning of the inner loop 
            #if the current position of the outer loop is greater than or equal to the last element. 
            # Because there will be no other area that will be greater than current start and current end.
            if height[start] >= height[len(height)-1-end_right]:
                end_right+=1

        return max_area
    
    def maxArea_approach_2(self, height: List[int]) -> int:
        max_area = 0

        left, right = 0, len(height)-1
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
            
        return max_area

    def maxArea_dumb_3(self, height: List[int]) -> int:
        max_area = 0

        max_height = 0

        for start in range(len(height)-1):
            if height[start] == 0 or height[start] <= max_height:
                continue
            
            max_height = max(max_height,height[start])

            if max_area == 0:
                start_delta = 1
            else:
                start_delta = max_area // height[start]

            for current in range(len(height)-1, start+start_delta-1, -1):
                area = (current - start) * min(height[start], height[current])
                max_area = max(area, max_area)
                if height[current] >= height[start]:
                    break

        return max_area
    
    def maxArea_dumb_2(self, height: List[int]) -> int:
        max_area = 0

        for start in range(len(height)-1):
            if height[start] == 0:
                continue

            if max_area == 0:
                start_delta = 1
            else:
                start_delta = max_area // height[start]

            for current in range(len(height)-1, start+start_delta-1, -1):
                area = (current - start) * min(height[start], height[current])
                max_area = max(area, max_area)
                if height[current] >= height[start]:
                    break

        return max_area

    def maxArea_dumb(self, height: List[int]) -> int:
        max_area = 0

        for start in range(len(height)-1):
            if height[start] == 0:
                continue

            if max_area == 0:
                start_delta = 1
            else:
                start_delta = max_area // height[start]

            for current in range(start+start_delta, len(height)):
                area = (current - start) * min(height[start], height[current])
                max_area = max(area, max_area)

        return max_area


def do_test(i: int, s, r):
    c = Solution()
    resp = c.maxArea(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)

def do_test2(i: int, s, r):
    c = Solution()
    resp = c.maxArea_approach_2(s)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, [1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
    do_test(1, [1, 1], 1)
    do_test(2, [1, 1, 1, 1], 3)
    do_test(3, [1, 1, 1, 1], 3)
    do_test(4, [1, 10, 1, 1], 3)
    do_test(5, [1, 10, 1, 1], 3)
    do_test(6, [1, 0, 0, 1], 3)
    do_test(7, list(range(0,10001)) + list(range(9999,0,-1)), 50000000)

    do_test2(0, [1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
    do_test2(1, [1, 1], 1)
    do_test2(2, [1, 1, 1, 1], 3)
    do_test2(3, [1, 1, 1, 1], 3)
    do_test2(4, [1, 10, 1, 1], 3)
    do_test2(5, [1, 10, 1, 1], 3)
    do_test2(6, [1, 0, 0, 1], 3)
    do_test2(7, list(range(0,10001)) + list(range(9999,0,-1)), 50000000)
