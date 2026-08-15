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


class StyleManager:
    def __init__(self):
        """
        Manages UI styles.
        """
        self.__load_styles()

    def __load_styles(self):
        # Default style
        with dpg.theme() as self.style_default:
            with dpg.theme_component(dpg.mvAll):
                # Main
                dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8.0, 8.0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 5.0, 6.0, category=dpg.mvThemeCat_Core)

                # Rounding
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5.0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 5.0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 5.0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 5.0, category=dpg.mvThemeCat_Core)

                # Alignment
                dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign, 0.5, 0.5, category=dpg.mvThemeCat_Core)

                # Colours
                dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 0, 0), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, (240, 240, 240), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (230, 230, 230), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (220, 220, 220), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Border, (177, 177, 177), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (177, 177, 177), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (200, 200, 200), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (215, 215, 215), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, (91, 148, 227), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, (215, 215, 215), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBg, (218, 218, 218), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, (205, 205, 205), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, (205, 205, 205), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, (160, 160, 160), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, (150, 150, 150), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, (130, 130, 130), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Button, (205, 205, 205), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Header, (205, 205, 205), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Separator, (175, 175, 175), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip, (215, 215, 215), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered, (205, 205, 205), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, (180, 180, 180), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Tab, (205, 205, 205), category=dpg.mvThemeCat_Core)
                
                dpg.add_theme_color(dpg.mvThemeCol_TableHeaderBg, (205, 205, 205), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TableBorderStrong, (175, 175, 175), category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TableBorderLight, (195, 195, 195), category=dpg.mvThemeCat_Core)

        with dpg.theme() as self.style_no_window_padding:
            with dpg.theme_component(dpg.mvAll):
                # Main
                dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0.0, 0.0, category=dpg.mvThemeCat_Core)

                # Rounding
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5.0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 5.0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 5.0, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_WindowTitleAlign, 0.5, 0.5, category=dpg.mvThemeCat_Core)

        # Change the font and set it as default
        with dpg.font_registry():
            self.font_inter_regular_16 = dpg.add_font("inter_regular.ttf", 16)
            self.font_inter_regular_24 = dpg.add_font("inter_regular.ttf", 24)

        dpg.bind_font(self.font_inter_regular_16)

    def set_global_theme(self, theme: str | int):
        dpg.bind_theme(theme)

    def set_item_style(self, item: str | int, theme: str | int):
        dpg.bind_item_theme(item, theme)
    
    def set_item_font(self, item: str | int, font: str | int):
        dpg.bind_item_font(item, font)
