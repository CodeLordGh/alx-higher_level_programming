#!/usr/bin/python3

class MyList(list):
    """A custom list class that adds a print_sorted method."""
    def print_sorted(self):
        """Print the list, sorted in ascending order."""
        print(sorted(self))