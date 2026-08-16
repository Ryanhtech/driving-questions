#  Copyright (c) 2026 Ryanhtech Labs.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import dearpygui.dearpygui as dpg

class MainWindow:
    def __init__(self):
        # Define global variables
        self._question_data: dict[str, list] = { }
        self._enabled = False

        # Initialise the window
        self._init_window()

    def _init_window(self):
        """
        Initialises the window.
        """
        with dpg.window(label="Fenêtre principale", show=self._enabled) as self._window:
            dpg.add_text("Hello, World!")

    def set_question_data(self, question_data: dict[str, list]):
        """
        Sets the question data, and refreshes the window.
        """
        self._question_data = question_data
        self._refresh_ui()

    def enable(self):
        """
        Enables the window and sets it as primary.
        """
        if self._enabled:
            return

        dpg.show_item(self._window)
        dpg.set_primary_window(self._window, True)
        self._enabled = True

    def disable(self):
        """
        Like enable, but opposite.
        """
        if not self._enabled:
            return

        dpg.set_primary_window(self._window, False)
        dpg.hide_item(self._window)
        self._enabled = False

    def _refresh_ui(self):
        """
        Refreshes the UI.
        """
        pass
