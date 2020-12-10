"""
--- Day 4: Passport Processing ---

You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)

Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in


The first passport is valid - all eight fields are present. 
The second passport is invalid - it is missing hgt (the Height field).
The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.
The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

To begin, get your puzzle input.
"""

def all_pass(lines):
    all_pass = []
    passp = {}
    for line in lines:
        if line == "\n":
            all_pass.append(passp)
            passp = {}
        elif line:
            passp = get_p(line, passp)
    return all_pass


def get_p(line, passp):
    for i in line.strip("\n").split(" "):
        k, v = get_dict(i)
        passp[k] = v
    return passp


def get_dict(string):
    return string.split(":")

"""
def is_valid(passp):
    byr = bool(passp.get("byr", False))
    iyr = bool(passp.get("iyr", False))
    eyr = bool(passp.get("eyr", False))
    hgt = bool(passp.get("hgt", False))
    hcl = bool(passp.get("hcl", False))
    ecl = bool(passp.get("ecl", False))
    pid = bool(passp.get("pid", False))

    musts = [byr, iyr, eyr, hgt, hcl, ecl, pid]

    if all(x for x in musts):
        return True
    else:
        return False


def count_valid(all_passps):
    trues = {}
    for passp in all_passps:
        try:
            trues[is_valid(passp)] += 1
        except KeyError:
            trues[is_valid(passp)] = 1
    return trues

passps = [{'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}, {'iyr': '2013', 'ecl': 'amb', 'cid': '350', 'eyr': '2023', 'pid': '028048884', 'hcl': '#cfa07d', 'byr': '1929'}, {'hcl': '#ae17e1', 'iyr': '2013', 'eyr': '2024', 'ecl': 'brn', 'pid': '760753108', 'byr': '1931', 'hgt': '179cm'}, {'hcl': '#cfa07d', 'eyr': '2025', 'pid': '166559648', 'iyr': '2011', 'ecl': 'brn', 'hgt': '59in'}]


assert is_valid(passps[0])
assert not is_valid(passps[1])
assert is_valid(passps[2])
assert not is_valid(passps[3])

with open("04_input.txt", "r") as f:
    all_passps = all_pass(f)
print(count_valid(all_passps)) # 230
"""


"""
Your puzzle answer was 230.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
"""

t_invalid = [
    {"eyr":"1972", "cid":"100", "hcl":"#18171d", "ecl":"amb", "hgt":"170", "pid":"186cm", "iyr":"2018", "byr":"1926"},
    {"iyr": "2019", "hcl": "#602927", "eyr": "1967", "hgt": "170cm", "ecl": "grn ", "pid": "012533040", "byr": "1946"},
    {"hcl": "dab227", "iyr": "2012", "ecl": "brn", "hgt": "182cm", "pid": "021572410", "eyr": "2020", "byr": "1992", "cid": "277"},
    {"hgt": "59cm", "ecl": "zzz", "eyr": "2038", "hcl": "74454a", "iyr": "2023", "pid": "3556412378", "byr": "2007"}
]

t_valid = [
    {'pid': '087499704', 'hgt': '74in', 'ecl': 'grn', 'iyr': '2012', 'eyr': '2030', 'byr': '1980', 'hcl': '#623a2f'},
    {'eyr': '2029', 'ecl': 'blu', 'cid': '129', 'byr': '1989', 'iyr': '2014', 'pid': '896056539', 'hcl': '#a97842', 'hgt': '165cm'},
    {'hcl': '#888785', 'hgt': '164cm', 'byr': '2001', 'iyr': '2015', 'cid': '88', 'pid': '545766238', 'ecl': 'hzl', 'eyr': '2022'},
    {'iyr': '2010', 'hgt': '158cm', 'hcl': '#b6652a', 'ecl': 'blu', 'byr': '1944', 'eyr': '2021', 'pid': '093154719'},
]

def is_byr(passp):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    i = passp.get("byr", False)
    try:
        i = int(i)
        if 1920 <= i <= 2002:
            return True
    except:
        return False


def is_iyr(passp):
    #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    i = passp.get("iyr", False)
    try:
        i = int(i)
        if 2010 <= i <= 2020:
            return True
    except:
        return False


