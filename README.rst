========================
pymetacode documentation
========================

Welcome! This is pymetacode, a Python package helping to write and maintain Python packages.

Code that writes code - yes, that's correct. Automating the boring stuff, one could say, or helping to focus on the creative part of programming. In any case, the idea for this package stems from experience with a couple of Python projects, and as such it is pretty opinionated, focussing on personal needs regarding structure and layout. Nevertheless, it tries to be as user-friendly as possible, coming with an intuitive command-line interface (CLI).

Want to get an idea? Here you go. Creating a new package would be a two-step process:

1) Write a configuration file for your new package (and afterwards fill it with sensible content)

.. code-block:: bash

    pymeta write config to mypackage_config.yaml

2) Create the basic Python package structure for your package.

.. code-block:: bash

    pymeta create package from mypackage_config.yaml

Once you have your package structure, you can add modules, classes, and functions to your package from within the package's root directory any time:

.. code-block:: bash

    pymeta add module mymodule
    pymeta add class MyClass to mymodule
    pymeta add function my_function to mymodule

And now - happy coding!


Features
========

A list of features:

* Create initial package structure (directory layout, files)

* Add module, class, and function scaffolds to an existing project, including tests and API documentation

* Intuitive command-line interface (CLI)


And to make it even more convenient for users and future-proof:

* Open source project written in Python (>= 3.7)

* Developed fully test-driven

* Extensive user and API documentation



.. warning::
    pymetacode is currently under active development and still considered in Beta development state. Therefore, expect frequent changes in features and public APIs that may break your own code. Nevertheless, feedback as well as feature requests are highly welcome.


Installation
============

To install the pymetacode package on your computer (sensibly within a Python virtual environment), open a terminal (activate your virtual environment), and type in the following:

.. code-block:: bash

    pip install pymetacode


License
=======

This program is free software: you can redistribute it and/or modify it under the terms of the **BSD License**.

