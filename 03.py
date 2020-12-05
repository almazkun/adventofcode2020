"""
--- Day 3: Toboggan Trajectory ---

With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
"""
file = "03_input.txt"

lines = ["..##.......", "#...#...#..", ".#....#..#.", "..#.#...#.#", ".#...##..#.", "..#.##.....", ".#.#.#....#", ".#........#", "#.##...#...", "#...##....#", ".#..#...#.#"]
test = (lines, 7)

line = "01234567890"
test_obj = [(0, 3),(1, 4),(2, 5),(3, 6),(4, 7),(5, 8),(6, 9),(7, 10), (8, 0),(9, 1),(10, 2),]

def get_next_index(line: str, index: int, step: int) -> int:
    _len = len(line)
    _next_index = index + step
    if _next_index < _len:
        return _next_index
    elif _next_index >= _len:
        return _next_index - _len


for index, outcome in test_obj:
    assert get_next_index(line, index, 3) == outcome


def is_tree(line, index):
    _sub = line[index]
    if _sub == ".":
        return False
    elif _sub == "#":
        return True


assert not is_tree("..##.......", 0)
assert not is_tree("..##.......", 1)
assert is_tree("..##.......", 2)
assert is_tree("..##.......", 3)
assert not is_tree("..##.......", 10)


def tree_in_line(line, trees, index, step):
    try:
        trees[is_tree(line, index)] += 1
    except KeyError:
        trees[is_tree(line, index)] = 1
    return (trees, get_next_index(line, index, step))


def more_down(lines, index):
    _len = len(lines)
    if index < _len:
        return True
    elif index >= _len:
        return False

assert more_down("0123", 3)
assert not more_down("0123", 4)
assert not more_down("0123", 5)


def all_trees(lines, right, down):
    trees = {}
    index = 0
    i = 0
    for _ in lines:
        if more_down(lines, i):
            line = lines[i]
            if i == 0:
                index = get_next_index(line, index, step=right)
                i += down
            else:
                trees, index = tree_in_line(line, trees, index, step=right)
                i += down
    return trees[True]

assert all_trees(lines, right=3, down=1) == 7


def get_line(path: str) -> str:
    with open(path, "r") as f:
        for line in f:
            yield line.strip('\n')

lin = [x for x in get_line(file)]
assert all_trees(lin, right=3, down=1) == 252


"""
--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

r1d1 = 2
assert all_trees(lines, right=1, down=1) == 2

r3d1 = 7
assert all_trees(lines, right=3, down=1) == 7

r5d1 = 3
assert all_trees(lines, right=5, down=1) == 3

r7d1 = 4
assert all_trees(lines, right=7, down=1) == 4

r1d2 = 2
assert all_trees(lines, right=1, down=2) == 2

assert (r1d1* r3d1*r5d1*r7d1*r1d2) == 336



lines = [x for x in get_line(file)]
r1d1 = all_trees(lines, right=1, down=1)
r3d1 = all_trees(lines, right=3, down=1)
r5d1 = all_trees(lines, right=5, down=1)
r7d1 = all_trees(lines, right=7, down=1)
r1d2 = all_trees(lines, right=1, down=2)

print(r1d1* r3d1*r5d1*r7d1*r1d2) #2608962048
