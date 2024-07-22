=========
Templates
=========

.. sidebar:: Contents

    .. contents::
        :local:
        :depth: 1


pymetacode heavily relies on templates (and uses Jinja as template engine) for performing most of its tasks. The major areas where templates are used are identical to those use cases you encounter in the daily use of the package:

* creating a new module
* adding a class to a module
* adding a function to a module

In each case, not only code stubs are created, but stubs for **unit tests** as well.

Another line of organisation are subpackages. Hence another, though perhaps less likely usecase in the daily use of the package is:

* creating a new subpackage

Below, the templates for these most important aspects are documented in the form currently contained in the pymetacode package itself. Although these templates contain some markup for the Jinja template engine, they should still be rather readable.


Templates for modules
=====================

When adding a module to your package, three files are created in their respective (sub)directories:

* The module in the package source directory (same name as the package)
* The corresponding test module in the tests directory
* The reStructuredText file for the API documentation in the docs/api directory

For details, see the :class:`pymetacode.coding.ModuleCreator` class documentation. Note that the module does not yet have any further content.


The module template
-------------------

.. literalinclude:: ../pymetacode/templates/code/module.j2.py
   :language: python


The test_module template
------------------------

.. literalinclude:: ../pymetacode/templates/code/test_module.j2.py
   :language: python


The module API documentation template
-------------------------------------

.. literalinclude:: ../pymetacode/templates/docs/api_module.j2.rst
   :language: rst


Templates for classes
=====================

When adding a class to a module, two files are modified and the respective code appended:

* The class implementation to the module in the package source directory
* The TestClass implementation in the corresponding test module in the tests directory

As the class template comes with a docstring, and the module API documentation is set such that each class will automatically be documented there (see above), building the documentation will automatically add the class documentation without further ado.

Classes (and corresponding test classes) are always appended to the end of the respective module.

For details, see the :class:`pymetacode.coding.ClassCreator` class documentation.


The class template
------------------

.. literalinclude:: ../pymetacode/templates/code/class.j2.py
   :language: python
   :force:


The test_class template
-----------------------

.. literalinclude:: ../pymetacode/templates/code/test_class.j2.py
   :language: python


Templates for functions
=======================

When adding a function to a module, two files are modified and the respective code appended:

* The function implementation to the module in the package source directory
* The TestClass implementation in the corresponding test module in the tests directory

As the function template comes with a docstring, and the module API documentation is set such that each function will automatically be documented there (see above), building the documentation will automatically add the function documentation without further ado.

Functions (and corresponding test classes) are always appended to the end of the respective module.

For details, see the :class:`pymetacode.coding.FunctionCreator` class documentation.

The function template
---------------------

.. literalinclude:: ../pymetacode/templates/code/function.j2.py
   :language: python


The test_function template
--------------------------

.. literalinclude:: ../pymetacode/templates/code/test_function.j2.py
   :language: python


Templates for subpackages
=========================

When adding a subpackage to your package, three directories are created in their respective (sub)directories:

* The subpackage directory in the package source directory (same name as the package)
* The corresponding test subpackage directory in the tests directory
* The subpackage directory for the API documentation in the docs/api/ directory

Furthermore, in each of these directories, the respective files are created:

* ``__init__.py`` in the subpackage and tests subpackage (empty files each)
* ``index.rst`` in the docs/api subdirectory

If there is no subpackages table of contents (TOC) block in the API docs index.rst file, such a TOC block will be created using a specific template.

For details, see the :class:`pymetacode.coding.SubpackageCreator` class documentation.


The subpackage API documentation template
-----------------------------------------

.. literalinclude:: ../pymetacode/templates/docs/api_subpackage_index.j2.rst
   :language: rst


The subpackage API index TOC template
-------------------------------------

.. literalinclude:: ../pymetacode/templates/docs/api_index_subpackages_block.j2.rst
   :language: rst


Customising templates
=====================

While you as a user are free to :doc:`customise these templates <customisation>` according to your needs, regarding the pattern search and replace options you are pretty much stuck with what is implemented in the respective classes and passed as "context" to the Jinja template engine. As a rule of thumb, the entire :doc:`configuration <configuration>` is passed as context to each template.
