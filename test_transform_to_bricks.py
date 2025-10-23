import unittest
import sys
import os

# 假設 play.py 跟本測試檔在同一目錄下
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from play import transformToBricks, bricks, brick_dict

def get_expected_bricks(brick_id, state):
    key = f"{brick_id}{state}"
    indices = brick_dict[key]
    expected = [[0]*4 for _ in range(4)]
    for idx in indices:
        x = idx % 4
        y = idx // 4
        expected[x][y] = brick_id
    return expected

class TestTransformToBricks(unittest.TestCase):
    def setUp(self):
        # 清空 bricks 陣列
        for x in range(4):
            for y in range(4):
                bricks[x][y] = 0

    def check_brick(self, brick_id, state):
        transformToBricks(brick_id, state)
        expected = get_expected_bricks(brick_id, state)
        for x in range(4):
            for y in range(4):
                self.assertEqual(bricks[x][y], expected[x][y], f"({x},{y}) 應為 {expected[x][y]}")

    def test_n1_brick_state_0(self):
        self.check_brick(1, 0)

    def test_n1_brick_state_1(self):
        self.check_brick(1, 1)

    def test_l1_brick_state_2(self):
        self.check_brick(3, 2)

    def test_o_brick(self):
        self.check_brick(6, 0)

    def test_i_brick_state_1(self):
        self.check_brick(7, 1)

if __name__ == "__main__":
    unittest.main()
