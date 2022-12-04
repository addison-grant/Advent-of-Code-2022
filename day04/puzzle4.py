#!//usr/local/bin/python3.10

from typing import Tuple

class IntegerRange():
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __str__(self):
        return f"[{self.a}, {self.b}]"

    def intersection(self, ir: "IntegerRange") -> "IntegerRange":
        if self.b < ir.a or self.a > ir.b:
            return None
        return IntegerRange(max(self.a, ir.a), min(self.b, ir.b))
    
    def contains(self, ir: "IntegerRange") -> bool:
        if self.a <= ir.a  and ir.b <= self.b:
            return True
        return False

def parseInput(line: str) -> Tuple[IntegerRange]:
    l = line.split(",")
    left = l[0]
    right = l[1]
    l_left = left.split("-")
    r_left = right.split("-")
    ir1 = IntegerRange(int(l_left[0]), int(l_left[1]))
    ir2 = IntegerRange(int(r_left[0]), int(r_left[1]))
    return (ir1, ir2)


def main():
    with open("input4.in.txt") as f:
        count_containing = 0
        count_intersecting = 0
        for line in f:
            ir1, ir2 = parseInput(line)
            if ir1.contains(ir2) or ir2.contains(ir1):
                count_containing += 1
            if ir1.intersection(ir2) != None:
                count_intersecting += 1
    print(f"Containing: {count_containing}")
    print(f"Intersecting: {count_intersecting}")

if __name__ == "__main__":
    main()


def tests() -> None:
    ir1 = IntegerRange(1,4)
    ir2 = IntegerRange(3,6)
    print(ir1.intersection(ir2))
    print(ir1.contains(ir2))

    ir3 = IntegerRange(1,4)
    ir4 = IntegerRange(7,9)
    print(ir3.intersection(ir4))
    print(ir3.contains(ir4))

    ir5 = IntegerRange(1,4)
    ir6 = IntegerRange(2,4)
    print(ir5.intersection(ir6))
    print(ir5.contains(ir6))
