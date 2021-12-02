from dataclasses import dataclass


@dataclass
class Command:
    type: str
    value: int

class Submarine:
    depth: int
    position: int

    def __init__(self, arg_depth, arg_pos):
        self.depth = arg_depth
        self.position = arg_pos

    def move(self, arg_cmd):
        if arg_cmd.type == "forward":
            self.position += arg_cmd.value
        elif arg_cmd.type == "down":
            self.depth += arg_cmd.value
        elif arg_cmd.type == "up":
            self.depth -= arg_cmd.value
        else:
            raise Exception('Command error')



if __name__ == '__main__':
    
    commands = []
    line_content = []
    with open('data/day2_data.txt') as file:
        for line in file:
            line_content = line.strip().split(' ')
            commands.append(Command(line_content[0], int(line_content[1])))

    MySumarine = Submarine(0, 0)

    for cmd in commands:
        MySumarine.move(cmd)
    
print("Pos: " + str(MySumarine.position))
print("Depth: " + str(MySumarine.depth))
print("Mul: " + str(MySumarine.position * MySumarine.depth))