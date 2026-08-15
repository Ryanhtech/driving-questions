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

import sqlite3

from Question import Question


class DatabaseLoader:
    @staticmethod
    def get_database_data(path: str):
        """
        Returns the database data as a dictionary from a source database.
        """
        # Load the database
        con = sqlite3.connect(path)
        cur = con.cursor()

        # Get the question groups
        cur.execute("SELECT id, name FROM question_group")
        groups = cur.fetchall()

        # Prepare the dictionary
        data = {}

        # Loop through each group, and fetch the questions that belong to the group.
        for group in groups:
            # Query the questions that match
            cur.execute("""
                SELECT question.question, question.answer
                FROM group_map
                JOIN question ON group_map.question_id = question.id
                WHERE group_map.group_id = ?
            """, (group[0],))
            questions = cur.fetchall()

            question_list = []
            for question in questions:
                question_list.append(Question(question[0], question[1]))

            data[group[1]] = question_list

        con.close()
        return data
