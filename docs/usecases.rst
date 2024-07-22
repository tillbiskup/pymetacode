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

But before you add modules to your new package, you may want to make yourself familiar with the (helper) files created and double-check that the ``CITATION.cff`` file contains correct contents. In particular, check the author names in there, as the ``CITATION.cff`` format separates given and family names, whereas ``setup.py`` (and the pymetacode configuration file) do not. Furthermore, you may want to add your ORCID.


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


.. hint::

    All these commands work with (nested) subpackages as well. Just use the familiar dot notation for the module names, *e.g.* ``mysubpackage.mymodule``. For details on how to create subpackages, see below.


Adding subpackages
==================

All following commands need to be issued from *within* the root directory of your new package.

.. code-block:: bash

    pymeta add subpackage mysubpackage

will add a subpackage "mysubpackage" to your package, together with a "mysubpackage" directory in the "tests" subdirectory. And even better, the API documentation will be updated for you as well.

This works similarly for nested subpackages. However, note that you need to *first* create the intermediate subpackage(s). Hence, a possible sequence of commands would be:

.. code-block:: bash

    pymeta add subpackage mysubpackage
    pymeta add subpackage mysubpackage.mysubsubpackage

But why would one want to add nested subpackages? Suppose you had a rather complicated Python package in mind and wanted to separate functional and technical layers, with the former being the first line of organisation of your package. A typical layer structure for technical layers according to Jacobson would be "boundaries", "controllers", and "entities" (BCE). Hence, for each functional layer you would end up with (at least) three technical layers. All these could be modelled as subpackages in Python. In such cases, however, it might be sensible to import the facades of the individual functional layers to the main namespace of your package for easier access by the users.


Adding a GUI and GUI windows
============================

All following commands need to be issued from *within* the root directory of your package.

.. code-block:: bash

    pymeta add gui

will add the scaffold (directory structure, files, documentation, configuration in setup.py) necessary for adding a graphical user interface (GUI) to your package. Note that **Qt6 and the PySide6 Qt bindings** are used.

At the same time, a first window, named ``mainwindow``, will be added, together with a very basic template of the UI file used by the Qt Designer to layout your window.

Adding additional windows is as simple as

.. code-block:: bash

    pymeta add window mysubwindow

As windows are always suffixed with "window", you are not required to add the suffix "window", but in case you do, it will be handled accordingly.

Hence, the same window as above will get added with the command

.. code-block:: bash

    pymeta add window mysub

Therefore, use whichever way you are more comfortable with.

The same strategy applies for GUI widgets. To add a GUI widget, just type

.. code-block:: bash

    pymeta add widget fancywidget

As widgets are always suffixed with "widget", you are not required to add the suffix "widget", but in case you do, it will be handled accordingly.

Hence, the same widget as above will get added with the command

.. code-block:: bash

    pymeta add widget fancy

Therefore, use whichever way you are more comfortable with.

Again, if you want to add dialogs, follow the same pattern:

.. code-block:: bash

    pymeta add dialog fancydialog

As dialogs are always suffixed with "dialog", you are not required to add the suffix "dialog", but in case you do, it will be handled accordingly.

Hence, the same dialog as above will get added with the command

.. code-block:: bash

    pymeta add dialog fancy

Therefore, use whichever way you are more comfortable with.
