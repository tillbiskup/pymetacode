"""
{{ package.name }} app.

This module provides the high-level interface to the app and a function that
gets wired up as "gui_script" entry point in the ``setup.py``.
"""

import os
import sys

{%- if gui.splash %}
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QSplashScreen
from PySide6.QtCore import Qt
{%- else %}
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
{%- endif %}

from {{ package.name }}.gui.mainwindow import MainWindow
from {{ package.name }}.gui import utils


{% if gui.splash -%}
def splash_screen():
    splash = QSplashScreen(QPixmap(utils.image_path("splash.svg")))
    splash.show()
    return splash


{% endif -%}
def main():
    """
    Entry point for the GUI application.

    This function serves as main entry point to the GUI application and gets
    added as "gui_script" entry point. Additionally, the essential
    aspects of the (Qt) application are set that are relevant for saving and
    restoring settings, as well as the window icon.
    """
    app = QApplication(sys.argv)
    {% if gui.splash -%}
    splash = splash_screen()

    {% endif -%}
    app.setOrganizationName("{{ gui.organisation }}")
    app.setOrganizationDomain("{{ gui.domain }}")
    app.setApplicationName("{{ package.name }}")
    app.setWindowIcon(QIcon(utils.image_path("icon.svg")))
    window = MainWindow()
    window.show()
    {% if gui.splash -%}

    alignment = Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom
    splash.showMessage("Loaded main window", alignment=alignment)
    splash.finish(window)

    {% endif -%}
    app.exec()


if __name__ == "__main__":
    main()
