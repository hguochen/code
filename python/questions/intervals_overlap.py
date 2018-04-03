"""
https://www.geeksforgeeks.org/check-if-any-two-intervals-overlap-among-a-given-set-of-intervals/

An interval is represented as a combination of start time and end time.
Given a set of intervals check if any two intervals overlap.

"""

class Result(object):
    """docstring for Result"""
    def __init__(self):
        self.overlaps = 0
        self.intervals = []
        
def intervals_overlap_brute(schedule):
    """
    return the number of overlaps and the overlap intervals
    Time: O(n^2)
    Space: O(1)
    where n is the number of schedule
    """
    if not schedule:
        return None
    elif len(schedule) == 1:
        return None
    result = Result()
    for i in xrange(len(schedule)-1):
        for j in xrange(i+1, len(schedule)):
            earlier = schedule[i]
            later = schedule[j]
            # define earlier timeslot if they are reverse
            if earlier[0] > later[0]:
                earlier, later = later, earlier
            if overlap(earlier, later):
                result.overlaps += 1
                result.intervals.append([earlier, later])
    print result.overlaps, result.intervals
    return result

def intervals_overlap(schedule):
    """
    Sort the schedule in ascending order of start time.
    Compare each set of 2 schedule for overlaps
    Time: O(n)
    Space: O(1)
    where n is the number of schedules
    """
    if not schedule:
        return None
    elif len(schedule) == 1:
        return None
    result = Result()
    sorted_schedule = sorted(schedule, key=lambda item: item[0])
    # loop through schedule starting from the second schedule
    for i in xrange(1,len(sorted_schedule)):
        if overlap(sorted_schedule[i-1], sorted_schedule[i]):
            result.overlaps += 1
            result.intervals.append([sorted_schedule[i-1], sorted_schedule[i]])
    print result.overlaps, result.intervals
    return result

def overlap(earlier, later):
    if earlier[0] == later[0] or later[0] < earlier[1]:
        return True
    return False

if __name__ == '__main__':
    arr1 = [[1,3], [5,7], [2,4], [6,8]]

    intervals_overlap_brute(arr1)
    intervals_overlap(arr1)
