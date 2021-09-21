.. _use_cases:

=========
Use cases
=========

.. sidebar:: Contents

    .. contents::
        :local:
        :depth: 1


Generally, you will use the command-line interface (CLI) of the pymetacode package, *i.e.* typing commands on a terminal, probably from within your IDE while programming. Hence, the use cases described here focus entirely on this user interface.

Of course, you could use the API of the actual code creating code that is contained in the :mod:`pymetacode.coding` module. However, this is only useful for rather special purposes. For details, see the :doc:`API documentation <api/index>`.


General usage
=============

The package provides a command ``pymeta`` (by means of a console-script entry point) available from the command line given the pymetacode package is installed. This command comes with built-in help and follows a rather simple scheme:

.. code-block:: bash

    pymeta <command> <option1> ...

The number of options available and required depends on the type of command used. The design goal is an intuitive and robust user interface with feedback and help built-in and a "grammar" that feels natural.


Getting help for a command
==========================

If you are in doubt how to use the ``pymeta`` command, we've got you covered:

.. code-block:: bash

    pymeta
    pymeta help

are two equivalent commands that display some general help. The result of either of these commands looks like this:

.. code-block:: bash

    General usage:
        pymeta <command> <option1> ...

    Possible commands are:
        write
        add
        create
        help

    To get more details for a command, type:
        pymeta help <command>


Furthermore, you can get help for particular commands, too:

.. code-block:: bash

    pymeta help create

would provide you with help specifically for the "create" command, like this:

.. code-block:: bash

    Usage for create command:
        pymeta create package from <config>

    Prerequisite for this command is an existing configuration stored in
    the file given as <config> (a YAML file). Use

        pymeta write config to <filename>

    to create a config file in YAML format and populate the values
    according to your needs.


Furthermore, if you make a mistake, usually, the context-specific help will be displayed for you as well.


Creating a package
==================

The first step when creating a new package is to write a config file that can be filled with sensible content afterwards:

.. code-block:: bash

    pymeta write config to mypackage_config.yaml

This would write the default configuration to "mypackage_config.yaml". You may want to have a look at the :doc:`details of the configuration file <configuration>`. Change all values in this file according to your needs. Afterwards, you can create the basic structure of your new project:

.. code-block:: bash

    pymeta create package from mypackage_config.yaml

Now, you have a complete package that is installable and deployable. If you would like to know what directories and files have been created, have a look at the :doc:`package directory structure <directory-structure>`. Next is to add some modules to your newly created package.


.. hint::

    You can even use a lazy form of the first command, namely

    .. code-block:: bash

        pymeta write config

    This will result in a configuration file with the default name ``package_config.yaml``.


Adding modules, classes, functions
==================================

All following commands need to be issued from *within* the root directory of your new package.

.. code-block:: bash

    pymeta add module mymodule

will add a module "mymodule" to your package, together with a "test_mymodule" module in the "tests" subdirectory. And even better, the API documentation will be updated as well for you.

Time to add a class to your new module:

.. code-block:: bash

    pymeta add class MyClass to mymodule

Here, again, the class will be added to "mymodule" and a test class added to "test_mymodule". Similarly, you can add a function:

.. code-block:: bash

    pymeta add function my_function to mymodule

Again, function and test class will be added to your package.

In both cases, class and function, a minimum documentation header will be created as well, just to make it easier to properly document your code.

