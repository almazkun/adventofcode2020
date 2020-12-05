"""
--- Day 2: Password Philosophy ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
"""
file = "02_input.txt"

test_obj = [
    ("1-3 a: abcde", True),
    ("1-3 b: cdefg", False),
    ("2-9 c: ccccccccc", True),
]

def get_policy(path: str) -> str:
    with open(path, "r") as f:
        for line in f:
            yield line.strip('\n')


def get_min_max(policy: str) -> tuple:
    f_l = policy.split(" ")[0]
    _min = int(f_l.split("-")[0])
    _max = int(f_l.split("-")[-1])
    return (_min, _max)

assert get_min_max(test_obj[0][0]) == (1, 3)
assert get_min_max(test_obj[1][0]) == (1, 3)
assert get_min_max(test_obj[2][0]) == (2, 9)


def get_obj(policy: str) -> str:
    return policy.split(" ")[1].strip(":")


assert get_obj(test_obj[0][0]) == "a"
assert get_obj(test_obj[1][0]) == "b"
assert get_obj(test_obj[2][0]) == "c"


def get_subj(policy: str) -> str:
    return policy.split(" ")[2]


assert get_subj(test_obj[0][0]) == "abcde"
assert get_subj(test_obj[1][0]) == "cdefg"
assert get_subj(test_obj[2][0]) == "ccccccccc"


def get_cunt(obj: str, subj: str) -> int:
    count = 0
    for i in subj:
        if i == obj:
            count += 1
    return count


assert get_cunt(get_obj(test_obj[0][0]), get_subj(test_obj[0][0])) == 1
assert get_cunt(get_obj(test_obj[1][0]), get_subj(test_obj[1][0])) == 0
assert get_cunt(get_obj(test_obj[2][0]), get_subj(test_obj[2][0])) == 9


def is_valid(policy: str) -> bool:
    _min, _max = get_min_max(policy)
    obj = get_obj(policy)
    subj = get_subj(policy)
    count = get_cunt(obj, subj)
    
    if _min <= count <= _max:
        return True
    return False


for test in test_obj:
    assert is_valid(test[0]) == test[1]


results = {}
for pol in get_policy(file):
    try: 
        results[is_valid(pol)].append(pol)
    except KeyError:
        results[is_valid(pol)] = [pol]


print(len(results[True]))

"""
--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
"""
p2_test = [
    ("1-3 a: abcde", True),
    ("1-3 b: cdefg", False),
    ("2-9 c: ceccccccc", True),
    ("2-9 c: ccccccccc", False),

    
]

def there(i: int, obj: str, subj: str) -> bool:
    i -= 1
    if subj[i] == obj:
        return True
    return False


assert there(1, "a", "abcde") == True
assert there(3, "a", "abcde") == False
assert there(1, "d", "cdefg") == False
assert there(3, "d", "cdefg") == False
assert there(2, "c", "ccccccccc") == True
assert there(9, "c", "ccccccccc") == True
assert there(2, "c", "ceccccccc") == False
assert there(9, "c", "ccccccccc") == True


def only_one(one: bool, two: bool) -> bool:
    if one and not two:
        return True
    elif not one and two:
        return True
    else:
        return False

def p2_is_valid(policy: str) -> bool:
    i1, i2 = get_min_max(policy)
    obj = get_obj(policy)
    subj = get_subj(policy)
    
    is_there_1 = there(i1, obj, subj)
    is_there_2 = there(i2, obj, subj)
    
    return only_one(is_there_1, is_there_2)


for test in p2_test:
    print(test[0], test[1], p2_is_valid(test[0]))
    assert p2_is_valid(test[0]) == test[1]


results = {}
for pol in get_policy(file):
    try: 
        results[p2_is_valid(pol)].append(pol)
    except KeyError:
        results[p2_is_valid(pol)] = [pol]


print(len(results[True]))