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
import dearpygui.demo as dpg_demo

from EmptyMainWindow import EmptyMainWindow
from MainWindow import MainWindow

from StyleManager import StyleManager
from DatabaseLoader import DatabaseLoader
from TextureManager import TextureManager
from textures.textures import DQ_TEXTURES


class DqApplication:
    def __init__(self):
        """
        Application management class.
        """
        # Initialise Dear PyGui
        self._init_dpg()

        # Initialise textures
        self._init_textures()

        # Initialise styles
        self._init_styles()

        # Initialise file pickers
        self._init_file_pickers()

        # Initialise UI
        self._init_ui()

        # Initialise local variables
        self._menu_items_to_toggle = [
            self._item_menu_select_random_question_group
        ]

        # Initialise question data
        self._set_question_data({})

    def _init_dpg(self):
        """
        Initialises the dearpygui library.
        """
        dpg.create_context()

    def _init_textures(self):
        """
        Initialises a [TextureManager] object and uses it to load the app's textures.
        """
        self._texture_manager = TextureManager()
        self._texture_manager.load_textures(DQ_TEXTURES)

    def _init_styles(self):
        """
        Initialises UI styles.
        """
        self._style_manager = StyleManager()
        self._style_manager.set_global_theme(self._style_manager.style_default)

    def _init_file_pickers(self):
        """
        Initialises the file pickers.
        """
        # Create the datanase selection file picker
        with dpg.file_dialog(
            directory_selector=False,
            show=False,
            callback=self._callback_database_file_picker_select,
            width=700,
            height=400,
            modal=True,
            min_size=(700, 400),
            max_size=(700, 400),
            label="Ouvrir une base"
        ) as self._item_file_picker_database:
            dpg.add_file_extension(".dqdb", label="Base DrivingQuestions", color=(0, 0, 120))

    def _init_ui(self):
        """
        Initialises the user interface.
        """
        # Create a viewport, which is a system window.
        dpg.create_viewport(
            title="DrivingQuestions",
            width=800,
            height=500
        )

        # Initialise callbacks
        dpg.set_viewport_resize_callback(
            lambda a, b, c: self._callback_viewport_resize()
        )
        dpg.set_frame_callback(
            frame=3,
            callback=lambda: self._callback_start()
        )

        # Initialise the menu
        self._init_menu()

        ## Window creation ##
        # Create the EmptyMainWindow
        self._window_main_empty = EmptyMainWindow(self._style_manager)

        self._window_main = MainWindow()

        # The UI has been initialised; finish dearpygui initialisation.
        dpg.setup_dearpygui()

    def _init_menu(self):
        """
        Initialise the viewport's menu.
        """
        with dpg.viewport_menu_bar():
            with dpg.menu(label="Fichier"):
                dpg.add_menu_item(
                    label="Ouvrir une base...",
                    callback=lambda: dpg.show_item(self._item_file_picker_database)
                )

                dpg.add_separator()

                dpg.add_menu_item(
                    label="Quitter DrivingQuestions"
                )

            with dpg.menu(label="Outils"):
                self._item_menu_select_random_question_group = dpg.add_menu_item(
                    label="Sélectionner un groupe de questions aléatoire",
                    callback=lambda a, b, c: self._window_main.select_random_group()
                )

            with dpg.menu(label="Affichage"):
                dpg.add_menu_item(
                    label="Plein écran"
                )

            with dpg.menu(label="Aide"):
                dpg.add_menu_item(label="A propos de DrivingQuestions...")
                dpg.add_menu_item(label="A propos de Dear PyGui...", callback=lambda: dpg.show_about())

                dpg.add_separator()

                with dpg.menu(label="Débogage"):
                    dpg.add_menu_item(label="Menu de débogage", callback=lambda: dpg.show_debug())
                    dpg.add_menu_item(label="Gestionnaire d'éléments", callback=lambda: dpg.show_item_registry())
                    dpg.add_menu_item(label="Gestionnaire de polices", callback=lambda: dpg.show_font_manager())
                    dpg.add_menu_item(label="Gestionnaire de styles", callback=lambda: dpg.show_style_editor())
                    dpg.add_menu_item(label="Statistiques de l'interface", callback=lambda: dpg.show_metrics())

                    dpg.add_separator()

                    dpg.add_menu_item(label="Documentation de Dear PyGui", callback=lambda: dpg.show_documentation())
                    dpg.add_menu_item(label="Démonstration de Dear PyGui", callback=lambda: dpg_demo.show_demo())

    ## Helper functions ##
    def _set_question_data(self, data: dict[str, list]):
        """
        Sets the question data (stored in MainWindow), and refreshes the UI.
        """
        self._window_main.set_question_data(data)
        empty = len(data) <= 0

        if empty:
            # There are no questions.
            self._window_main.disable()
            self._window_main_empty.enable()
        else:
            self._window_main_empty.disable()
            self._window_main.enable()

        # Enable or disable menu items depending on the status
        for item in self._menu_items_to_toggle:
            if empty:
                dpg.disable_item(item)
            else:
                dpg.enable_item(item)

    ## Callbacks ##
    def _callback_database_file_picker_select(self, sender, app_data):
        # Retrieve the database file path
        file_path = list(app_data["selections"].values())[0]

        # Refresh the data
        self._set_question_data(DatabaseLoader.get_database_data(file_path))

    def _callback_viewport_resize(self):
        """
        Callback to be called when the viewport's size changes.
        """
        self._window_main_empty.refresh()

    def _callback_start(self):
        """
        Callback to be called when the UI starts.
        """
        self._window_main_empty.refresh()

    def mainloop(self):
        """
        Performs the UI's main loop. Does not return unless the UI terminates.
        """
        # Display the viewport we created earlier
        dpg.show_viewport(maximized=True)

        # Start dearpygui's main loop
        dpg.start_dearpygui()

        # Destroy the UI
        dpg.destroy_context()
