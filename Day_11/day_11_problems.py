from os import system

"""
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey
is a ferry that goes directly to the tropical island where you can finally
start your vacation. As you reach the waiting area to board the ferry, you
realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the
waiting area, you're pretty sure you can predict the best place to sit. You
make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an
empty seat (L), or an occupied seat (#). For example, the initial seat layout
might look like this:

    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL

Now, you just need to model the people who will be arriving shortly.
Fortunately, people are entirely predictable and always follow a simple set of
rules. All decisions are based on the number of occupied seats adjacent to a
given seat (one of the eight positions immediately up, down, left, right, or
diagonal from the seat). The following rules are applied to every seat
simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the
seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also
occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes
occupied:

    #.##.##.##
    #######.##
    #.#.#..#..
    ####.##.##
    #.##.##.##
    #.#####.##
    ..#.#.....
    ##########
    #.######.#
    #.#####.##

After a second round, the seats with four or more occupied adjacent seats
become empty again:

    #.LL.L#.##
    #LLLLLL.L#
    L.L.L..L..
    #LLL.LL.L#
    #.LL.LL.LL
    #.LLLL#.##
    ..L.L.....
    #LLLLLLLL#
    #.LLLLLL.L
    #.#LLLL.##

This process continues for three more rounds:

    #.##.L#.##
    #L###LL.L#
    L.#.#..#..
    #L##.##.L#
    #.##.LL.LL
    #.###L#.##
    ..#.#.....
    #L######L#
    #.LL###L.L
    #.#L###.##

    #.#L.L#.##
    #LLL#LL.L#
    L.L.L..#..
    #LLL.##.L#
    #.LL.LL.LL
    #.LL#L#.##
    ..L.L.....
    #L#LLLL#L#
    #.LLLLLL.L
    #.#L#L#.##

    #.#L.L#.##
    #LLL#LL.L#
    L.#.L..#..
    #L##.##.L#
    #.#L.LL.LL
    #.#L#L#.##
    ..L.L.....
    #L#L##L#L#
    #.LLLLLL.L
    #.#L#L#.##

At this point, something interesting happens: the chaos stabilizes and further
applications of these rules cause no seats to change state! Once people stop
moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no
seats change state. How many seats end up occupied?

* 2354
"""


"""
--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just
care about adjacent seats - they care about the first seat they can see in
each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats,
consider the first seat in each of those eight directions. For example, the
empty seat below would see eight occupied seats:

    .......#.
    ...#.....
    .#.......
    .........
    ..#L....#
    ....#....
    .........
    #........
    ...#.....

The leftmost empty seat below would only see one empty seat, but cannot see
any of the occupied ones:

    .............
    .L.L.#.#.#.#.
    .............

The empty seat below would see no occupied seats:

    .##.##.
    #.#.#.#
    ##...##
    ...L...
    ##...##
    #.#.#.#
    .##.##.

Also, people seem to be more tolerant than you expected: it now takes five or
more visible occupied seats for an occupied seat to become empty (rather than
four or more from the previous rules). The other rules still apply: empty
seats that see no occupied seats become occupied, seats matching no rule
don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating
area to shift around as follows:

    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL

    #.##.##.##
    #######.##
    #.#.#..#..
    ####.##.##
    #.##.##.##
    #.#####.##
    ..#.#.....
    ##########
    #.######.#
    #.#####.##

    #.LL.LL.L#
    #LLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLL#
    #.LLLLLL.L
    #.LLLLL.L#

    #.L#.##.L#
    #L#####.LL
    L.#.#..#..
    ##L#.##.##
    #.##.#L.##
    #.#####.#L
    ..#.#.....
    LLL####LL#
    #.L#####.L
    #.L####.L#

    #.L#.L#.L#
    #LLLLLL.LL
    L.L.L..#..
    ##LL.LL.L#
    L.LL.LL.L#
    #.LLLLL.LL
    ..L.L.....
    LLLLLLLLL#
    #.LLLLL#.L
    #.L#LL#.L#

    #.L#.L#.L#
    #LLLLLL.LL
    L.L.L..#..
    ##L#.#L.L#
    L.L#.#L.L#
    #.L####.LL
    ..#.#.....
    LLL###LLL#
    #.LLLLL#.L
    #.L#LL#.L#

    #.L#.L#.L#
    #LLLLLL.LL
    L.L.L..#..
    ##L#.#L.L#
    L.L#.LL.L#
    #.LLLL#.LL
    ..#.L.....
    LLL###LLL#
    #.LLLLL#.L
    #.L#LL#.L#

Again, at this point, people stop shifting around and the seating area reaches
equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats
becoming empty, once equilibrium is reached, how many seats end up occupied?

Your puzzle answer was 2072.
"""


