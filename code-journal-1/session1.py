"""
Write a Python program to print out your full name, your preferred pronouns (optional), 
and two sentences about your favorite movie and your favorite food.
"""


def print_name():
    """Prints my name"""
    print("Name: Ernani Raffo")


def print_pronouns():
    """Prints my pronouns"""
    print("Pronouns: He/Him")


def print_favorite_movie():
    """Prints my favorite movie"""
    print("My favorite movie at the moment is Interstellar because I love the science behind the events of the movie.")


def print_favorite_food():
    """Prints my favorite food"""
    print("I am Brazilian, so it's only right that my favorite food is Brazilian food, which includes rice and beans, "
          "beef strogonoff, and more.")


def main():
    """Call all functions to print information"""
    functions = [print_name, print_pronouns, print_favorite_movie, print_favorite_food]
    for f in functions:
        f()


if __name__ == "__main__":
    main()
