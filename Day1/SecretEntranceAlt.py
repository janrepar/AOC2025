f = open("input.txt")
lines: list[str] = f.readlines()

class Dial:
    def __init__(self, position: int):
        self.position: int = position
        self.number_of_zeros: int = 0

    def dial_change(self, direction: str, change: int):
        start: int = self.position

        if direction == "R":
            self.number_of_zeros += (start + change) // 100
            self.position = (start + change) % 100
        elif direction == "L":
            if start == 0:
                self.number_of_zeros += change // 100
            elif change >= start:
                self.number_of_zeros += 1 + (change - start) // 100

            self.position = (start - change) % 100


dial = Dial(50)

for line in lines:
    dial.dial_change(line[0], int(line[1:]))

print(dial.number_of_zeros)

f.close()