from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        x = arr.index(max(arr))
        if x == 0 or x == len(arr) - 1:
            return False
        if arr[:x] != sorted(arr[:x]) or len(set(arr[:x])) != len(arr[:x]):
            return False
        if arr[x:] != list(reversed(sorted(arr[x:]))) or len(set(arr[x:])) != len(arr[x:]):
            return False
        return True

        