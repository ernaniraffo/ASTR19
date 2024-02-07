import numpy as np
import matplotlib.pyplot as plt


def main():
    # number of numbers to generate
    n = 100

    # create array x from 0 to 2*π with n points
    x = np.linspace(0, 2 * np.pi, n)

    # y = sin(x)
    y = np.sin(x)

    # plot x (horizontal) versus y (vertical)
    plt.plot(x, y)

    # the figure is generated in the background
    # it needs to be shown with this command
    plt.show()


if __name__ == '__main__':
    main()
