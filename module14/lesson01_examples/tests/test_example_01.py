import unittest

from src.example.ops import add, sub, mul, div, async_add


class TestExamples(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start before all test')

    @classmethod
    def tearDownClass(cls):
        print('Start after all test')

    def setUp(self):
        print('Start before each test')

    def tearDown(self):
        print('Start after each test')

    def test_add(self):
        """Add function test"""
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(add(2, 3), 5)

    @unittest.skip('Функціонал не готовий')
    def test_div(self):
        self.assertAlmostEqual(div(2, 3), 0.66666666)
        with self.assertRaises(ZeroDivisionError) as cm:
            div(3, 0)


class TestAsyncMethod(unittest.IsolatedAsyncioTestCase):
    async def test_add(self):
        """Add function test"""
        r = await async_add(2, 3)
        self.assertEqual(r, 5)
