# Python program to check if the given path for a robot is circular
# or not

# This function returns true if the given path is circular,
# else false
def moved_circle(move):
    x = 0
    y = 0

    # Traverse the path given for robot
    for i in xrange(len(path)):

        move = path[i]
        # If move is left or right, then change direction
        if move == 'R':
            dir = (dir + 1) % 4
        elif move == 'L':
            dir = (4 + dir - 1) % 4

            # If move is Go, then change x or y according to
            # current direction
        else:
            if dir == N:
                y += 1
            elif dir == E:
                x += 1
            elif dir == S:
                y -= 1
            else:
                x -= 1

    return (x == 0 and y == 0)

# Driver program
path = 'GLGLGLG'
if isCircular(path):
	print('Given sequence of moves is circular')
else:
	print('Given sequence of moves is NOT circular')


