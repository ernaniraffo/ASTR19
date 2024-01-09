"""
Write a Python program that declares a class describing your favorite animal. 
Have the data members of the class represent the following physical parameters of the animal: 
length of the arms (float),
length of the legs (float),
number of eyes (int),
does it have a tail? (bool),
is it furry? (bool).
Write an initialization function that sets the values of the data members when an instance of the 
class is created. 
Write a member function of the class to print out and describe the data members representing the 
physical characteristics of the animal.
"""


from random import randint
import string


class Wolf:
    """Class representing a Wolf"""

    def __init__(self,
                 arms_len: float = 1.0,
                 legs_len: float = 1.0,
                 eye_count: int = 2,
                 tail: bool = True,
                 furry: bool = True) -> None:
        self.arms_len = arms_len
        self.legs_len = legs_len
        self.eye_count = eye_count
        self.tail = tail
        self.furry = furry

        # Generate random name for fun
        self.name = self.generate_name()

    def print_info(self) -> None:
        """Prints the wolf's information"""

        print(self)

    def __repr__(self) -> str:
        s =  "Class       : Wolf\n"
        s += "Name        : " + str(self.name) + "\n"
        s += "Arms Length : " + str(self.arms_len) + "\n"
        s += "Legs Length : " + str(self.legs_len) + "\n"
        s += "Eye count   : " + str(self.eye_count) + "\n"
        s += "Tail        : " + str(self.tail) + "\n"
        s += "Furry       : " + str(self.furry) + "\n"
        return s

    def generate_name(self) -> str:
        """Generates a random name for the wolf object"""

        s = string.ascii_uppercase[randint(0, 25)]
        for _ in range(randint(1, 15)):
            s += string.ascii_lowercase[randint(0, 25)]

        return s


def main():
    """Main program"""

    my_wolf = Wolf()
    print(my_wolf)
    my_other_wolf = Wolf(10, 10, 5, False, False)
    print(my_other_wolf)
    my_very_random_wolf = Wolf(randint(0, 100),
                               randint(0, 100),
                               randint(0, 50),
                               bool(randint(0, 1)),
                               bool(randint(0, 1)))
    print(my_very_random_wolf)


if __name__ == "__main__":
    main()
