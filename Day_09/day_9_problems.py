import sys
import time
from os import system

"""
--- Day 9: Encoding Error ---
With your neighbor happily enjoying their video game, you turn your attention
to an open data port on the little screen in the seat in front of you.

Though the port is non-standard, you manage to connect it to your computer
through the clever use of several paperclips. Upon connection, the port
outputs a series of numbers (your puzzle input).

The data appears to be encrypted with the eXchange-Masking Addition System
(XMAS) which, conveniently for you, is an old cypher with an important
weakness.

XMAS starts by transmitting a preamble of 25 numbers. After that, each number
you receive should be the sum of any two of the 25 immediately previous
numbers. The two numbers will have different values, and there might be more
than one such pair.

For example, suppose your preamble consists of the numbers 1 through 25 in a
random order. To be valid, the next number must be the sum of two of those
numbers:

    26 would be a valid next number, as it could be 1 plus 25 (or many other
    pairs, like 2 and 24).
    49 would be a valid next number, as it is the sum of 24 and 25.
    100 would not be valid; no two of the previous 25 numbers sum to 100.
    50 would also not be valid; although 25 appears in the previous 25 numbers,
    the two numbers in the pair must be different.

Suppose the 26th number is 45, and the first number (no longer an option, as
it is more than 25 numbers ago) was 20. Now, for the next number to be valid,
there needs to be some pair of numbers among 1-19, 21-25, or 45 that add up to
it:

    26 would still be a valid next number, as 1 and 25 are still within the
    previous 25 numbers.
    65 would not be valid, as no two of the available numbers sum to it.
    64 and 66 would both be valid, as they are the result of 19+45 and 21+45
    respectively.

Here is a larger example which only considers the previous 5 numbers (and has
a preamble of length 5):

    35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576

In this example, after the 5-number preamble, almost every number is the sum
of two of the previous 5 numbers; the only number that does not follow this
rule is 127.

The first step of attacking the weakness in the XMAS data is to find the first
number in the list (after the preamble) which is not the sum of two of the 25
numbers before it. What is the first number that does not have this property?

* 400480901
"""


"""
--- Part Two ---
The final step in breaking the XMAS encryption relies on the invalid number
you just found: you must find a contiguous set of at least two numbers in your
list which sum to the invalid number from step 1.

Again consider the above example:

    35
    20
    15
    25
    47
    40
    62
    55
    65
    95
    102
    117
    150
    182
    127
    219
    299
    277
    309
    576

In this list, adding up all of the numbers from 15 through 40 produces the
invalid number from step 1, 127. (Of course, the contiguous set of numbers in
your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number
in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?

* 67587168
"""


GREEN = "\033[0;42;30;1m"
RED = "\033[0;31;40m"
BLUE = "\033[0;37;44;1m"
YELLOW = "\033[0;30;43;1m"

END = "\033[0m"
START = "\033[F"
UP = "\033[A"
HIDE = "\033[8m"

PRINT = True


def clear():
    _ = system('cls')


def print_window_search(numbers, j, i, min_, max_, target):
    if i <= 0 or not PRINT: return
    sys.stdout.write(f"{START}{UP*80}")
    srt = ''.join(f"{RED } {x:<10}" for x in numbers[0:j])
    mid = ''.join(f"{BLUE} {x:<10}" if x == min_ else f"{BLUE} {x:<10}" if x == max_ else f"{GREEN} {x:<10}"for x in numbers[j:i])
    end = ''.join(f"{YELLOW } {x:<10}" if x == target else f"{RED } {x:<10}" for x in numbers[i:637])
    r = f"{srt}{mid}{end}{END}\n"
    sys.stdout.write(f"{r}\nTarget: {YELLOW}{target:9}{END} Total: {GREEN}{sum(numbers[j:i+1]):<10}{END} Answer: {BLUE}{(min_ + max_):<10}{END} Min: {BLUE}{min_:<10}{END} Max: {BLUE}{max_:<10}{END} Queue Length: {GREEN}{(i-j):<10}{END}\n")


def print_two_sums_search(numbers, j, i, a_, b_, target, valid):
    if not PRINT: return
    sys.stdout.write(f"{HIDE}{START}{UP*80}")
    srt = ''.join(f"{RED } {x:<10}" for x in numbers[0:j])
    mid = ''.join(f"{BLUE} {x:<10}" if x == a_ else f"{BLUE} {x:<10}" if x == b_ else f"{GREEN} {x:<10}"for x in numbers[j:i])+f"{YELLOW } {numbers[i]:<10}"
    end = ''.join(f"{RED } {x:<10}" for x in numbers[i+1:637])
    r = f"{srt}{mid}{end}{END}\n"
    sys.stdout.write(f"{r}\nTarget: {YELLOW}{target:<10}{END} Total: {GREEN if a_+b_!=target else YELLOW}{(a_ + b_):<10}{END} Answer: {BLUE}{target if valid else '--':<10}{END} a: {BLUE}{a_:<10}{END} b: {BLUE}{b_:<10}{END}{HIDE}\n")


def format_data(data):
    return [int(x.strip()) for x in data.readlines()]


def find_value(numbers, preamble_length):
    p_index = 0
    while p_index + preamble_length < len(numbers):
        t_index = p_index + preamble_length
        target = numbers[t_index]
        valid = False
        for a_index in range(p_index, t_index):
            if valid:
                break
            a = numbers[a_index]
            for b_index in range(a_index, t_index):
                b = numbers[b_index]
                if b % 10 == 0 and p_index > 0:
                    print_two_sums_search(numbers, p_index, t_index, a, b, target, valid)
                if b >= target:
                    continue
                if a + b == target:
                    valid = True
                    break
        if not valid:
            print_two_sums_search(numbers, p_index, t_index, 0, 0, target, True)
            return target
        p_index += 1


def find_contiguous_set(numbers, target):
    i = j = 0
    s_total = 0
    while i < len(numbers)-1:
        print_window_search(numbers, j, i, min(numbers[j:i+1]), max(numbers[j:i+1]), target)
        s_total += numbers[i]
        if s_total == target:
            return min(numbers[j:i+1]) + max(numbers[j:i+1])
        while (s_total + numbers[i+1]) > target:
            print_window_search(numbers, j, i, min(numbers[j:i+1]), max(numbers[j:i+1]), target)
            s_total -= numbers[j]
            j += 1
        i += 1


if __name__ == "__main__":
    with open("D:/PythonFiles/AdventOfCode_2020/Day_09/input.txt", "r") as in_file:
        numbers = format_data(in_file)
        target = find_value(numbers, 25)
        weakness = find_contiguous_set(numbers, target)
        print(f"Part 1: {target}")
        print(f"Part 2: {weakness}")
        print(END)
