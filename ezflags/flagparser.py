# -*- coding: utf-8 -*-

import argparse
import sys
from typing import List


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


def _string_max(string_one: str, string_two: str):
    length1 = 0
    length2 = 0
    for i in string_one:
        length1 += 1
    for i in string_two:
        length2 += 1
    if length1 > length2:
        return string_one
    else:
        return string_two


def _string_min(string_one: str, string_two: str):
    length1 = 0
    length2 = 0
    for i in string_one:
        length1 += 1
    for i in string_two:
        length2 += 1
    if length1 < length2:
        return string_one
    else:
        return string_two


class FlagParser(argparse.ArgumentParser):
    """
    This is the main class for parsing flags.
    It extends :class:`argparse.ArgumentParser`, and uses the same parameters for __init__.

    :param program_name: The name of the program. Defaults to :class:`sys.argv[0]`
    :type program_name: str, optional
    :param description: The message to display before the arguments.
    :type description: str, optional
    :param epilogue: The message to display at the end of the help message
    :type epilogue: str, optional
    :param prefix_chars: The prefix of each argument. Defaults to '-'
    :type prefix_chars: str, optional

    flags
        A list of flags added to the parser
    flags_short
        Same as `flags`, but contains the short versions of each flag.
    """

    def __init__(self, program_name: str = None, description: str = None, epilogue: str = None, prefix_chars: str = None):
        program_name = program_name or sys.argv[0]
        prefix_chars = prefix_chars or "-"
        self.flags = []
        self.flags_short = []
        super().__init__(prog=program_name, description=description, epilog=epilogue, prefix_chars=prefix_chars)

    def add_flag(
            self, *args: str, value: bool, help: str = None, required: bool = False
    ):
        """Add a flag to the parser.

        :param args: Things to name the flag. Maximum of two values.
        :type args: str
        :param value: The value of the flag when present.
        :type value: bool
        :param required: Whether the flag is required for the script to run. Defaults to False.
        :type required: bool, optional
        :param help: A brief description of the flag. These descriptions will be displayed when the `-h` or `--help` flags are present.
        :type help: str, optional
        """
        args = args[:2]
        result = "true" if value else "false"
        action_str = f"store_{result}"
        string_one = args[0]
        string_two = args[1]
        self.flags.append(_string_max(string_one, string_two))
        self.flags_short.append(_string_min(string_one, string_two))
        self.add_argument(*args, action=action_str, help=help, required=required)

    def parse_flags(self, flag_list: List[str] = None) -> argparse.Namespace:
        """Parse the flag inputs. Returns an :class:`argparse.Namespace` object with each flag.

        :param flag_list: List of flags to parse. This can be used for testing. Defaults to :class:`sys.argv[1:]`.
        :type flag_list: list, optional
        :return: Returns an object containing the values of all the flags.
        :rtype: Instance of :class:`argparse.Namespace`
        """
        flag_list = flag_list or sys.argv[1:]
        args = self.parse_args(flag_list)
        return args
