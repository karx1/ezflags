from unittest import TestCase

import ezflags


def create_parser():
    parser = ezflags.FlagParser()
    parser.add_flag('--true', '-t', value=True)
    return parser


class TestFlag(TestCase):

    def test_is_true(self):
        parser = create_parser()
        flags = parser.parse_flags(['--true'])
        self.assertTrue(flags.true)
        print("Test passed!")
