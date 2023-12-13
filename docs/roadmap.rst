=======
Roadmap
=======

A few ideas how to develop the project further, currently a list as a reminder for the main developers themselves, in no particular order, though with a tendency to list more important aspects first:


For version 0.5
===============

* GUI code

  * additional subcommand for dialogs

    * ``pymeta add dialog``

  * Discriminate between ui and non-ui windows/dialogs/widgets

    * Two separate commands, one creating ui files for use with QtDesigner, the other for programmatically laid out windows/dialogs/widgets

  * Rearrange modules:

    * separation of models and views


For version 0.6
===============

* Update command (*e.g.*, for configuration, setup.py)

  * Configuration: useful when newer versions of pymetacode change the structure of the configuration file.

* Command for copying templates to user-specific/site-wide directory


For later versions
==================

* Transition config to ``pyproject.toml`` file

* Templates specific to packages (*e.g.*, ASpecD)

  * Requires mechanism to detect which package we are called from

* More configuration options

* Commands for releasing a package to PyPI


Todos
=====

A list of todos, extracted from the code and documentation itself, and only meant as convenience for the main developers. Ideally, this list will be empty at some point.

.. todolist::

