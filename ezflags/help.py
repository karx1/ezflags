# -*- coding: utf-8 -*-

from typing import List
import textwrap

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


class HelpFormatter:
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
        formatted_string_body = textwrap.indent(formatted_string_body, "    ")
        formatted_string_closing = f"\n\n{self.epilogue}"
        formatted_string_final = f"{formatted_string_opening}{formatted_string_body}{formatted_string_closing}"
        return formatted_string_final
