"""
    Dummy project, with dummy code
"""
import sys


def add(x, y):
    """Adds two numbers"""
    return x + y


def multiply(x, y):
    """Multiplies two numbers"""
    return x * y


def main():
    """Main method"""
    print(add(2, 3))
    print(multiply(2, 3))


if __name__ == '__main__':
    sys.exit(main())
