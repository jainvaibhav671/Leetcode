
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/

class SummaryRanges:

    def __init__(self):
        self.arr: set = set()

    def addNum(self, value: int) -> None:
        self.arr.add(value)
        
    def getIntervals(self) -> List[List[int]]:
        intervals: List[List[int]] = []

        s: int = -1
        e: int = -1

        for num in sorted(self.arr):
            if s == -1:
                s = e = num
            elif  num - e == 1:
                e = num
            else:
                intervals.append( [s, e] )
                s = e = num
        if s != -1:
            intervals.append( [s, e] )
            
        return intervals                
        
# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
