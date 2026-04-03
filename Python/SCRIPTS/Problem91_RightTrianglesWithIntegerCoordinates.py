"""How many right triangles are there with integer coordinates with 0 <= x, y <= 50.
One of the corners is always the origin (0, 0)

with 0 <= x, y <= 2 the answer is 14

https://projecteuler.net/problem=91
"""

from icecream import ic
import time

class Point():

    def __init__(self, x: float, y: float) -> None:

        self.x = x
        self.y = y

    def __add__(self, other):

        x = self.x + other.x
        y = self.y + other.y

        return Point(x = x, y = y)

    def __mul__(self, scalar):
        return Point(x = scalar * self.x, y = scalar * self.y)
    __rmul__ = __mul__

    def __sub__(self, other):

        x = self.x - other.x
        y = self.y - other.y

        return Point(x = x, y = y)


    def __eq__(self, other) -> bool:

        if isinstance(other, tuple):

            if self.x == other[0] and self.y == other[1]:
                return True

        else:

            if self.x == other.x and self.y == other.y:
                return True

        return False


    def __repr__(self) -> str:
        return f'(x: {self.x}, y: {self.y})'


def rotations(p_one: Point) -> bool:

    clockwise_rotation = Point(x = p_one.y, y = p_one.x * -1)

    anticlockwise_rotation = Point(x = p_one.y * -1, y = p_one.x)

    return clockwise_rotation, anticlockwise_rotation


def main(grid_size: int = 2):

    origin = Point(0, 0)

    # build pairs of integers square by square, so that those nearest to the origin come first
    pairs_of_integers = []
    for u in range(1, grid_size + 2):
        for i in range(u-1, u):

            if i == 0:
                continue

            pairs_of_integers.append(Point(x = i, y = i))

            for ii in range(u-1):

                point_one = Point(x = i, y = ii)
                point_two = Point(x = ii, y = i)

                pairs_of_integers.append(point_one)
                pairs_of_integers.append(point_two)

    points_to_look_at = pairs_of_integers.copy()

    count = 0
    while points_to_look_at:

        original_vector = points_to_look_at[0]

        clockwise_rotation, anticlockwise_rotation = rotations(original_vector)

        # per extension of the original vector
        scalar_original_vector = 1
        while scalar_original_vector * original_vector in pairs_of_integers:    # here I could determine a for loop to get around the list checking

            points_to_look_at.remove(scalar_original_vector * original_vector)

            ## look at the extensions of the clockwise rotation
            scalar_clockwise_rotation = 1
            while True:

                x = scalar_original_vector * original_vector.x + scalar_clockwise_rotation * clockwise_rotation.x
                y = scalar_original_vector * original_vector.y + scalar_clockwise_rotation * clockwise_rotation.y

                point = Point(x, y)

                if point in pairs_of_integers:
                    ### increment the scalar
                    scalar_clockwise_rotation += 1

                    count += 1

                else:
                    break

            ## look at the extensions of the anticlockwise rotation
            scalar_anticlockwise_rotation = 1
            while True:

                x = scalar_original_vector * original_vector.x + scalar_anticlockwise_rotation * anticlockwise_rotation.x
                y = scalar_original_vector * original_vector.y + scalar_anticlockwise_rotation * anticlockwise_rotation.y

                point = Point(x, y)

                if point in pairs_of_integers:
                    ### increment the scalar
                    scalar_anticlockwise_rotation += 1

                    count += 1

                else:
                    break


            ## increment the scalar
            scalar_original_vector += 1

    # amount of right angled triangles with their right angle at the origin
    count += grid_size ** 2

    print(count)


if __name__ == "__main__":
    
    grid_size = 50

    start = time.time()

    main(grid_size)

    print(f'elapsed time main:  {time.time() - start}')