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

class EmptyMainWindow:
    def __init__(self):
        """
        This window is displayed when there is no loaded database.
        """
        # Create UI attributes
        self._enabled = False

        # Initialise the window
        self._init_window()

    def _init_window(self):
        """
        Initialises the window.
        """
        with dpg.window(label="Bienvenue", show=self._enabled) as self._item_window:
            with dpg.child_window(
                label="Bienvenue",
                width=400,
                height=200,
                resizable_x=False,
                resizable_y=False
            ) as self._item_welcome_child_window:
                self._item_welcome_text = dpg.add_text(
                    "Aucune base de questions chargée.\nPour ouvrir une base, utilisez la commande Fichier > Ouvrir une base.",
                    wrap=380,
                    pos=[10, 80]
                )

    def enable(self):
        """
        Enable the window, and set it as primary window.
        """
        if self._enabled:
            return

        dpg.show_item(self._item_window)
        dpg.set_primary_window(self._item_window, True)
        self._enabled = True
