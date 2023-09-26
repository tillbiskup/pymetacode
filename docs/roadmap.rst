=======
Roadmap
=======

A few ideas how to develop the project further, currently a list as a reminder for the main developers themselves, in no particular order, though with a tendency to list more important aspects first:


For version 0.4
===============

* CITATION.cff template?

  * Would possibly need much more information in .package_config.yaml

* Directory structure for GUIs (created with PySide6)

  * CLI commands for creating GUI structure and adding a GUI window
  * Update configuration to cope with things such as splash
  * Modify setup.py and MANIFEST.in in case of added GUI
  * Add gui_scripts entrypoint to setup.py

* Using black for code style?

* Update command (*e.g.*, for configuration, setup.py)

* Command for copying templates to user-specific/site-wide directory

* Check for existence of class/function and issue warning if already present instead of adding it again.

* Makefile for tests, prospector, documentation, ...


For later versions
==================

* More configuration options.

* Commands for releasing a package to PyPI
