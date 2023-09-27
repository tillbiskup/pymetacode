=============
Configuration
=============

Core aspect of the pymetacode package is the configuration for a package that shall be created/maintained using pymetacode. This configuration can be created initially by issuing the following command:

.. code-block:: bash

    pymeta write config

This will result in a file ``package_config.yaml`` whose content should be adjusted according to your specific needs. Upon creating the package, this file will be copied within the root directory of the new package, to the file ``.package_config.yaml`` (mind the leading "." that renders it hidden in a unixoid context).

The structure of this configuration file is documented below. Most of the fields in the ``package`` block resemble the structure of a ``setup.py`` file, while the ``documentation`` block collects additional settings for the Sphinx configuration residing in the ``conf.py`` file in the ``docs`` subdirectory of the project. The block ``options`` (new in version 0.3) contains settings relevant mainly for package creation, the block ``gui`` (new in version 0.4) settings for GUI creation.


.. literalinclude:: package_config.yaml
   :language: yaml
