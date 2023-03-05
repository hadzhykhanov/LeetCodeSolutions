import math
from heapq import heappop, heapify


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # O(n + k(logn + logk))
        for idx, item in enumerate(arr):
            arr[idx] = (abs(x - item), item)

        heapify(arr)

        out = [0] * k
        for i in range(k):
            out[i] = heappop(arr)[1]

        out.sort()
        return out


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # O(n + klogk)
        min_complement, min_complement_idx = math.inf, None
        for idx, item in enumerate(arr):
            complement = abs(item - x)
            arr[idx] = (item, complement)
            if complement < min_complement:
                min_complement, min_complement_idx = complement, idx

        out = [arr[min_complement_idx][0]]
        arr_idx = min_complement_idx
        left, right = arr_idx - 1, arr_idx + 1
        while len(out) != k:
            if left == -1:
                out.append(arr[right][0])
                right += 1

            elif right == len(arr):
                out.append(arr[left][0])
                left -= 1

            elif arr[left][1] <= arr[right][1]:
                out.append(arr[left][0])
                left -= 1
            else:
                out.append(arr[right][0])
                right += 1

        out.sort()
        return out


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda item: abs(x - item))
        return sorted(arr[:k])