def check_north(previous_cycle, rows, cols,  r, c):
    if r-1 >= 0:
        if previous_cycle[r-1][c] == '.':
            return check_north(previous_cycle, rows, cols, r-1, c)
        elif previous_cycle[r-1][c] == "#":
            return 1
    return 0


def check_south(previous_cycle, rows, cols,  r, c):
    if r+1 < rows:
        if previous_cycle[r+1][c] == '.':
            return check_south(previous_cycle, rows, cols, r+1, c)
        elif previous_cycle[r+1][c] == "#":
            return 1
    return 0


def check_left(previous_cycle, rows, cols,  r, c):
    if c-1 >= 0:
        if previous_cycle[r][c-1] == '.':
            return check_left(previous_cycle, rows, cols, r, c-1)
        elif previous_cycle[r][c-1] == "#":
            return 1
    return 0


def check_right(previous_cycle, rows, cols,  r, c):
    if c+1 < cols:
        if previous_cycle[r][c+1] == '.':
            return check_right(previous_cycle, rows, cols, r, c+1)
        elif previous_cycle[r][c+1] == "#":
            return 1
    return 0


def check_l_north(previous_cycle, rows, cols,  r, c):
    if r-1 >= 0 and c-1 >= 0:
        if previous_cycle[r-1][c-1] == '.':
            return check_l_north(previous_cycle, rows, cols, r-1, c-1)
        elif previous_cycle[r-1][c-1] == "#":
            return 1
    return 0


def check_r_north(previous_cycle, rows, cols,  r, c):
    if r-1 >= 0 and c+1 < cols:
        if previous_cycle[r-1][c+1] == '.':
            return check_r_north(previous_cycle, rows, cols, r-1, c+1)
        elif previous_cycle[r-1][c+1] == "#":
            return 1

    return 0


def check_l_south(previous_cycle, rows, cols,  r, c):
    if r+1 < rows and c-1 >= 0:
        if previous_cycle[r+1][c-1] == '.':
            return check_l_south(previous_cycle, rows, cols, r+1, c-1)
        elif previous_cycle[r+1][c-1] == "#":
            return 1
    return 0


def check_r_south(previous_cycle, rows, cols,  r, c):
    if r+1 < rows and c+1 < cols:
        if previous_cycle[r+1][c+1] == '.':
            return check_r_south(previous_cycle, rows, cols, r+1, c+1)
        elif previous_cycle[r+1][c+1] == "#":
            return 1
    return 0


directions = {
    (-1, 0): check_north,
    (1, 0): check_south,
    (0, -1): check_left,
    (0, +1): check_right,
    (-1, -1): check_l_north,
    (-1, 1): check_r_north,
    (1, -1): check_l_south,
    (1, 1): check_r_south,
}


def clear():
    _ = system('cls')


STATS = {
    'intial_occupied': 0,
    'occupied': 0,
    'moved': 0,
    'Cycles': 0,
    'all_empty': False,
    'all_occupied': False,
    'cycle_occupied': 1,
    'cycle_moved': 1,
    'total_occupied': 0
    }


def format_data(data):
    current_cycle_data = [[y for y in x.strip()] for x in data.readlines()]
    rows = len(current_cycle_data)
    columns = len(current_cycle_data[0])

    for row in range(0, rows):
        for col in range(0, columns):
            if current_cycle_data[row][col] == '#':
                STATS['initial_population'] += 1

    return current_cycle_data, rows, columns


def next_life_cycle_iteration(previous_cycle, current_cycle):
    STATS['all_empty'] = True
    STATS['all_occupied'] = True
    STATS['cycle_occupied'] = 0
    STATS['cycle_moved'] = 0
    STATS['total_occupied'] = 0

    rows = len(previous_cycle)
    columns = len(previous_cycle[0])

    for row in range(0, rows):
        for col in range(0, columns):
            live_neighbors = count_neighbors(previous_cycle, row, col)
            check_seat_rules(previous_cycle, current_cycle, row, col, live_neighbors)

    STATS['moved'] += STATS['cycle_moved']
    STATS['occupied'] += STATS['cycle_occupied']
    save_previous_cycle_iteration(current_cycle, previous_cycle)
    return


