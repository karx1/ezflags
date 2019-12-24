import argparse


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
    def add_flag(self, *args: str, action: bool, help: str = None):
        """Add a flag to the parser.

        :param args: Things to name the flag.
        :type args: str
        :param action: Which boolean the flag returns.
        :type action: bool
        :param help: The help message to display when invoked with -h or --help.
        :type help: str, optional
        """
        action_str = "store_{}".format(_parse_bool(action))
        self.add_argument(*args, action=action_str, help=help)

    def parse_flags(self):
        """
        Parse the flag inputs. Returns an :class:`argparse.Namespace` object with each flag.
        """
        args = self.parse_args()
        return args
