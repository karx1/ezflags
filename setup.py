# -*- coding: utf-8 -*-

from setuptools import setup
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

with open("README.rst") as f:
    readme = f.read()

extras_require = {"docs": ["sphinx", "sphinx-rtd-theme"]}

setup(
    name="ezflags",
    version=ezflags.__version__,
    packages=["ezflags", "ezflags.ext"],
    url="https://github.com/karx1/ezflags",
    project_urls={"Documentation": "https://ezflags.readthedocs.io/en/latest"},
    license="MIT",
    author="karx",
    author_email="nerdstep710@gmail.com",
    description="A tool that makes creating command line flags super easy.",
    long_description=readme,
    python_requires=">=3.6",
    extras_require=extras_require,
    test_suite="nose.collector",
    tests_require=["nose"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
)
