"""
CtCi
10.6 Imagine you have a 20GB file with one string per line. Explain how you
would sort the file.
"""

# 1. break up to 20GB into 20,000 files of 1MB file size each.
# 2. use mergesort to sort each 1MB file.
# 3. after all files are independently sorted, we use the merge procedure(from mergesort) to merge
# each pairs of files together. after step 3, we would have 10,000 files independently merged
# 4. we repeatedly use merge procedure to merge each pairs of files until we have 1 file left of 20GB
# size.
# 5. now the file is sorted

# This algorithm is known as external sort
# Time: O(nlgn)
# Space: O(20GB)
