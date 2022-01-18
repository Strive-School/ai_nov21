import numpy as np
import matplotlib.pyplot as plt

class Gamefield():
    def __init__(self, items = []) -> None:
        self.__dims = [0, 10, 0, 10]
        self.__elements = []
        self.items = items

    def show_gamefield(self):
        plt.axis(self.__dims)

        for i in range(1000):

            xs = []
            ys = []
            ms = []
            mks = []
            cs = []

            for item in self.items:
                x, y, m, mk, c = item.x, item.y, item.direction, item.mark, item.color
                xs.append(x)
                ys.append(y)
                ms.append(m)
                mks.append(mk)
                cs.append(c)

            
            
            for x, y, m, mk, c in zip(xs, ys, ms, mks, cs):
                plt.xlim([self.__dims[0], self.__dims[1]])
                plt.ylim([self.__dims[2], self.__dims[3]])
                plt.plot(x, y, marker=mk, color=c)
            plt.pause(0.01)
            plt.clf()

            for item in self.items:
                item.move(0.1)
                item.bounce()


        plt.show()

        plt.close('all')