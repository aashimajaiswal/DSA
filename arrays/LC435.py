class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        # Algorithm: keep the meeting that r short/end early to make space for more

        # sort on end
        intervals.sort(key = lambda x:x[1])

        removed = 0
        prev = 0

        for i in range(1,len(intervals)):

            # remove condition
            if intervals[i][0] < intervals[prev][1]:
                removed += 1
            else: 
                # not removed
                prev = i
        
        return removed