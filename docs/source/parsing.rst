.. _parsing:

Parsing flags
=============

`parse_flags` takes in a list of strings denoting which flags to parse. If no list is given, it uses :class:`sys.argv[1]`.
If providing a list, the flags must be typed exactly as you would type them in the command line.
For example:

.. code:: py

   import ezflags

   parser = ezflags.FlagParser()
   parser.add_flag(--flag, value=True)

   flags = parser.parse_flags(["--flag"])
   print(flags.flag) # Prints True


If your flag has a dash ("-") in it (excluding the dash(es) at the beginning), it is represented in python with an underscore.
For example:

.. code:: py

   import ezflags
   parser = ezflags.FlagParser()
   parser.add_flag('--demo-flag', value=True, help="A demo flag.")

   flags = parser.parse_flags()
   print(flags.demo_flag) # Represents --demo-flag