# Advent Of Code 2020
Advent of Code 2020 https://adventofcode.com/2020

<details>
<summary><b>Day 1: Report Repair</b></summary>
<p>
Day 1 provides an expense report with which one must search through each entry and find the pair that total 2020. Then find the triplet that totals 2020.

```
1721
979
366
299
675
1456
```

### Part 1:
For every entry in the list, compare it with every other entry until once pair totals 2020. 

### Part 2:
Same as part 1 but check every triplet in the same manner as before.

Added in some early outs in case there was no chance of a solution for any particular pair. Additionally, the data was sorted in ascending order to speed up operations. 
</p>
</details>


<details>
<summary><b>Day 2: Password Philosophy</b></summary>
<p>
Day 2 provides a list of passwords along with some criteria for validity. Where you are given two numbers and one character. The numbers being the min and max occurrences for the given char in the respective password.

```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

### Part 1:
Parse the data to extract the min, max, and special char and the password. Check the occurrences of the char in the password and verify it is within the min and max allowed.

### Part 2:
The rules change such that the numbers are now indices of where the char can occur in the password, but it can only occur in one of the two indices to be valid. For a little extra challenge, the numbers are not 0 based as is typical in programming languages. Check each index for the char and return a valid result only if one occurs.

Added in a regex version as well as built-in methods to solve.
</p>
</details>


<details>
<summary><b>Day 3: Toboggan Trajectory</b></summary>
<p>
Day 3 provides a map of trees for a given region. This region repeats the tree pattern out to the right. Each '#' indicates a tree. One must find all trees hit based on a given trajectory (slope)

```
..##....... --->
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##..... ...>
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.# --->
```

### Part 1:
Given a slope of (3, 1) calculate the number of tees hit - points on the path with "#".

### Part 2:
Given a number of slopes,[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] calculate the trees hit for each slope and find the product of them all.

### Created a little gif to show part one in action
<p align="center">
<img src="https://github.com/GlassToeStudio/AdventOfCode_2020/blob/master/Day_03/AoC_day3_p1.gif" width="50%" height="50%"
</p>

</p>
</details>

<details>
<summary><b>Day 4: Passport Processing</b></summary>
<p>
Day 4 number of key:value pairs for a given set of passport data all separated by a blank line. One must parse the data and check that the required fields are present.

```
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
```
### Required felids (except cid)

```
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
```

### Part 1:
Break down the data in separate passports then break out each key:value pair of fields. Check that the required fields are present and count the total number of valid passports.

### Part 2:
Each field now required some data validation. Check each field against its respective criteria and find the total number of valid passports.

```
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeros.
cid (Country ID) - ignored, missing or not.
```
</p>
</details>


<details>
<summary><b>Day 5: Binary Boarding</b></summary>
<p>
Day 5 provides a list of instructions for calculating a row, column and seat id for a given line of input. The instructions state to perform somewhat of a binary search, in that one must continuously take either the upper or lower half of some range until a single value is left. Do this for the first 7 characters of the input, then again for the last 3 characters. The two values are then used to calculate a seat id. Once all seat ids are found, locate the seat id that is missing from the others. 

```py
BFFFBBFRRR

def get_seat_id(row, column):
    return row * 8 + column
```

### Part 1:
For every line of input, split out the first 7 and last 3 characters. Based on each value, take either the upper or lower half of a given range (128 and 8, respectively). Take these two values and calculate a seat id.

### Part 2:
For every seat id, find which one is missing from the total range of seat ids (128 * 8). However, not all seat ids are actually available, so to find the missing seat, find also that its neighbors (+1 and -1) are not missing. 

```py
if seat + 1 not in missing_seats and seat - 1 not in missing_seats:
``` 
</p>
</details>


<details>
<summary><b>Day 6: Custom Customs</b></summary>
<p>
Day 6 provides a list of groups of answers, each answer being a letter of the alphabet noting a answer of yes for one of 26 questions.

```
abc

a
b
c

ab
ac

a
a
a
a

b
```

### Part 1:
For every groups of answers, find ANY response of yes. (Union). 

### Part 2:
For every group of answers, find responses where ALL answered yes. (Intersection)


### Created some visuals of the data
#### Part 1
<p align="center">
<img src="https://github.com/GlassToeStudio/AdventOfCode_2020/blob/master/Day_06/day_6_part_1.PNG" width="100%" height="100%"
</p>

#### Part 2
<p align="center">
<img src="https://github.com/GlassToeStudio/AdventOfCode_2020/blob/master/Day_06/day_6_part_2.PNG" width="100%" height="100%"
</p>

</p>
</details>


<details>
<summary><b>Day 7: Handy Haversacks</b></summary>
<p>
Day 7

```
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
```

### Part 1:
 
### Part 2:


</p>
</details>


<details>
<summary><b>Day 8: Handheld Halting</b></summary>
<p>
Day 8 - our first VM

```
```

### Part 1:
For every groups of answers, find ANY response of yes. (Union). 

### Part 2:

### Visusal
<p align="center">
<img src="https://github.com/GlassToeStudio/AdventOfCode_2020/blob/master/Day_08/AoC_day8_vis.gif" width="100%" height="100%"
</p>

</p>
</details>


<details>
<summary><b>Day 9: Encoding Error</b></summary>
<p>
Day 9 - Window search

```
```

### Part 1:

### Part 2:

### Visusal
<p align="center">
<img src="https://github.com/GlassToeStudio/AdventOfCode_2020/blob/master/Day_09/AoC_day9_vis.gif" width="100%" height="100%"
</p>


</p>
</details>