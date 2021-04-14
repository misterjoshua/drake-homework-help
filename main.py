import unittest


def parse_coords(coords):
    """
    Parses the user's coordinates into letter and number components.
    Example: parse_coords('A1') => { 'letter': 'A', 'num': '1 }
    """

    if len(coords) != 2:
        raise Exception("Invalid input")

    return {
        'letter': coords[0].upper(),
        'num': coords[1]
    }


class InvalidInputException(Exception):
    """This exception is thrown when the user's input is invalid"""
    pass


def check_grid(grid, letter, num):
    """
    Checks the grid at the letter and number coordinate. Returns True if it's
    a hit, returns False if it's a miss.
    """

    if letter not in grid:
        raise InvalidInputException('That letter is invalid!')
    if num not in grid[letter]:
        raise InvalidInputException('That number is invalid!')

    if grid[letter][num] == 'X':
        return True
    else:
        return False


class MyTest(unittest.TestCase):
    def test_get_coords(self):
        coords = parse_coords("A1")
        self.assertEqual(coords['letter'], 'A')
        self.assertEqual(coords['num'], '1')

        coords = parse_coords("B1")
        self.assertEqual(coords['letter'], 'B')
        self.assertEqual(coords['num'], '1')

        coords = parse_coords("B2")
        self.assertEqual(coords['letter'], 'B')
        self.assertEqual(coords['num'], '2')


    def test_check_grid(self):
        grid = {
            'A': {
                '1': 'X',
                '2': ' ',
            },
            'B': {
                '1': ' ',
                '2': 'X',
            }
        }

        self.assertTrue(check_grid(grid, 'A', '1'))
        self.assertFalse(check_grid(grid, 'A', '2'))
        self.assertFalse(check_grid(grid, 'B', '1'))
        self.assertTrue(check_grid(grid, 'B', '2'))

        with self.assertRaises(Exception):
            raise Exception('works fine')

        # @see https://docs.python.org/3/library/unittest.html
        with self.assertRaises(InvalidInputException):
            check_grid(grid, 'C', '1')

        with self.assertRaises(InvalidInputException):
            check_grid(grid, 'A', '9')


    def test_integration(self):
        grid = {
            'A': {
                '1': 'X',
                '2': ' ',
            },
            'B': {
                '1': ' ',
                '2': 'X',
            }
        }

        game_main_method(grid)


def game_main_method(grid):
    user_input = input('coords: ')
    components = parse_coords(user_input)
    try:
        is_hit = check_grid(grid, components['letter'], components['num'])
        if is_hit:
            print("hit!")
        else:
            print("miss!")

    except InvalidInputException:
        print("You messed up! Type it right next time")


if __name__ == '__main__':
    grid = {
        'A': {
            '1': 'X',
            '2': ' ',
        },
        'B': {
            '1': ' ',
            '2': 'X',
        }
    }
    game_main_method(grid)
