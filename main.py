from src import game
import unittest

class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.g = game.Game()
    
    def __roll_many(self, n, pins):
        for i in range(n):
            self.g.roll(pins)
    
    def __roll_strike(self):
        self.g.roll(10)

    def __roll_spare(self):
        self.g.roll(5)
        self.g.roll(5)

    def test_gutter_game(self):
        self.__roll_many(20, 0)
        self.assertEqual(0, self.g.score())

    def test_all_ones(self):
        self.__roll_many(20, 1)
        self.assertEqual(20, self.g.score())
    
    def test_one_spare(self):
        self.__roll_spare()
        self.g.roll(3)
        self.__roll_many(17, 0)
        self.assertEqual(16, self.g.score())

    def test_one_strike(self):
        self.__roll_strike()
        self.g.roll(3)
        self.g.roll(4)
        self.__roll_many(16, 0)
        self.assertEqual(24, self.g.score())
    
    def test_perfect_game(self):
        self.__roll_many(12,10)
        self.assertEqual(300, self.g.score())

if __name__ == '__main__':
    unittest.main()