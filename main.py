# The whole idea of algorithm is basing on 3 main steps:
# Placing first disk on second tower
# Then placing second disk on third tower
# And then replacing first disk from second tower to third
# Making a recursion algorithm with this three steps...


def move(number, start_pos, finish_pos):
    """
    Recursion algorithm
    :param number: the number of disks
    :param start_pos: the position of tower at the start
    :param finish_pos: the position of tower at the end
    """
    if number == 1:
        print("Move disk 1 from tower", start_pos, "to tower", finish_pos)
    else:
        temp = (6 - start_pos) - finish_pos  # temporary variable for counting
        move(number - 1, start_pos, temp)
        print("Move disk", number, "from tower", start_pos, "to tower", finish_pos)
        move(number - 1, temp, finish_pos)


number = int(input("Enter the number of disks:"))
move(number, 1, 3)
