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

class TextureManager:
    def __init__(self):
        """
        Manages UI textures.
        """
        pass

    def load_texture(self, file, tag):
        """
        Loads a texture from an image file.
        """
        width, height, channels, data = dpg.load_image(file)

        with dpg.texture_registry():
            dpg.add_static_texture(width=width, height=height, default_value=data, tag=tag)

    def load_textures(self, textures: dict[str, str]):
        """
        Loads multiple textures from a texture dictionary.
        """
        for texture in textures:
            _file = textures[texture]
            self.load_texture(_file, texture)
