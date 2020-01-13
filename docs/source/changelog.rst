Changelog
=========

This is a detailed rendering of what changed in each version.

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