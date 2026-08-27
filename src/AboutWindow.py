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

from textures import textures


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
            width=450,
            height=172,
            modal=True,
            show=False
        ) as self._window:
            with dpg.group(horizontal=True, horizontal_spacing=16):
                dpg.add_image(textures.TEX_DQ_LOGO_128)

                with dpg.group():
                    dpg.add_text("Ryanhtech DrivingQuestions\nCopyright (c) 2026 Ryanhtech Labs.")
                    dpg.add_text("Licensed under the GNU GPL version 3.0.")

    def show(self):
        """
        Shows the window.
        """
        dpg.show_item(self._window)
