import argparse
import sys
from typing import List


def _parse_bool(inp: bool):
    if inp:
        return "true"
    else:
        return "false"


class FlagParser(argparse.ArgumentParser):
    """
    This is the main class for parsing flags.
    It extends :class:`argparse.ArgumentParser`, and uses the same parameters for __init__.
    """
    def add_flag(self, *args: str, value: bool, help: str = None, required: bool = False):
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
        action_str = "store_{}".format(_parse_bool(value))
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
