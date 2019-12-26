import argparse
import sys


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
    def add_flag(self, *args: str, value: bool, help: str = None):
        """Add a flag to the parser.

        :param args: Things to name the flag.
        :type args: str
        :param value: The value of the flag when present.
        :type value: bool
        :param help: The help message to display when invoked with -h or --help.
        :type help: str, optional
        """
        action_str = "store_{}".format(_parse_bool(value))
        self.add_argument(*args, action=action_str, help=help)

    def parse_flags(self, flag_list=None):
        flag_list = flag_list or sys.argv[1:]
        """
        Parse the flag inputs. Returns an :class:`argparse.Namespace` object with each flag.
        
        :param flag_list: List of flags to parse. This can be used for testing. Defaults to :class:`sys.argv[1:]`.
        :type flag_list: list, optional
        """
        args = self.parse_args(flag_list)
        return args
