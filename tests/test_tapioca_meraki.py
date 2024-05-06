# coding: utf-8

import unittest

from tapioca_meraki import Meraki


class TestTapiocaMeraki(unittest.TestCase):

    def setUp(self):
        self.wrapper = Meraki()


if __name__ == '__main__':
    unittest.main()
