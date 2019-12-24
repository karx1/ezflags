from unittest import TestCase

import ezflags


def create_parser():
    parser = ezflags.FlagParser()
    parser.add_flag('--true', '-t', action=True)
    return parser


class TestFlag(TestCase):

    def test_is_true(self):
        parser = create_parser()
        flags = parser.parse_args(['--true'])
        self.assertTrue(flags.true)
        print("Test passed!")
