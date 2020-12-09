import sys
import time
from copy import deepcopy
from os import system

"""
--- Day 8: Handheld Halting ---
Your flight to the major airline hub reaches cruising altitude without
incident. While you consider checking the in-flight menu for one of those
drinks that come with a little umbrella, you are interrupted by the kid
sitting next to you.

Their handheld game console won't turn on! They ask if you can take a look.

You narrow the problem down to a strange infinite loop in the boot code (your
puzzle input) of the device. You should be able to fix it, but first you need
to be able to run the code in isolation.

The boot code is represented as a text file with one instruction per line of
text. Each instruction consists of an operation (acc, jmp, or nop) and an
argument (a signed number like +4 or -20).

    - acc increases or decreases a single global value called the accumulator
      by the value given in the argument. For example, acc +7 would increase
      the accumulator by 7. The accumulator starts at 0. After an acc
      instruction, the instruction immediately below it is executed next.
    - jmp jumps to a new instruction relative to itself. The next instruction
      to execute is found using the argument as an offset from the jmp
      instruction; for example, jmp +2 would skip the next instruction, jmp +1
      would continue to the instruction immediately below it, and jmp -20
      would cause the instruction 20 lines above to be executed next.
    - nop stands for No OPeration - it does nothing. The instruction
      immediately below it is executed next.

For example, consider the following program:

    nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6

These instructions are visited in this order:

    nop +0  | 1
    acc +1  | 2, 8(!)
    jmp +4  | 3
    acc +3  | 6
    jmp -3  | 7
    acc -99 |
    acc +1  | 4
    jmp -4  | 5
    acc +6  |

First, the nop +0 does nothing. Then, the accumulator is increased from 0 to 1
(acc +1) and jmp +4 sets the next instruction to the other acc +1 near the
bottom. After it increases the accumulator from 1 to 2, jmp -4 executes,
setting the next instruction to the only acc +3. It sets the accumulator to 5,
and jmp -3 causes the program to continue back at the first acc +1.

This is an infinite loop: with this sequence of jumps, the program will run
forever. The moment the program tries to run any instruction a second time,
you know it will never terminate.

Immediately before the program would run an instruction a second time, the
value in the accumulator is 5.

Run your copy of the boot code. Immediately before any instruction is executed
a second time, what value is in the accumulator?

* 1420
"""


"""
--- Part Two ---
After some careful analysis, you believe that exactly one instruction is
corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is
supposed to be a jmp. (No acc instructions were harmed in the corruption of
this boot code.)

The program is supposed to terminate by attempting to execute an instruction
immediately after the last instruction in the file. By changing exactly one
jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

    nop +0
    acc +1
    jmp +4
    acc +3
    jmp -3
    acc -99
    acc +1
    jmp -4
    acc +6

If you change the first instruction from nop +0 to jmp +0, it would create a
single-instruction infinite loop, never leaving that instruction. If you
change almost any of the jmp instructions, the program will still eventually
find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4),
the program terminates! The instructions are visited in this order:

    nop +0  | 1
    acc +1  | 2
    jmp +4  | 3
    acc +3  |
    jmp -3  |
    acc -99 |
    acc +1  | 4
    nop -4  | 5
    acc +6  | 6

After the last instruction (acc +6), the program terminates by attempting to
run the instruction below the last instruction in the file. With this change,
after the program terminates, the accumulator contains the value 8 (acc +1,
acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to
nop) or nop (to jmp). What is the value of the accumulator after the program
terminates?

* 1245
"""


def clear():
    _ = system('cls')


def format_data(data):
    return [[x[:3], int(x[3:])] for x in data.readlines()]


def try_swap_op(op):
    op[0] = 'jmp' if op[0] == 'nop' else 'nop' if op[0] == 'jmp' else 'acc'


