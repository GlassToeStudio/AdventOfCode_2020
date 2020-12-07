from collections import OrderedDict

"""
--- Day 6= Custom Customs ---
As your flight approaches the regional airport where you'll switch to a much
larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you
need to do is identify the questions for which anyone in your group answers
"yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language
barrier and asks if you can help. For each of the people in their group, you
write down the questions for which they answer "yes", one per line.
For example=

    abcx
    abcy
    abcz

In this group, there are 6 questions to which anyone answered "yes"=
a, b, c, x, y, and z. (Duplicate answers to the same question don't count
extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've
collected answers from every group on the plane (your puzzle input). Each
group's answers are separated by a blank line, and within each group, each
person's answers are on a single line.
For example=

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

This list represents answers from five groups=

    The first group contains one person who answered "yes" to 3 questions=
    a, b, and c.
    The second group contains three people; combined, they answered "yes" to
    3 questions= a, b, and c.
    The third group contains two people; combined, they answered "yes" to
    3 questions= a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to
    only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question,
    b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes".
What is the sum of those counts?

* Part 1= 6583
"""


"""
--- Part Two ---
As you finish the last group's customs declaration, you notice that you
misread one word in the instructions=

You don't need to identify the questions to which anyone answered "yes"; you
need to identify the questions to which everyone answered "yes"!

Using the same example as above=

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

This list represents answers from five groups=

    In the first group, everyone (all 1 person) answered "yes" to 3 questions=
    a, b, and c.
    In the second group, there is no question to which everyone answered "yes".
    In the third group, everyone answered yes to only 1 question, a. Since some
    people did not answer "yes" to b or c, they don't count.
    In the fourth group, everyone answered yes to only 1 question, a.
    In the fifth group, everyone (all 1 person) answered "yes" to 1 question,
    b.

In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes".
What is the sum of those counts?

* Part 2= 3290
"""

colors = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m']
chars = ['█', '▓', '▒', '░']

ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def format_data_1(data):
    return [set(x.replace('\n', '')) for x in data.read().split('\n\n')]


def format_data_2(data):
    return [set(x.split()[0]).intersection(*x.split()) for x in data.read().split('\n\n')]


def print_graph(graph, total, text):
    scale = 3
    s = ''
    i = 0
    m = 0
    c = 0
    for bar in graph:
        m = max(m, graph[bar])
        s += f"{BOLD}{bar}{ENDC} │ {colors[i]}{chars[c] * int(graph[bar]/scale)}{ENDC} - {BOLD}{graph[bar]}{ENDC}\n"
        i = (i + 1)%len(colors)
        c = (c + 1)%len(chars)
    s += f"{UNDERLINE}{'░'*int(m/(2*scale))}{BOLD} Total : {total}{ENDC}_{'░'*int(m/(2*scale))}\n"
    s = f"{'░'*int(m/(2*scale))}______{BOLD}{UNDERLINE}{text}{ENDC}_____{'░'*int(m/(2*scale))}\n{s}"
    print(s)


if __name__ == "__main__":
    with open("Day_06/input.txt", "r") as in_file:
        print()
        groups = format_data_1(in_file)
        graph = {}
        sum = 0
        for group in groups:
            sum += len(group)
            for answer in group:
                if answer not in graph:
                    graph[answer] = 1
                else:
                    graph[answer] += 1
        print_graph(OrderedDict(sorted(graph.items())), sum, "Any")

    with open("Day_06/input.txt", "r") as in_file:
        print()
        groups = format_data_2(in_file)
        graph = {}
        sum = 0
        for group in groups:
            sum += len(group)
            for answer in group:
                if answer not in graph:
                    graph[answer] = 1
                else:
                    graph[answer] += 1
        print_graph(OrderedDict(sorted(graph.items())), sum, "All")
