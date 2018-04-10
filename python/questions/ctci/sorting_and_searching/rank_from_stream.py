"""
CtCi
10.10 Imagine you are reading in a stream of integers. Periodically, you wish to be
able to look up the rank of a number x ( the number of values less than or equal to x).
implement the data structures and algorithms to support these operations. That is, implement
the method track(int x), which is called when each number is generated, and the method
getRankOfNumber(int x), which returns the number of values less than or equal to x(not including
x itself).

"""

class Rank(object):
    def __init__(self):
        self.rank = []

    def track(self, x):
        if len(self.rank) < 1:
            self.rank.append(x)
            return
        idx = -1
        for i in xrange(len(self.rank)-1, -1, -1):
            if x < self.rank[i]:
                idx = i
            else:
                break
        if idx == -1:
            self.rank.append(x)
        else:
            self.rank.insert(idx, x)
        return

    def get_ranks(self):
        return self.rank

    def get_rank_of_number(self, x):
        return self.binary_search(x, 0, len(self.rank)-1)

    def binary_search(self, val, low, high):
        if low > high:
            return -1
        mid = (low + high) / 2
        if self.rank[mid] == val:
            while self.rank[mid] == val:
                mid += 1
            return mid - 1
        if val < self.rank[mid]:
            return self.binary_search(val, low, mid-1)
        return self.binary_search(val, mid+1, high)

if __name__ == '__main__':
    arr1 = [5,1,4,4,5,9,7,13,3]
    rank = Rank()
    rank.track(5)
    rank.track(1)
    rank.track(4)
    rank.track(4)
    rank.track(5)
    rank.track(9)
    rank.track(7)
    rank.track(13)
    rank.track(3)
    print rank.get_ranks()
    print rank.get_rank_of_number(1) # 0
    print rank.get_rank_of_number(3) # 1
    print rank.get_rank_of_number(4) # 3
