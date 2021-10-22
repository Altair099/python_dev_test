class Calculator:
    def __init__(self):
        self.acc = 0

    def add(self, num):
        self.acc += num

    def sub(self, num):
        self.acc -= num

    def mul(self, num):
        self.acc *= num

    def div(self, num):
        self.acc /= num

    def clr(self):
        self.acc = 0

    def res(self):
        return self.acc


c = Calculator()
c.sub(10)
assert c.res() == -10
c.add(12)
assert c.res() == 2
c.add(4)
assert c.res() == 6
c.mul(2)
assert c.res() == 12
c.div(4)
assert c.res() == 3
c.clr()
assert c.res() == 0