class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        minHeap = []
        for i in range(len(points)):
            minHeap.append(((points[i][0]**2 + points[i][1]**2), points[i]))
        heapq.heapify(minHeap)
        for i in range(k):
            result.append(heapq.heappop(minHeap)[1])
        return result