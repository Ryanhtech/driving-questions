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

class AboutWindow:
    def __init__(self):
        # Initialise UI
        self._init_window()

    def _init_window(self):
        """
        Initialises the window.
        """
        with dpg.window(
            label="À propos de DrivingQuestions",
            width=600,
            height=200,
            modal=True
        ) as self._window:
            dpg.add_text("Hello, World!")
