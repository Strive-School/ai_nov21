from dataclasses import field
from gamefield import Gamefield
from point import Point

if __name__ == '__main__':
    p = Point(0, 0, 1, 1)
    q = Point(0, 1, 1.5, 0.5)

    points = [p, q]

    battlefield = Gamefield(points)
    

    battlefield.show_gamefield()

    