def is_eyr(passp):
    #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    i = passp.get("eyr", False)
    try:
        i = int(i)
        if 2020 <= i <= 2030:
            return True
    except:
        return False


def is_hgt(passp):
    #hgt (Height) - a number followed by either cm or in:
    #If cm, the number must be at least 150 and at most 193.
    #If in, the number must be at least 59 and at most 76.
    i = passp.get("hgt", False)
    if i and i.endswith("cm"):
        i = int(i[:-2])
        if 150 <= i <= 190:
            return True
    elif i and i.endswith("in"):
        i = int(i[:-2])
        if 59 <= i <= 76:
            return True


def is_hcl(passp):
    #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    i = passp.get("hcl", False)
    ii = passp.get("hcl", False)
    if i and i.startswith("#"):
        i = len(i[1:])
        if i == 6:
            return True


def is_ecl(passp):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    i = passp.get("ecl", False)
    musts = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if i and (i in musts):
        return True


def is_pid(passp):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    i = passp.get("pid", False)
    if i and len(i) == 9:
        return True


def is_valid2(passp):
    i = passp.get("ecl", False)
    if i == "grn ":
        passp["ecl"] = "grn"

    byr = is_byr(passp)
    iyr = is_iyr(passp)
    eyr = is_eyr(passp)
    hgt = is_hgt(passp)
    hcl = is_hcl(passp)
    ecl = is_ecl(passp)
    pid = is_pid(passp)

    musts = [byr, iyr, eyr, hgt, hcl, ecl, pid]
    count = 0
    
    for a in (x for x in musts if not x):
        count+=1
    
    if count == 1:
        print(passp, musts)

    if all(x for x in musts):
        return True
    else:
        return False


for passp in t_invalid:
    assert not is_valid2(passp)

for passp in t_valid:
    assert is_valid2(passp)


def count_valid2():
    with open("04_input.txt", "r") as f:
        all_passps = all_pass(f)

    trues = {}
    for passp in all_passps:
        try:
            trues[is_valid2(passp)] += 1
        except KeyError:
            trues[is_valid2(passp)] = 1
    return trues


class Validator:
    def __init__(self, passport):
        self.passport = passport

    def check_field_count(self):
        return len(self.passport) == 8 or (len(self.passport) == 7 and 'cid' not in self.passport)

    def check_year(self, key, start, end):
        return len(self.passport[key]) == 4 and int(self.passport[key]) >= start and int(self.passport[key]) <= end

    def check_byr(self):
        return self.check_year('byr', 1920, 2002)

    def check_iyr(self):
        return self.check_year('iyr', 2010, 2020)

    def check_eyr(self):
        return self.check_year('eyr', 2020, 2030)

    def check_hcl(self):
        return self.passport['hcl'][0] == "#" and self.passport['hcl'][1:].isalnum()

    def check_ecl(self):
        return self.passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def check_pid(self):
        return len(self.passport['pid']) == 9

    def check_hgt(self):
        if self.passport['hgt'][-2:] == "cm":
            return int(self.passport['hgt'][:-2]) >= 150 and int(self.passport['hgt'][:-2]) <= 193
        elif self.passport['hgt'][-2:] == "in":
            return int(self.passport['hgt'][:-2]) >= 59 and int(self.passport['hgt'][:-2]) <= 76

    def is_valid(self):
        return (self.check_field_count() and self.check_byr() and self.check_iyr() and self.check_eyr() 
            and self.check_hcl() and self.check_ecl() and self.check_pid() and self.check_hgt())


def get_passports(inp):
    passports = []
    passport = {}
    for line in inp:
        if line != "\n":
            line = line.rstrip().split(" ")
            line = [field.split(":") for field in line]
            for field in line:
                passport[field[0]] = field[1]
        else:
            passports.append(passport)
            passport = {}
    passports.append(passport)
    return passports


with open('04_input.txt') as inp:
    passports = get_passports(inp)
    validators = [Validator(passport) for passport in passports]
    part_1_count = 0
    part_2_count = 0
    for validator in validators:
        if validator.check_field_count(): 
            part_1_count += 1
        if validator.is_valid(): 
            part_2_count += 1                        

    print(part_1_count) 
    print(part_2_count) 


print(count_valid2()) # 230