# -*- coding: utf-8 -*-

import argparse
import sys
from typing import List
import time
import datetime


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
    return string_one if len(string_one) > len(string_two) else string_two


def _string_min(string_one: str, string_two: str):
    return string_one if len(string_one) < len(string_two) else string_two


def _parse_current_time():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S:%f")
    return st


class FlagParser:
    """
    This is the main class for parsing flags.

    :param program_name: The name of the program. Defaults to :class:`sys.argv[0]`
    :type program_name: str, optional
    :param description: The message to display before the arguments.
    :type description: str, optional
    :param epilogue: The message to display at the end of the help message
    :type epilogue: str, optional
    :param prefix_chars: The prefix of each argument. Defaults to '-'
    :type prefix_chars: str, optional
    :param debug: Turns on or off debug mode. Defaults to false.
    :type debug: bool, optional
    :param debug_file: The file to write to in debug mode. Needs to be a file object as returned by :class:`open`. Defaults to :class`sys.stdout`.
    :type debug_file: file, optional

    flags
        A dictionary of flags and their values.
        For example:\n
        .. code:: py

            {"--flag, -f": True}
    """
    def __init__(
        self,
        program_name: str = None,
        description: str = None,
        epilogue: str = None,
        prefix_chars: str = None,
        debug: bool = False,
        debug_file=None,
    ):
        program_name = program_name or sys.argv[0]
        prefix_chars = prefix_chars or "-"
        debug_file = debug_file or sys.stdout
        self.program_name = program_name
        self.prefix_chars = prefix_chars
        self.description = description
        self.epilogue = epilogue
        self.debug = debug
        self.debug_file = debug_file
        self.flags = {}
        self._added_flags = {}
        self._help_messages = ["--help, -h - Show this help message and exit"]
        self._flag_pairs = {}

    def add_flag(self, *args: str, value: bool, help: str = None):
        """Add a flag to the parser.

        :param args: Things to name the flag. Maximum of two values.
        :type args: str
        :param value: The value of the flag when present.
        :type value: bool
        :param help: A brief description of the flag. These descriptions will be displayed when the `-h` or `--help` flags are present.
        :type help: str, optional
        """
        if len(args) < 0:
            raise ValueError("Must provide at least one flag")
        args = args[:2]
        string_one = args[0]
        try:
            string_two = args[1]
        except IndexError:
            string_two = None

        if string_two:
            bigger_string = _string_max(string_one, string_two)
            smaller_string = _string_min(string_one, string_two)
            key_string = f"{bigger_string}, {smaller_string}"
            help_string = f"{key_string} - {help}"
            self.flags[key_string] = value
            self._added_flags[bigger_string] = value
            self._added_flags[smaller_string] = value
            self._help_messages.append(help_string)
            self._flag_pairs[bigger_string] = smaller_string
        else:
            key_string = string_one
            self.flags[key_string] = value
            self._added_flags[string_one] = value

    def parse_flags(self, flag_list: List[str] = None):
        """Parse the flag inputs. Returns an object with the values of each flag.
        See :ref:`parsing` for more info.

        :param flag_list: List of flags to parse. This can be used for testing. Defaults to :class:`sys.argv[1:]`.
        :type flag_list: list, optional
        :return: Returns an object containing the values of all the flags.
        :rtype: Instance of :class:`argparse.Namespace`
        """
        flag_list = flag_list or sys.argv[1:]
        formatter = _HelpFormatter(
            self._help_messages,
            self.program_name,
            description=self.description,
            epilogue=self.epilogue,
        )
        help_string = formatter.format()
        if "--help" in flag_list or "-h" in flag_list:
            print(help_string)
            sys.exit()
        parsed = _ParsedObj()
        for key, value in self._added_flags.items():
            stripped_flag = key.replace("-", "")
            flipped_bool = not value
            setattr(parsed, stripped_flag, flipped_bool)
        for flag in flag_list:
            if flag in self._added_flags:
                stripped_flag = flag.replace("-", "")
                values = self._flag_pairs.values()
                if flag in values:
                    key = list(self._flag_pairs.keys())[list(self._flag_pairs.values()).index(flag)]
                    short_version = key.replace("-", "")
                    setattr(parsed, short_version, self._added_flags[flag])
                setattr(parsed, stripped_flag, self._added_flags[flag])
            else:
                raise ValueError(f"Unrecognized flag: {flag}")

        return parsed


