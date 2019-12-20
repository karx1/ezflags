ezflags
=======

A tool that makes creating command line flags super easy.

Built on `argparse <https://docs.python.org/3/library/argparse.html>`__,
switching is no problem at all! You can even use the FlagParser as if it
were a normal ArgumentParser for full integration with existing
arguments.

Install with:

.. code:: bash

   pip install ezflags

Here’s a simple example:

.. code:: py

   # main.py
   import ezflags

   parser = ezflags.FlagParser()
   parser.add_flag('--flag', '-f', action=True, help="A demo flag.")

   flags = parser.parse_flags()
   print(flags.flag)

To integrate with ArgumentParser:

.. code:: py

   import ezflags

   parser = ezflags.FlagParser()
   parser.add_flag('--flag', '-f', action=True, help="A demo flag.")
   parser.add_argument('--arg', '-a', help="A demo argument.")

   args = parser.parse_args() # Flags are included, too!
   print(args.flag)
   print(args.arg)

This can be invoked as such:

.. code:: bash

   python main.py --flag
   # With ArgumentParser()
   python main.py --flag --arg arg

Supports
--------

Supports Python 3.2 and up.

##License

MIT license. See the
`LICENSE <https://github.com/karx1/ezflags/blob/master/LICENSE>`__ file
for more details.
