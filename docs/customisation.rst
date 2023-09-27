=============
Customisation
=============

While pymetacode comes with defaults that have been proven sensible from its author's practice, starting with version 0.3 you can customise the templates used to create packages.

The most important aspect in this respect is clearly the templates used for creating modules, classes, and functions.

While the default configuration is stored within and gets installed together with the package, all files and templates used are searched for in three places, in this order:

#. In the user-specific data directory (with the package name as subdirectory),

#. In the site-wide data directory (with the package name as subdirectory),

#. Within the package.

Therefore, if you place a template in either of the first two places and adjust it to your needs, it will override the default template distributed with the package.

The actual locations of the user-specific and site-wide data directories are operating-system specific. For details, see the documentation of the `platformdirs package <https://pypi.org/project/platformdirs/>`_ that gets used internally and provides paths for all major platforms (Windows, macOS, Linux/Unix).