def count_neighbors(previous_cycle, r, c):
    occupied = '#'
    wrap_around = False

    rows = len(previous_cycle)
    columns = len(previous_cycle[0])

    total_neighbors = 0
    for row in range((r - 1), (r + 2)):
        for col in range((c - 1), (c + 2)):
            if row != r or col != c:  # Dont count yourself as a neighbor.
                if row < rows and row >= 0 and col < columns and col >= 0:
                    if previous_cycle[row][col] == occupied:
                        total_neighbors += 1
                    elif previous_cycle[row][col] == '.':
                        total_neighbors += directions[(row - r, col - c)](previous_cycle, rows, columns, row, col)

    return total_neighbors


def check_seat_rules(previous_cycle, current_cycle, row, column, occupied_neighbors):
    """
        If a seat is empty (L) and there are no occupied seats adjacent to it,
        the seat becomes occupied.
        If a seat is occupied (#) and four or more seats adjacent to it are
        also occupied, the seat becomes empty.
        Otherwise, the seat's state does not change.
    """

    empty_seat = 'L'
    occupied = '#'

    # rules for occupied seats
    if previous_cycle[row][column] == occupied:
        if occupied_neighbors >= 5:
            current_cycle[row][column] = empty_seat
            STATS['all_occupied'] = False
            STATS['cycle_moved'] += 1
        else:
            current_cycle[row][column] = occupied
            STATS['total_occupied'] += 1
            STATS['cycle_occupied'] += 1
            STATS['all_empty'] = False
    # rules for empty seats
    elif previous_cycle[row][column] == empty_seat:
        if occupied_neighbors == 0:
            current_cycle[row][column] = occupied
            STATS['total_occupied'] += 1
            STATS['all_empty'] = False
            STATS['all_occupied'] = False
            STATS['cycle_occupied'] += 1
        else:
            current_cycle[row][column] = empty_seat
    else:
        current_cycle[row][column] = '.'
    return


def save_previous_cycle_iteration(from_board, to_board):
    rows = len(from_board)
    columns = len(from_board[0])

    for row in range(0, rows):
        for col in range(0, columns):
            to_board[row][col] = from_board[row][col]
    return


def all_empty(current_cycle_data, current_loop):
    # format_and_print_output(current_cycle_data)
    print("\n\tNoone left after: {} iterations".format(current_loop))


def noone_moved(current_cycle_data, current_loop):
    # format_and_print_output(current_cycle_data)
    print("\n\tSimulation is stable after: {} iterations".format(current_loop))


def format_and_print_output(board):
    rows = len(board)
    columns = len(board[0])

    output = ''
    for row in range(0, rows):
        output += ' |\t'
        for col in range(0, columns):
            output += '{}'.format(board[row][col])
        if row == 1:
            output += '\t|  --------------\n'
        elif row == 2:
            output += '\t|  New occupied: {}\n'.format(STATS['cycle_occupied'])
        elif row == 4:
            output += '\t|  New moved: {}\n'.format(STATS['cycle_moved'])
        elif row == 5:
            output += '\t|  --------------\n'
        else:
            output += '\t|\n'
    output += (f"Total occupied {STATS['total_occupied']}\n")
    print(output)
    return


if __name__ == "__main__":
    with open("Day_11/input.txt", "r") as in_file:
        current_cycle_data, rows, columns = format_data(in_file)
        current_loop = 0
        previous_cycle_data = [['.' for i in range(columns)] for j in range(rows)]
        save_previous_cycle_iteration(current_cycle_data, previous_cycle_data)

        # Begin simulation loop
        while STATS['cycle_occupied'] + STATS['cycle_moved'] > 0:
            if STATS['all_empty'] is True:
                all_empty(current_cycle_data, current_loop)
                break
            if STATS['all_occupied'] is True:
                noone_moved(current_cycle_data, current_loop)
                break

            # clear()
            # format_and_print_output(current_cycle_data)

            next_life_cycle_iteration(previous_cycle_data, current_cycle_data)

            current_loop += 1
            STATS['Cycles'] = current_loop

        print(f"Total occupied {STATS['total_occupied']}\n")
