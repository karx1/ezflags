.. ezflags documentation master file, created by
   sphinx-quickstart on Sat Dec 21 19:07:53 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ezflags's documentation!
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   parsing
   ezflags
   changelog

`ezflags` is a tool that makes creating command line flags super easy.

Built on `argparse <https://docs.python.org/3/library/argparse.html>`__,
switching is no problem at all! You can even use the FlagParser as if it
were a normal ArgumentParser for full integration with existing
arguments.

Here’s a simple example:

.. code:: py

   # main.py
   import ezflags

   parser = ezflags.FlagParser()
   parser.add_flag('--flag', '-f', value=True, help="A demo flag.")

   flags = parser.parse_flags()
   print(flags.flag)

To integrate with ArgumentParser:

.. code:: py

   import ezflags

   parser = ezflags.FlagParser()
   parser.add_flag('--flag', '-f', value=True, help="A demo flag.")
   parser.add_argument('--arg', '-a', help="A demo argument.")

   args = parser.parse_args() # Flags are included, too!
   print(args.flag)
   print(args.arg)

This can be invoked as such:

.. code:: bash

   python main.py --flag
   # With ArgumentParser()
   python main.py --flag --arg arg

