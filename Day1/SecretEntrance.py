f = open("test_input.txt")
lines: list[str] = f.readlines()

class Dial:
    def __init__(self, position: int):
        self.position: int = position
        self.number_of_zeros: int = 0

    def dial_change(self, direction: str, change: int):
            if direction == "L":
                difference: int = self.position - change
                if difference < 0:
                    self.position = (difference % 100)
                else:
                    self.position = difference

            if direction == "R":
                difference: int = self.position + change
                if difference > 99:
                    self.position = (difference % 100)
                else:
                    self.position = difference

            if self.position == 0:
                self.number_of_zeros += 1

dial = Dial(50)

for line in lines:
    dial.dial_change(line[0], int(line[1:]))

print(dial.number_of_zeros)

f.close()