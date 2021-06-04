import random


def find_pacman(map):
    pacman_x = -1
    pacman_y = -1

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == '@':
                pacman_x = x
                pacman_y = y

    return pacman_x, pacman_y

def move_pacman(map, next_pacman_x, next_pacman_y):
    pacman_x, pacman_y = find_pacman(map)

    # the place where the pacman was is now empty
    everything_to_the_left = map[pacman_x][0:pacman_y]
    everything_to_the_right = map[pacman_x][pacman_y+1:]
    map[pacman_x] = everything_to_the_left + "." + everything_to_the_right

    # the new place has the pacman
    everything_to_the_left = map[next_pacman_x][0:next_pacman_y]
    everything_to_the_right = map[next_pacman_x][next_pacman_y+1:]
    map[next_pacman_x] = everything_to_the_left + "@" + everything_to_the_right

# this function returns two booleans
# the first indicates whether the pressed key was a valid key
# the second indicates whether the pacman is still alive
# the third indicates whether next is pill
def play(map, key):
    next_x, next_y = next_position(map, key)
    # if it is a invalid key
    is_an_invalid_key = next_x == -1 and next_y == -1
    if is_an_invalid_key:
        return False, True,False

    # if it is not within borders
    if not within_borders(map, next_x, next_y):
        return False, True,False

    # if it is a wall
    if is_a_wall(map, next_x, next_y):
        return False, True,False


    if is_a_ghost(map, next_x, next_y):
        return True, False,False


    if is_a_pill(map, next_x, next_y):
        move_pacman(map, next_x, next_y)
        return True,True,True
    else:
        move_pacman(map, next_x, next_y)
        return True, True,False



def is_a_wall(map, next_x, next_y):
    is_a_wall = map[next_x][next_y] == '|' or map[next_x][next_y] == '-'
    return is_a_wall

def is_a_ghost(map, next_x, next_y):
    if map[next_x][next_y] == 'G' or map[next_x][next_y] == 'Q':
        return True

def is_a_pill(map, next_x, next_y):
    return map[next_x][next_y] == 'P'

def is_pacman(map, next_x, next_y):
    return map[next_x][next_y] == '@'

def is_nothing(map,next_x,next_y):
    return map[next_x][next_y] == '.'

def within_borders(map, next_x, next_y):
    number_of_rows = len(map)
    x_is_valid = 0 <= next_x < number_of_rows

    number_of_columns = len(map[0])
    y_is_valid = 0 <= next_y < number_of_columns

    return x_is_valid and y_is_valid

def total_pills(map):
    total = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'P':
                total = total + 1
    return total


def next_position(map, key):
    x, y = find_pacman(map)
    next_x = -1
    next_y = -1

    if key == 'left':
        next_x = x
        next_y = y - 1
    elif key == 'right':
        next_x = x
        next_y = y + 1
    elif key == 'up':
        next_x = x - 1
        next_y = y
    elif key == 'down':
        next_x = x + 1
        next_y = y
    return next_x,next_y

def find_ghosts(map):
    all=[]
    all_ghosts = []
    all_ghosts_pills =[]
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'G':
                all_ghosts.append([x,y])
                all.append([x,y])
            elif map[x][y] =='Q':
                all_ghosts_pills.append([x, y])
                all.append([x,y])
    return all ,all_ghosts ,all_ghosts_pills

def move_ghost(map,ghost_x,ghost_y,next_ghost_x,next_ghost_y):
    # move the ghost to the random position
    everything_to_the_left = map[ghost_x][0:ghost_y]
    everything_to_the_right = map[ghost_x][ghost_y + 1:]
    map[ghost_x] = everything_to_the_left + "." + everything_to_the_right

    # the new place has the pacman
    everything_to_the_left = map[next_ghost_x][0:next_ghost_y]
    everything_to_the_right = map[next_ghost_x][next_ghost_y + 1:]
    map[next_ghost_x] = everything_to_the_left + "G" + everything_to_the_right
def move_ghost_from_pill(map, ghost_x, ghost_y, next_ghost_x, next_ghost_y):
    # move the ghost to the random position
    everything_to_the_left = map[ghost_x][0:ghost_y]
    everything_to_the_right = map[ghost_x][ghost_y + 1:]
    map[ghost_x] = everything_to_the_left + "P" + everything_to_the_right

    # the new place has the pacman
    everything_to_the_left = map[next_ghost_x][0:next_ghost_y]
    everything_to_the_right = map[next_ghost_x][next_ghost_y + 1:]
    map[next_ghost_x] = everything_to_the_left + "G" + everything_to_the_right
