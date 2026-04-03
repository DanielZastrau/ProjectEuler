"""https://projecteuler.net/problem=700"""

from time import time, sleep
from Package import prime
from Constants import primes_up_to_100Million

class circle:
    
    def __init__(self, length, step_length, point):
        self.length = length
        self.step_length = step_length
        self.point = point
        self.min = length
        self.overflow = False

    def step(self):
        self.point = (self.point + self.step_length)

        if self.point > self.length:
            self.point = self.point - self.length
            self.overflow = True

        elif self.point < 0:
            self.point = self.length + self.point
            self.overflow = True

    def update(self, shift):
        self.length = circle.min
        self.step_length = shift
        self.min = self.point
        self.overflow = False
        print('checkpoint 1')


if __name__=="__main__":
    t = time()

    n1 = 1504170715041707
    n2 = 4503599627370517

    circle = circle(n2, n1, 0)

    s = 0
    while circle.point != 1:
        circle.step()
        print('point', circle.point)
        if circle.overflow and circle.point < circle.min:
            shift_ = circle.point - circle.min
            s += circle.point
            
            print('min', circle.min)
            circle.update(shift=shift_)

        elif circle.point < circle.min:
            circle.min = circle.point

            s += circle.min
    print(s)

    print(time() - t)