import unittest
import utils

class TestDirectedMaze(unittest.TestCase):
    def test_evaluate_type(self):
        self.assertTrue(utils.evaluate_type(int, 1))
        self.assertTrue(utils.evaluate_type(int, 1, 2, -3))
        self.assertFalse(utils.evaluate_type(int, "1"))
        self.assertFalse(utils.evaluate_type(int, [1], 2, -3))
        self.assertFalse(utils.evaluate_type(int, 1, 2.0, -3))

        self.assertTrue(utils.evaluate_type(str, "A", "B"))
        self.assertTrue(utils.evaluate_type(str, "1", "2"))
        self.assertFalse(utils.evaluate_type(str, 1, 2))
        self.assertFalse(utils.evaluate_type(str, ["A"], "B"))
        self.assertFalse(utils.evaluate_type(str, "A", {"B"}))

        self.assertTrue(utils.evaluate_type(list, ["1"], ["2"]))
        self.assertTrue(utils.evaluate_type(list, ["B"], ["A"]))
        self.assertTrue(utils.evaluate_type(list, ["B", "A", 1], [1,2,3]))
        self.assertFalse(utils.evaluate_type(list, 1, 2))
        self.assertFalse(utils.evaluate_type(list, 1, "2"))
        self.assertFalse(utils.evaluate_type(list, 1, ["2"]))
        self.assertFalse(utils.evaluate_type(list, {"1"}, {"2"}))

        self.assertTrue(utils.evaluate_type(dict, {"A":2, "B":1}, {"C":"2", "B":1}))
        self.assertFalse(utils.evaluate_type(dict, {"A":2, "B":1}, 2))

        self.assertTrue(utils.evaluate_type(tuple, (1,)))
        self.assertTrue(utils.evaluate_type(tuple, (1,2)))
        self.assertTrue(utils.evaluate_type(tuple, (1,2), (1,"A")))
        self.assertFalse(utils.evaluate_type(tuple, {1,2}))
        self.assertFalse(utils.evaluate_type(tuple, (1)))
        
        class New():
            def __init__(self, _):
                pass
        self.assertTrue(utils.evaluate_type(New, New(1)))
        self.assertFalse(utils.evaluate_type(New, 1))
        
        class NewInt(int):
            pass
        self.assertTrue(utils.evaluate_type(NewInt, NewInt(1)))
        self.assertFalse(utils.evaluate_type(NewInt, 1))
        
if __name__ == '__main__':
    unittest.main()
