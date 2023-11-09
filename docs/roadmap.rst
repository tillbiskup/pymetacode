=======
Roadmap
=======

A few ideas how to develop the project further, currently a list as a reminder for the main developers themselves, in no particular order, though with a tendency to list more important aspects first:


For version 0.5
===============

* GUI code

  * additional subcommands for non-windows (dialogs, widgets)

    * ``pymeta add dialog``
    * ``pymeta add widget``

  * Rearrange modules:

    * separation of models and views

* Add subpackage command

  * Helpful for organising packages
  * ``pymeta add subpackage <name>``

* Update command (*e.g.*, for configuration, setup.py)

  * Configuration: useful when newer versions of pymetacode change the structure of the configuration file.

* CITATION.cff template?

  * Would possibly need much more information in .package_config.yaml

* Using black for code style?

  * If used, should go into git hook (pre-commit?)

* Command for copying templates to user-specific/site-wide directory

* Makefile for tests, prospector, documentation, ...


For later versions
==================

* Templates specific to packages (*e.g.*, ASpecD)

  * Requires mechanism to detect which package we are called from

* More configuration options

* Commands for releasing a package to PyPI


Todos
=====

A list of todos, extracted from the code and documentation itself, and only meant as convenience for the main developers. Ideally, this list will be empty at some point.

.. todolist::

