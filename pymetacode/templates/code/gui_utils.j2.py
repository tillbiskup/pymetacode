"""
Helper functions and classes specific for the GUI part of the package.

In contrast to the :mod:`utils` module of the main package, the utils
contained in this module are specific for the GUI part.
"""

import os


def image_path(name='', icon_dir='images'):
    """
    Return full path to a given image.

    Images, such as icons, are used in several places in GUIs, but are
    usually stored in a separate directory. Hence, a generic function
    returning the full path is both, convenient and modular.

    If the internal organisation of images changes, only this code needs to
    be adapted.

    Parameters
    ----------
    name : :class:`str`
        Name of the icon

    icon_dir : :class:`str`
        Directory containing the icons

        Default: "images"

    Returns
    -------
    path : :class:`str`
        Full path to the icon
    """
    basedir = os.path.dirname(__file__)
    path = os.path.join(basedir, icon_dir, name)
    return path