def move_ghost_on_pill(map,ghost_x,ghost_y,next_ghost_x,next_ghost_y):
    # move the ghost to the random position
    everything_to_the_left = map[ghost_x][0:ghost_y]
    everything_to_the_right = map[ghost_x][ghost_y + 1:]
    map[ghost_x] = everything_to_the_left + "." + everything_to_the_right

    # the new place has the pacman
    everything_to_the_left = map[next_ghost_x][0:next_ghost_y]
    everything_to_the_right = map[next_ghost_x][next_ghost_y + 1:]
    map[next_ghost_x] = everything_to_the_left + "Q" + everything_to_the_right

def move_ghost_on_pill_from_pill(map,ghost_x, ghost_y, next_ghost_x, next_ghost_y):
    # move the ghost to the random position
    everything_to_the_left = map[ghost_x][0:ghost_y]
    everything_to_the_right = map[ghost_x][ghost_y + 1:]
    map[ghost_x] = everything_to_the_left + "P" + everything_to_the_right

    # the new place has the pacman
    everything_to_the_left = map[next_ghost_x][0:next_ghost_y]
    everything_to_the_right = map[next_ghost_x][next_ghost_y + 1:]
    map[next_ghost_x] = everything_to_the_left + "Q" + everything_to_the_right
def move_ghosts(map,level):
    all,all_ghosts ,all_ghosts_pills = find_ghosts(map)
    for ghost in all:
        ghost_x = ghost[0]
        ghost_y = ghost[1]

        possible_directions = [
            [ghost_x, ghost_y + 1],
            [ghost_x, ghost_y - 1],
            [ghost_x - 1, ghost_y],
            [ghost_x + 1, ghost_y]
            ]
        if level=="easy":
            # select a random possible movement
            # and get the x,y of the movement
            random_number = random.randint(0, 3)
            next_ghost_x = possible_directions[random_number][0]
            next_ghost_y = possible_directions[random_number][1]
            # checks before actually moving it!
        elif level=="normal":
            pacman_x, pacman_y = find_pacman(map)
            x_pacman_ghost ,y_pacman_ghost=pacman_x-ghost_x ,pacman_y-ghost_y
            if   x_pacman_ghost <  0and y_pacman_ghost   <0:
                if abs(x_pacman_ghost)>=abs(y_pacman_ghost):
                    next_ghost_x =ghost_x -1
                    next_ghost_y =ghost_y
                else:
                    next_ghost_y =ghost_y -1
                    next_ghost_x =ghost_x
            elif x_pacman_ghost >= 0and y_pacman_ghost >= 0:
                if abs(x_pacman_ghost) >= abs(y_pacman_ghost):
                    next_ghost_x = ghost_x +1
                    next_ghost_y = ghost_y
                else:
                    next_ghost_y = ghost_y +1
                    next_ghost_x = ghost_x
            elif x_pacman_ghost <  0and y_pacman_ghost >= 0:
                if abs(x_pacman_ghost) >= abs(y_pacman_ghost):
                    next_ghost_x = ghost_x -1
                    next_ghost_y = ghost_y
                else:
                    next_ghost_y = ghost_y +1
                    next_ghost_x = ghost_x
            elif x_pacman_ghost >= 0and y_pacman_ghost<  0:
                if abs(x_pacman_ghost) >= abs(y_pacman_ghost):
                    next_ghost_x = ghost_x +1
                    next_ghost_y = ghost_y
                else:
                    next_ghost_y = ghost_y -1
                    next_ghost_x = ghost_x
        elif level=="hard":
            pass
        if not within_borders(map, next_ghost_x, next_ghost_y):
            continue

        if is_a_wall(map, next_ghost_x, next_ghost_y):
            continue

        if is_a_ghost(map, next_ghost_x, next_ghost_y):
            continue
        if ghost in all_ghosts:
            if is_a_pill(map, next_ghost_x, next_ghost_y):
                move_ghost_on_pill(map,ghost_x, ghost_y, next_ghost_x, next_ghost_y)
                continue
            if is_pacman(map, next_ghost_x, next_ghost_y):
                return True

            move_ghost(map,ghost_x,ghost_y,next_ghost_x,next_ghost_y)

        elif ghost in all_ghosts_pills:
            if is_a_pill(map, next_ghost_x, next_ghost_y):
                move_ghost_on_pill_from_pill(map,ghost_x, ghost_y, next_ghost_x, next_ghost_y)
                continue
            if is_pacman(map, next_ghost_x, next_ghost_y):
                return True

            move_ghost_from_pill(map, ghost_x, ghost_y, next_ghost_x, next_ghost_y)

