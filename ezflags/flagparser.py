import argparse


def _parse_bool(inp: bool):
    if inp:
        return "true"
    else:
        return "false"


class FlagParser(argparse.ArgumentParser):
    def add_flag(self, *args: str, action: bool, help: str = None):
        action_str = f"store_{_parse_bool(action)}"
        self.add_argument(*args, action=action_str, help=help)

    def parse_flags(self):
        args = self.parse_args()
        return args
