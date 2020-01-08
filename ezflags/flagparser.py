# -*- coding: utf-8 -*-

import argparse
import sys
from typing import List

"""
MIT License

Copyright (c) 2019-2020 karx1

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class FlagParser(argparse.ArgumentParser):
    """
    This is the main class for parsing flags.
    It extends :class:`argparse.ArgumentParser`, and uses the same parameters for __init__.
    """

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
