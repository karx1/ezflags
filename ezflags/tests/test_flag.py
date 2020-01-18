# -*- coding: utf-8 -*-

from unittest import TestCase
import ezflags


# MIT License
#
# Copyright (c) 2019-2020 karx1
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


def create_parser():
    parser = ezflags.FlagParser()
    parser.add_flag("--true", "-t", value=True)
    parser.add_flag("--false", "-f", value=False)
    return parser


class TestFlag(TestCase):
    def test_is_true(self):
        parser = create_parser()
        flags = parser.parse_flags(["--true"])
        self.assertTrue(flags.true)
        print("Test passed!")

    def test_is_false(self):
        parser = create_parser()
        flags = parser.parse_flags(["--false"])
        self.assertFalse(flags.false)
        print("Test passed!")

    def test_exception(self):
        parser = create_parser()
        try:
            parser.add_flag("--test", "-t")
        except Exception:
            print("Test passed!")
            return True

        print("Test failed")
        return False

    def test_flag_error(self):
        parser = create_parser()
        parser.add_flag("--flag", value=True)
        try:
            parser.parse_flags(["--test", "flag"])
        except:
            print("Test passed!")
            return True

        print("Test failed")
        return False

    def test_interaction(self):
        parser = create_parser()
        parser.add_argument("--arg", type=str)
        args = parser.parse_args(["--true", "--arg", "test"])
        self.assertEqual("test", args.arg)

    def test_flag_list(self):
        parser = create_parser()
        parser.add_flag("--list", "-l", value=True)
        self.assertIn("--list, -l", parser.flags)
        print("Test passed!")
