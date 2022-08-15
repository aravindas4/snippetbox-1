from unittest import TestCase

from .StringBuilder import StringBuilder


class TestStringBuilder(TestCase):

    def test_list_to_string(self):
        input_list = ["a", "r", "a", "v", "i", "n", "d", "a"]

        stringBuilder = StringBuilder()

        for char in input_list:
            stringBuilder.append(char)

        self.assertEqual(str(stringBuilder), "aravinda")
