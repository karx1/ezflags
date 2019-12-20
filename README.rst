ezflags
=======

A tool that makes creating command line flags super easy.

Built on `argparse <https://docs.python.org/3/library/argparse.html>`__,
switching is no problem at all! You can even use the FlagParser as if it
were a normal ArgumentParser for full integration with existing
arguments.

Install with:

::

   pip install ezflags

Here’s a simple example:

.. code:: py

   # main.py
   import ezflags

   parser = ezflags.FlagParser()
   parser.add_flag('--flag', '-f', boolean=True, help="A demo flag.")

   flags = parser.parse_flags()
   print(flags.flag)

And can be invoked as such:

.. code:: bash

   python main.py --flag