class _ParsedObj:
    help = "--help"


class _HelpFormatter:
    def __init__(
        self,
        help_messages: List[str],
        program_name: str,
        description: str = None,
        epilogue: str = None,
    ):
        description = description or ""
        epilogue = epilogue or ""
        self.description = description
        self.epilogue = epilogue
        self.program_name = program_name
        self.help_messages = help_messages

    def format(self) -> str:
        formatted_string_opening = (
            f"{self.description}\nUsage: {self.program_name} [flags]\n\n"
        )
        formatted_string_body = "\n".join(self.help_messages)
        formatted_string_closing = f"\n\n{self.epilogue}"
        formatted_string_final = f"{formatted_string_opening}{formatted_string_body}{formatted_string_closing}"
        return formatted_string_final


class FlagParserExtended(argparse.ArgumentParser):
    """
    This is the class for using flags and argparse arguments in conjunction. It uses the same parameters as :class:`FlagParser`.

    :param program_name: The name of the program. Defaults to :class:`sys.argv[0]`
    :type program_name: str, optional
    :param description: The message to display before the arguments.
    :type description: str, optional
    :param epilogue: The message to display at the end of the help message
    :type epilogue: str, optional
    :param prefix_chars: The prefix of each argument. Defaults to '-'
    :type prefix_chars: str, optional
    :param debug: Turns on or off debug mode. Defaults to false.
    :type debug: bool, optional
    :param debug_file: The file to write to in debug mode. Needs to be a file object as returned by :class:`open`. Defaults to :class`sys.stdout`.
    :type debug_file: file, optional

    flags
        A dictionary of flags and their values.
        For example:\n
        .. code:: py

            {"--flag, -f": True}
    """
    def __init__(
        self,
        program_name: str = None,
        description: str = None,
        epilogue: str = None,
        prefix_chars: str = None,
        debug: bool = False,
        debug_file=None,
    ):
        program_name = program_name or sys.argv[0]
        prefix_chars = prefix_chars or "-"
        debug_file = debug_file or sys.stdout
        self.flags = {}
        self.debug = debug
        self.debug_file = debug_file
        super().__init__(
            prog=program_name,
            description=description,
            epilog=epilogue,
            prefix_chars=prefix_chars,
        )
        self._log("Parser initialized")

    def _log(self, string, file=None):
        file = file or self.debug_file
        string = f"{_parse_current_time()} - {string}"
        if self.debug:
            print(string, file=file)

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
        if len(args) < 0:
            raise ValueError("Must provide at least one flag")
        args = args[:2]
        self._log("Processing values")
        result = "true" if value else "false"
        action_str = f"store_{result}"
        string_one = args[0]
        try:
            string_two = args[1]
        except IndexError:
            string_two = None

        if string_two:
            key_string = f"{_string_max(string_one, string_two)}, {_string_min(string_one, string_two)}"
            self.flags[key_string] = value
            self._log(f'Added "{key_string}" to flag list')
        else:
            key_string = f"{string_one}"
            self.flags[key_string] = value
            self._log(f'Added "{key_string}" to flag list')
        self.add_argument(*args, action=action_str, help=help, required=required)
        self._log("Created flag")

    def parse_flags(self, flag_list: List[str] = None) -> argparse.Namespace:
        """Parse the flag inputs. Returns an :class:`argparse.Namespace` object with each flag.
        See :ref:`parsing` for more info.

        :param flag_list: List of flags to parse. This can be used for testing. Defaults to :class:`sys.argv[1:]`.
        :type flag_list: list, optional
        :return: Returns an object containing the values of all the flags.
        :rtype: Instance of :class:`argparse.Namespace`
        """
        self._log("Processing flag list")
        flag_list = flag_list or sys.argv[1:]
        self._log("Parsing flags")
        args = self.parse_args(flag_list)
        self._log("Cleaning up")
        return args
