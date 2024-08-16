"""
Not yet tested functionality of DirectedMaze class:
    def __is_move_valid(self, row, col, direction):
    def __change_cell(self, row, col, new_value):
    def __change_root(self, direction):
"""

import unittest
from directed_maze import DirectedMaze as DM


class TestDirectedMaze(unittest.TestCase):
    def test_create_starting_directions(self):
        self.assertEqual(DM.create_starting_directions(2, 2, 2, 2), "R")
        self.assertEqual(DM.create_starting_directions(3, 5, 3, 5), "R")

        self.assertEqual(DM.create_starting_directions(2, 2, 2, 3), "E")
        self.assertEqual(DM.create_starting_directions(3, 5, 3, 6), "E")

        self.assertEqual(DM.create_starting_directions(2, 2, 3, 2), "S")
        self.assertEqual(DM.create_starting_directions(3, 5, 4, 5), "S")

        self.assertRaises(
            TypeError, DM.create_starting_directions, "3", 5, 4, 5)
        self.assertRaises(
            TypeError, DM.create_starting_directions, 3, "L", 4, 5)
        self.assertRaises(
            TypeError, DM.create_starting_directions, "+", "+", 1, 5)

        self.assertRaises(
            AssertionError, DM.create_starting_directions, 0, 2, 2, 2)
        self.assertRaises(
            AssertionError, DM.create_starting_directions, 2, 0, 2, 2)
        self.assertRaises(
            AssertionError, DM.create_starting_directions, 2, 2, 0, 2)
        self.assertRaises(
            AssertionError, DM.create_starting_directions, 2, 2, 2, 0)
        self.assertRaises(
            AssertionError, DM.create_starting_directions, 0, 0, 0, 0)

        self.assertRaises(
            AssertionError, DM.create_starting_directions, 3, 2, 2, 2)
        self.assertRaises(
            AssertionError, DM.create_starting_directions, 2, 3, 2, 2)
        self.assertRaises(
            AssertionError, DM.create_starting_directions, 3, 3, 2, 2)

    def test_create_starting_maze(self):
        self.assertEqual(DM.create_starting_maze(
            2, 2), [["E", "S"], ["E", "R"]])
        self.assertEqual(DM.create_starting_maze(3, 5),
                         [["E", "E", "E", "E", "S"],
                          ["E", "E", "E", "E", "S"],
                          ["E", "E", "E", "E", "R"]])
        self.assertRaises(TypeError, DM.create_starting_maze, "3", 5)
        self.assertRaises(TypeError, DM.create_starting_maze, 3, "L")
        self.assertRaises(AssertionError, DM.create_starting_maze, 0, 2)
        self.assertRaises(AssertionError, DM.create_starting_maze, 2, 0)

    def test___init__(self):
        self.assertRaises(AssertionError, DM, 2, 0)
        self.assertRaises(AssertionError, DM, 2, -2)

        self.assertEqual(DM(3, 3).rows, 3)
        self.assertEqual(DM(2, 6).rows, 2)

        self.assertEqual(DM(3, 3).cols, 3)
        self.assertEqual(DM(2, 6).cols, 6)

        self.assertEqual(DM(3, 3).root, (3, 3))
        self.assertEqual(DM(2, 6).root, (2, 6))

        self.assertEqual(DM(3, 3).valid_values, ["N", "W", "E", "S", "R"])
        self.assertEqual(DM(2, 6).valid_values, ["N", "W", "E", "S", "R"])

        self.assertEqual(DM(3, 3).list, DM.create_starting_maze(3, 3))
        self.assertEqual(DM(2, 6).list, DM.create_starting_maze(2, 6))

    def test___len__(self):
        self.assertEqual(len(DM(3, 3)), 9)
        self.assertEqual(len(DM(2, 6)), 12)

    def test___repr__(self):
        self.assertEqual(DM(3, 3).__repr__(), "Maze(3, 3)")
        self.assertEqual(DM(2, 5).__repr__(), "Maze(2, 5)")

    def test___str__(self):
        self.assertEqual(DM(3, 3).__str__(), "EES\nEES\nEER\n")
        self.assertEqual(DM(5, 2).__str__(), "ES\nES\nES\nES\nER\n")

    def test_row(self):
        A = DM(3, 3)
        A.list = [
            ["E", "E", "S"],
            ["E", "E", "S"],
            ["E", "E", "R"],
        ]
        B = DM(5, 2)
        B.list = [
            ["A", "B"],
            ["C", "D"],
            ["E", "F"],
            ["G", "H"],
            ["K", "L"]
        ]

        self.assertEqual(A.row(1), ["E", "E", "S"])
        self.assertEqual(A.row(3), ["E", "E", "R"])

        self.assertEqual(B.row(1), ["A", "B"])
        self.assertEqual(B.row(5), ["K", "L"])

        self.assertRaises(ValueError, A.row, 0)
        self.assertRaises(ValueError, A.row, -2)

        self.assertRaises(ValueError, B.row, 0)
        self.assertRaises(ValueError, B.row, -2)

        self.assertRaises(TypeError, B.row, "2")

    def test_col(self):
        A = DM(3, 3)
        A.list = [
            ["E", "E", "S"],
            ["E", "E", "S"],
            ["E", "E", "R"],
        ]
        B = DM(5, 2)
        B.list = [
            ["A", "B"],
            ["C", "D"],
            ["E", "F"],
            ["G", "H"],
            ["K", "L"]
        ]

        self.assertEqual(A.col(1), ["E", "E", "E"])
        self.assertEqual(A.col(3), ["S", "S", "R"])

        self.assertEqual(B.col(1), ["A", "C", "E", "G", "K"])
        self.assertEqual(B.col(2), ["B", "D", "F", "H", "L"])

        self.assertRaises(ValueError, A.col, 0)
        self.assertRaises(ValueError, A.col, -2)

        self.assertRaises(ValueError, B.col, 0)
        self.assertRaises(ValueError, B.col, -2)

        self.assertRaises(TypeError, B.col, "2")

    def test___is_cell_in_range(self):
        A = DM(3, 3)
        A.cols = 3
        A.rows = 3
        B = DM(5, 2)
        B.rows = 5
        B.cols = 2

        self.assertFalse(A._DirectedMaze__is_cell_in_range(2, 6))
        self.assertFalse(A._DirectedMaze__is_cell_in_range(5, 5))
        self.assertFalse(B._DirectedMaze__is_cell_in_range(8, 1))
        self.assertFalse(B._DirectedMaze__is_cell_in_range(7, 7))
        self.assertFalse(A._DirectedMaze__is_cell_in_range(0, 0))
        self.assertFalse(B._DirectedMaze__is_cell_in_range(-1, -1))

        self.assertTrue(A._DirectedMaze__is_cell_in_range(2, 2))
        self.assertTrue(A._DirectedMaze__is_cell_in_range(3, 1))
        self.assertTrue(B._DirectedMaze__is_cell_in_range(5, 2))
        self.assertTrue(B._DirectedMaze__is_cell_in_range(2, 2))

    def test___move_in_direction(self):
        self.assertEqual(
            DM(3, 3)._DirectedMaze__move_in_direction(2, 2, "N"), (1, 2))
        self.assertEqual(
            DM(3, 3)._DirectedMaze__move_in_direction(2, 2, "E"), (2, 3))
        self.assertEqual(
            DM(3, 3)._DirectedMaze__move_in_direction(2, 2, "W"), (2, 1))
        self.assertEqual(
            DM(3, 3)._DirectedMaze__move_in_direction(2, 2, "S"), (3, 2))
        self.assertEqual(
            DM(3, 3)._DirectedMaze__move_in_direction(2, 2, "R"), (2, 2))

        self.assertRaises(ValueError, DM(
            3, 3)._DirectedMaze__move_in_direction, 2, 2, "D")

    def test_randomize_root(self):
        A = DM(20, 20)
        self.assertEqual(A.root, (20, 20))
        self.assertEqual(A.list[-1][-1], "R")

        A.randomize_root(1)

        self.assertNotEqual(A.root, (3, 3))
        self.assertNotEqual(A.list[-1][-1], "R")
        self.assertIn(A.list[-1][-1], ["W", "N"])
        A.moved = A.list[-1][-1]
        if A.moved == "N":
            self.assertEqual(A.list[-2][-1], "R")
        if A.moved == "W":
            self.assertEqual(A.list[-1][-2], "R")

        A.randomize_root(99)

        self.assertNotEqual(A.root, (20, 20))
        self.assertNotEqual(A.list[-1][-1], "R")
        self.assertIn(A.list[-1][-1], ["W", "N"])

    def test_convert_maze_to_binary(self):
        A = DM(3, 3)
        A.list = [
            ["E", "E", "S"],
            ["E", "E", "S"],
            ["E", "E", "R"],
        ]
        A.binary = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]

        B = DM(5, 2)
        B.list = [
            ['S', 'W'],
            ['S', 'N'],
            ['E', 'S'],
            ['S', 'W'],
            ['E', 'R']]
        B.binary = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
        self.assertEqual(A.convert_maze_to_binary(), A.binary)
        self.assertEqual(B.convert_maze_to_binary(), B.binary)


if __name__ == '__main__':
    unittest.main()
