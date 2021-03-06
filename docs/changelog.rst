=========
Changelog
=========

This page contains a summary of changes between the official pymetacode releases. Only the biggest changes are listed here. A complete and detailed log of all changes is available through the `GitHub Repository Browser <https://github.com/tillbiskup/pymetacode>`_.


Version 0.3.0
=============

Released 2021-09-23


New features
------------

* Templates adjustable by user (local install)

* Logging added in modules on request in config file

* Templates can be retrieved for other package, prefixing the template name with the package name (see :func:`pymetacode.utils.get_package_data` for details)


Changes
-------

* :class:`pymetacode.configuration.Configuration` with new property ``options``

  (**Important:** Requires updating existing configuration files)


Fixes
-----

* Whitespace in apidoc index preventing proper sphinx build


Version 0.2.0
=============

Released 2021-09-21


New features
------------

* Full sphinx-multiversion support (including version switcher and banner)

* Prospector profile gets added to project.

* Alphabetical sorting of modules in API index.

* Docstrings of classes and modules contain "versionadded" only if version > 0.1, and with correct version.


Bug fixes
---------

* Whitespace in setup.py (spurious empty lines)


Version 0.1.1
=============

Released 2021-09-01

The following bugs have been fixed:

* Permission of the version incrementer

* Templates are contained in package


Version 0.1.0
=============

Released 2021-09-01

* First public release

* Create initial package structure (directory layout, files)

* Add module, class, and function scaffolds to an existing project, including tests and API documentation

* Intuitive command-line interface (CLI)

