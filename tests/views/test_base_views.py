import unittest

from views import View


class TestBaseView(unittest.TestCase):

    def test_ask_input(self):
        view = View()

        self.assertEqual(view.check_input("Salut", "", required=True), "Salut")
        self.assertEqual(view.check_input("", "", required=False), "")
        self.assertEqual(view.check_input("5", '[1-5]', required=False), "5")
        self.assertEqual(view.check_input("6", '[1-5]', required=False), None)


if __name__ == '__main__':
    unittest.main()
