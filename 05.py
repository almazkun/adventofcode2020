"""
--- Day 5: Binary Boarding ---

You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
"""
path = "05_input.txt"
file = "test.txt"

all_codes = []

with open(file, "r") as f:
    for l in f.readlines():
        all_codes.append(l.rstrip())


class Code:
    def __init__(self, code):
        self.code = code
        self.row = None
        self.col = None
    
    def half(self, arr, half):
        l = len(arr)
        h2 = l//2
        if not l % 2:
            if half == "F" or half == "L":
                return arr[:h2]
            if half == "B" or half == "R":
                return arr[h2:]
        else:
            return arr
        
    def get_row(self, arr=None):
        if arr is None:
            arr = [x for x in range(0, 128)]
        while len(arr) > 1:
            for half in self.code[:7]:
                arr = self.half(arr, half)
        self.row = int(arr[0])
        return self.row
    
    def get_col(self, arr=None):

        if arr is None:
            arr = [x for x in range(0, 8)]
        while True:
            for half in self.code[7:]:
                arr = self.half(arr, half)
            if len(arr) == 1:
                break
        self.col = int(arr[0])
        return self.col
    
    def get_seat_id(self):
        self.get_row()
        self.get_col()
        self.seat_id = self.row * 8 + self.col
        return self.seat_id
         
        
        
tests = [
    (70, 7, 567),
    (14, 7, 119),
    (102, 4, 820),
]

def maxest():
    ids = []
    for code in all_codes:
        c = Code(code)
        c.get_seat_id()
        ids.append(c.seat_id)
    return ids


def a_ids():
    a_ids = []
    for r in [x for x in range(1,127)]:
        for c in [x for x in range(1, 6)]:
            i = r * 8 + c
            a_ids.append(i)
    return a_ids
"""
--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?

Your puzzle answer was 669.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your Advent calendar and try another puzzle.
"""
        
a_ = a_ids()
ii = maxest()

def dif():
    nots = []
    for a in a_:
        if a not in ii:
            nots.append(a)
    print(nots)

dif() #669