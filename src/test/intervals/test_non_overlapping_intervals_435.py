from unittest import TestCase

from leetcode75.intervals.non_overlapping_intervals_435 import Solution


class TestSolution(TestCase):

    def test_erase_overlap_intervals_example1(self):
        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        sol = Solution()
        result = sol.eraseOverlapIntervals(intervals)
        self.assertEqual(1, result)

    def test_erase_overlap_intervals_example2(self):
        intervals = [[1, 2], [1, 2], [1, 2]]
        sol = Solution()
        result = sol.eraseOverlapIntervals(intervals)
        self.assertEqual(2, result)

    def test_erase_overlap_intervals_example3(self):
        intervals = [[1, 2], [2, 3]]
        sol = Solution()
        result = sol.eraseOverlapIntervals(intervals)
        self.assertEqual(0, result)

    def test_erase_overlap_intervals_example4(self):
        intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
        sol = Solution()
        result = sol.eraseOverlapIntervals(intervals)
        self.assertEqual(2, result)

    def test_erase_overlap_intervals_example5(self):
        intervals = [[1, 2], [2, 3], [3, 4], [-100, -2], [5, 7]]
        sol = Solution()
        result = sol.eraseOverlapIntervals(intervals)
        self.assertEqual(0, result)
