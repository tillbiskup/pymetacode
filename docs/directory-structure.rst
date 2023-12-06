===========================
Package directory structure
===========================

If you create a new package using pymetadata, an entire directory structure will be created that follows best practices of Python packages, results in deployable packages and has been successfully applied to a number of packages of the author.

As there are different ways of how to eventually structure your package directory, pymetacode is opinionated in this regard. The package structure resulting in pymetacode creating a new package (here named "mypackage") is documented below:

.. code-block:: bash

    mypackage
    ├── bin
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
    ├── .gitignore
    ├── LICENSE
    ├── Makefile
    ├── MANIFEST.in
    ├── .package_config.yaml
    ├── README.rst
    ├── setup.py
    └── VERSION


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
