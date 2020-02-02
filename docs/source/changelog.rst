Changelog
=========

This is a detailed rendering of what changed in each version.

.. _vp1p4p2:

v1.4.2
------
 - Create custom exceptions. This makes it easier to include ezflags in error handlers.
 - Add str() and repr() functionality to _ParsedObj. This makes it easier to see what flags are present and their values.

.. _vp1p4p1:

v1.4.1
-------
 - Move FlagParserExtended to a new location, `ezflags.ext`
 - Bring back logging

.. _vp1p4p0:

v1.4.0
-------
 - This update is a complete rewrite of the module.
 - It moves away from using argparse and instead parses flags "in-house".
 - The new class saves a lot of memory because it now only contains the logic for boolean flags.
 - The argparse-like parser is still available through the FlagParserExtended class. (This may be moved to another location, so the import will be different.)
 - The new parser class is still incomplete and may be buggy. Features will be brought back in the next series of incremental updates.

.. _vp1p3p3:

v1.3.3
-------
 - Add debug mode. This prints various messages about what the parser is currently doing. You can specify the file it writes to like this:
 
.. code:: py

	file = open("somefile.txt", "w")
	parser = ezflags.FlagParser(debug=True, debug_file=file)

.. _vp1p3p2:

v1.3.2
-------
 - Change `parser.flags` to a dictionary with the flag names (and short versions, if applicable) corresponding to their value.
 - Fix bug where an error was raised when providing only one flag name

.. _vp1p3p1:

v1.3.1
-------
 - Add `parser.flags_short`, which contains the short versions of each flag. Each index in `flags_short` corresponds to its longer counterpart in `parser.flags`.

.. _vp1p3p0:

v1.3.0
-------
 - You can now see a list of all the flags in the parser using `parser.flags`
 - Performance improvements

.. _vp1p2p1:

v1.2.1
-------
 - Add a kwarg to specify whether the flag is required or not
 - Limit to two flag names
 - Improved type checking
 - Take info from README and add it to index of documentation

.. _vp1p2p0:

v1.2.0
-------
 - Rename kwarg action to value
 - Allow use of lists of flags in parse_flags(). Defaults to sys.argv[1:]

.. _vp1p1p4:

v1.1.4
------
 - Create documentation

.. _vp1p1p3:

v1.1.3
-------
 - Add advanced functionality

.. _vp1p1p1:

v1.1.1
-------
 - Initial release