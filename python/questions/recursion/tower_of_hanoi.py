"""
Tower of hanoi problem

"""

def tower_of_hanoi_recursive(n, from_rod, aux_rod, to_rod):
    """
    The pattern:
    1. Shift n-1 disks from A to B
    2. Shift last disk from A to C
    3. Shift n-1 disks from B to C

    Time: O(2^n-1)
    Space: O(n)

    Space for parameter for each call is independent of n, ie. constant.
    When we do the 2nd recursive call, 1st recursive call is over. Language optimizations reuses the space
    of 1st call for 2nd call. Hence,
    T(n) = T(n-1) + k
    T(0) = k
    T(1) = 2k
    T(2) = 3k
    """
    if n == 1:
        print "move disk 1 from rod ", from_rod, " to rod ", to_rod
        return
    tower_of_hanoi_recursive(n-1, from_rod, to_rod, aux_rod)
    print "move disk", n, "from rod", from_rod, "to rod", to_rod
    tower_of_hanoi_recursive(n-1, aux_rod, from_rod, to_rod,)

def tower_of_hanoi_iterative(n, from_rod, aux_rod, to_rod):
    # calculate number of moves required
    moves = 2**n - 1
    
    # if number of disks is even then interchanges destination pole and
    # auxiliary pole
    if n % 2 == 0:
        # even
        to_rod, aux_rod = aux_rod, to_rod

    for i in xrange(1, moves+1):
        if i % 3 == 1:
            print "move disk", "from rod", from_rod, "to rod", to_rod
        elif i % 3 == 2:
            print "move disk", "from rod", from_rod, "to rod", aux_rod
        elif i % 3 == 0:
            print "move disk", "from rod", aux_rod, "to rod", to_rod
    return 

if __name__ == '__main__':
    tower_of_hanoi_recursive(3, 'A', 'B', 'C')
    tower_of_hanoi_iterative(3, 'A', 'B', 'C')