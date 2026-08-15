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

from EmptyMainWindow import EmptyMainWindow

class DqApplication:
    def __init__(self):
        """
        Application management class.
        """
        # Initialise Dear PyGui
        self._init_dpg()

        # Initialise UI
        self._init_ui()

    def _init_dpg(self):
        """
        Initialises the dearpygui library.
        """
        dpg.create_context()

    def _init_ui(self):
        """
        Initialises the user interface.
        """
        # Create a viewport, which is a system window.
        dpg.create_viewport(
            title="DrivingQuestions",
            width=600,
            height=400
        )

        # Initialise the menu
        self._init_menu()

        ## Window creation ##
        # Create the EmptyMainWindow
        self._window_main_empty = EmptyMainWindow()
        self._window_main_empty.enable()

        # The UI has been initialised; finish dearpygui initialisation.
        dpg.setup_dearpygui()

    def _init_menu(self):
        """
        Initialise the viewport's menu.
        """
        with dpg.viewport_menu_bar():
            with dpg.menu(label="Fichier"):
                dpg.add_menu_item(
                    label="Ouvrir une base..."
                )

                dpg.add_separator()

                dpg.add_menu_item(
                    label="Quitter DrivingQuestions"
                )

    def mainloop(self):
        """
        Performs the UI's main loop. Does not return unless the UI terminates.
        """
        # Display the viewport we created earlier
        dpg.show_viewport()

        # Start dearpygui's main loop
        dpg.start_dearpygui()

        # Destroy the UI
        dpg.destroy_context()
