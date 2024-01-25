"""
Write a Python program that writes out a table of the function sin(x) vs. x,
where x is tabulated between 0 and 2 with a thousand entries.
Follow the basic Python program structure, including a main program function.
"""
import numpy as np
from tabulate import tabulate


def main():
    values = np.linspace(0, 2 * np.pi, 1000)
    table_data = [(x, sin_x) for x, sin_x in zip(values, np.sin(values))]
    print(tabulate(table_data, headers=['x', 'sin(x)'], floatfmt='.3f', tablefmt='rounded_grid'))


if __name__ == "__main__":
    main()
