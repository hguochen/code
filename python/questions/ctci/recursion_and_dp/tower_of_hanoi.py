"""
CtCi
8.6 In the classic problems of the Towers of Hanoi, you have 3 towers and N disks
of different sizes which can slide onto any tower. The puzzle starts with disks sorted
in ascending order of size from top to bottom(i.e, each disk sits on top of an even larger one).
You have the following constraints:
1. Only one disk can be moved at a time
2. A disk is slid off the top of one tower onto another tower
3. A disk cannot be placed on top of a smaller disk.
Write a program to move the diskd from the first tower to the last using stacks.
"""

def tower_of_hanoi(n, source, aux, dest):
    """
    Time: O(2^n)
    Space: O(2^n)
    """
    if n < 1:
        return
    tower_of_hanoi(n-1, source, dest, aux)
    print "move top disk from", source, "to", dest
    tower_of_hanoi(n-1, aux, source, dest)

if __name__ == '__main__':
    tower_of_hanoi(3, "src", "aux", "dest")
