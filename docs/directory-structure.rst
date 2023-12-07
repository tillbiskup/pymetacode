===========================
Package directory structure
===========================

If you create a new package using pymetadata, an entire directory structure will be created that follows best practices of Python packages, results in deployable packages and has been successfully applied to a number of packages of the author.


Basic package structure
=======================

As there are different ways of how to eventually structure your package directory, pymetacode is opinionated in this regard. The package structure resulting in pymetacode creating a new package (here named "mypackage") is documented below:

.. code-block:: bash

    mypackage
    ├── bin
    │   ├── formatPythonCode.sh
    │   └── incrementVersion.sh
    ├── docs
    │   ├── api
    │   │   └── index.rst
    │   ├── audience.rst
    │   ├── changelog.rst
    │   ├── conf.py
    │   ├── developers.rst
    │   ├── index.rst
    │   ├── installing.rst
    │   ├── make.bat
    │   ├── Makefile
    │   ├── people.rst
    │   ├── roadmap.rst
    │   ├── _templates
    │   │   ├── page.html
    │   │   └── versions.html
    │   └── usecases.rst
    ├── mypackage
    │   └── __init__.py
    ├── tests
    │   └── __init__.py
    ├── CITATION.cff
    ├── .gitignore
    ├── LICENSE
    ├── Makefile
    ├── MANIFEST.in
    ├── .package_config.yaml
    ├── README.rst
    ├── setup.py
    └── VERSION


In short, the modules reside in a subdirectory with the same name as the package, and parallel to that are directories for tests and documentation (``tests``, ``docs``).

Furthermore, a ``setup.py`` file is created to have the package installable using pip, and a license (``LICENSE``) and readme (``README.rst``) file are present.

The package version is stored in the file ``VERSION``, a ``.gitignore`` file exists as well in the package root, and depending on the configuration, a git repository is initialised within the package root directory. In this case, a pre-commit hook is installed as well incrementing the version number for each commit, using the file ``./bin/incrementVersion.sh``, and auto-formatting Python code using Black (via ``./bin/formatPythonCode.sh``) on each commit.

The ``CITATION.cff`` file contains metadata for properly citing/referencing your software package. Double-check its contents after initially creating the package, particular the author(s) names, and update it as needed (ORCIDs, DOI via Zenodo or else on first release).

For convenience, a ``Makefile`` is present, helping to automate recurring tasks during development, such as generating the documentation, running all the tests, checking your code using Prospector, and reformatting your code using Black.

Finally, the hidden file ``.package_config.yaml`` contains all the metadata you originally provided when creating the package. This file is *required* for pymetacode to work, hence do not delete it. Usually, you can just ignore it. However, it may be wise to keep it up to date.


Additional structure for GUIs
=============================

If you add a graphical user interface (GUI) to your package, the following additional directories and files are added to the basic package layout shown above:

.. code-block::

    mypackage
    ├── docs
    │   ├── api
    │   │   ├── gui
    │   │   │   ├── mypackage.gui.app.rst
    │   │   │   ├── mypackage.gui.mainwindow.rst
    │   │   │   └── index.rst
    │   │   └── ...
    │   └── ...
    ├── mypackage
    │   ├── gui
    │   │   ├── app.py
    │   │   ├── images
    │   │   │   │── icon.svg
    │   │   │   └── splash.svg
    │   │   ├── __init__.py
    │   │   ├── mainwindow.py
    │   │   ├── Makefile
    │   │   └── ui
    │   │       └── __init__.py
    │   └── ...
    └── tests
        ├── gui
        │   ├── __init__.py
        │   ├── test_app.py
        │   └── test_mainwindow.py
        └── ...
