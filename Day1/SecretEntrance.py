f = open("custom_input.txt")
lines: list[str] = f.readlines()

class Dial:
    def __init__(self, position: int):
        self.position: int = position
        self.number_of_zeros: int = 0

    def dial_change(self, direction: str, change: int):
        wraps: int = 0
        if direction == "L":
            difference: int = self.position - change
            if self.position == 0:
                wraps = change // 100
            else:
                wraps = (change - self.position + 99) // 100
            self.position = (difference % 100)
            self.number_of_zeros += wraps

        if direction == "R":
            difference: int = self.position + change
            wraps = (self.position + change) // 100
            self.position = (difference % 100)
            self.number_of_zeros += wraps

        if wraps == 0 and self.position == 0:
            self.number_of_zeros += 1

dial = Dial(50)

for line in lines:
    dial.dial_change(line[0], int(line[1:]))

print(dial.number_of_zeros)

f.close()