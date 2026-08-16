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
        self._selected_group: str | None = None
        self._enabled = False

        self._window_contents_group = None

        # Initialise the window
        self._init_window()

    def _init_window(self):
        """
        Initialises the window.
        """
        with dpg.window(label="Fenêtre principale", show=self._enabled) as self._window:
            dpg.add_spacer(height=16)

            self._init_window_contents()

    def _init_window_contents(self):
        """
        Initialises the window contents.
        """
        if self._window_contents_group is not None:
            if dpg.does_item_exist(self._window_contents_group):
                dpg.delete_item(self._window_contents_group)

            self._window_contents_group = None

        with dpg.group(horizontal=True, parent=self._window) as self._window_contents_group:
            # Question groups
            with dpg.child_window(width=300, height=-1):
                with dpg.tab_bar():
                    with dpg.tab(label="Explorateur de groupes"):
                        with dpg.table():
                            dpg.add_table_column(label="Nom du groupe")
                            for group in self._question_data:
                                with dpg.table_row():
                                    dpg.add_selectable(
                                        label=group,
                                        span_columns=True,
                                        default_value=self._selected_group == group,
                                        user_data=group,
                                        callback=lambda a, b, c: self._select_group(c)
                                    )

            with dpg.child_window(width=-1, height=-1):
                selected_group = self._selected_group
                selected_questions = None

                if self._selected_group is not None:
                    selected_questions = self._question_data[self._selected_group]

                if selected_questions is None:
                    dpg.add_text("Sélectionnez un groupe dans l'Explorateur de groupes pour voir les questions qui lui sont associées.")
                elif len(selected_questions) <= 0:
                    dpg.add_text("Ce groupe ne contient aucune question.")
                else:
                    for question_count in range(len(selected_questions)):
                        dpg.add_separator(label="Question %s" % (question_count + 1))

                        question_entity = selected_questions[question_count]
                        dpg.add_text(question_entity.get_question())

                        with dpg.tree_node(label="Réponse"):
                            dpg.add_text(question_entity.get_answer())

    def _select_group(self, group: str):
        """
        Selects a group and refreshes the UI.
        """
        self._selected_group = group
        self._refresh_ui()

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
        self._init_window_contents()
