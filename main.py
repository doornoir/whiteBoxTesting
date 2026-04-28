import unittest
from contrived_func import contrived_func


class TestContrivedFunc(unittest.TestCase):

    def test_val_0(self):
        contrived_func(0)

    def test_val_1(self):
        contrived_func(1)

    def test_val_2(self):
        contrived_func(2)

    def test_val_3(self):
        contrived_func(3)

    def test_val_14(self):
        contrived_func(14)

    def test_val_15(self):
        contrived_func(15)

    def test_val_38(self):
        contrived_func(38)

    def test_val_39(self):
        contrived_func(39)


if __name__ == "__main__":
    unittest.main()