class Computer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.accumulator = 0
        self.length = len(self.instructions)
        self.current_address = 0
        self.previous_addresses = []

        self.operations = {
            'acc': self.__do_acc__,
            'jmp': self.__do_jmp__,
            'nop': self.__do_nop__
        }

    def __update_steps__(self, amt):
        self.current_address += amt

    def __update_accumulator__(self, amt):
        self.accumulator += amt

    def __do_acc__(self, amount):
        self.__update_steps__(1)
        self.__update_accumulator__(amount)

    def __do_jmp__(self, amount):
        self.__update_steps__(amount)

    def __do_nop__(self, amount):
        self.__update_steps__(1)

    def __get_op__(self):
        return self.instructions[self.current_address][0]

    def __get_amt__(self):
        return self.instructions[self.current_address][1]

    def __execute__(self, op, amt):
        self.operations[op](amt)

    def __can_run__(self):
        return self.current_address < self.length

    def __has_visited__(self):
        return self.current_address in self.previous_addresses

    def __mark_visited__(self):
        self.previous_addresses.append(self.current_address)

    def __failed__(self):
        return -1, self.accumulator, self.current_address, self.accumulator

    def __passed__(self):
        return 0, self.accumulator, self.current_address, self.accumulator

    def __continue__(self):
        return 1, self.accumulator, self.current_address, self.accumulator

    def step(self):
        while self.__can_run__():
            self.__execute__(self.__get_op__(), self.__get_amt__())
            if self.__has_visited__():
                yield self.__failed__()
            self.__mark_visited__()
            yield self.__continue__()
        yield self.__passed__()

    def run(self):
        while self.__can_run__():
            self.__execute__(self.__get_op__(), self.__get_amt__())
            if self.__has_visited__():
                return self.__failed__()
            self.__mark_visited__()
        return self.__passed__()


def print_data(data, address, accumulated):
    GREEN = "\033[0;32;40m"
    YELLOW = "\033[0;33;40m"
    BLUE = "\033[0;34;40m"
    RED = "\033[0;31;40m"
    END = "\033[0m"
    START = "\033[F"
    UP = "\033[A"

    JMP = f"{BLUE}{'▲'} {END}"
    NOP = f"{RED}{'■'} {END}"
    ACC = f"{GREEN}{'⬤'} {END}"
    CURRENT = f"{YELLOW}{'   '}{END}"

    colors = {
        'jmp': BLUE,
        'nop': RED,
        'acc': GREEN
    }

    icons = {
        'jmp': JMP,
        'nop': NOP,
        'acc': ACC
    }

    sys.stdout.write(f"{START}{UP*13}")
    s = ''
    k = address-1
    for i in range(0, 600, 50):
        k = min(k+1, len(data)-1)
        if k+1 < len(data):
            s += f"{colors[data[k][0]]}{data[k][0]}{END}  "
            s += f"{data[k][1]:4} {YELLOW}│{END} "
        else:
            s += f"{'---  0000'} {YELLOW}│{END} "
        for j in range(i, i+50, 1):
            if j == address:
                s += f"{j:<3}"
            elif j < len(data):
                s += f"{icons[data[j][0]]} "
            else:
                s += f"{YELLOW}{'___'}{END}"
        if i == 0:
            s += f"{YELLOW}│{END} {accumulated:4}"
        else:
            s += f"{YELLOW}│{END}"
        s += "\n"
    s += f"Address: {address}\n"
    sys.stdout.write(s)
    sys.stdout.flush()


def part_1(instructions):
    computer = Computer(deepcopy(instructions))
    code, amt, a, ac = computer.run()
    return f"Part 1: {amt}"


def part_2(instructions):
    # 247 runs to completion
    for i in range(274, len(instructions)):
        d = deepcopy(instructions)
        try_swap_op(d[i])
        computer = Computer(d)
        for code, amt, address, accumulated in computer.step():
            print_data(d, address, accumulated)
            if code == -1:
                break
            if code == 0:
                return f"Part 2: {amt}"


if __name__ == "__main__":
    clear()
    with open("Day_08/input.txt", "r") as in_file:
        instructions = format_data(in_file)
        P1 = part_1(instructions)
        P2 = part_2(instructions)
        print(f"{P1}\n{P2}")
