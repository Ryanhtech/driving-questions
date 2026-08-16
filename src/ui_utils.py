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

def align_coord(item_size: tuple, parent_size: tuple, pos: str) -> list:
    _new_x = 0
    _new_y = 0

    if pos == "tl":
        # On ne fait rien
        pass
    elif pos == "ml":
        _new_x = 0
        _new_y = (parent_size[1] // 2) - (item_size[1] // 2)
    elif pos == "mm":
        _new_x = (parent_size[0] // 2) - (item_size[0] // 2)
        _new_y = (parent_size[1] // 2) - (item_size[1] // 2)
    elif pos == "br":
        _new_x = parent_size[0] - item_size[0]
        _new_y = parent_size[1] - item_size[1]

    return [_new_x, _new_y]

def align_item(item: int | str, pos: str):
    """
    Positionne un élément par rapport à son parent.
    Valeurs possibles pour le paramètre position :

    - 'tl' : en haut à gauche
    - 'tm' : en haut au milieu
    - 'tr' : en haut à droite
    - 'ml' : au milieu à gauche
    - 'mm' : au milieu
    - 'mr' : au milieu à droite
    - 'bl' : en bas à gauche
    - 'bm' : en bas au milieu
    - 'br' : en bas à droite
    """
    # On récupère le parent de l'élément
    _parent = dpg.get_item_parent(item)

    # On récupère les coordonnées et la taille du parent
    _p_x, _p_y = dpg.get_item_pos(_parent)
    _p_width = dpg.get_item_width(_parent)
    _p_height = dpg.get_item_height(_parent)

    # On récupère la taille de l'objet
    _width = dpg.get_item_width(item)
    _height = dpg.get_item_height(item)

    _new_x = 0
    _new_y = 0

    # On place l'objet en fonction de l'alignement demandé
    if _parent is not None \
        and _p_x is not None and _p_y is not None \
        and _p_width is not None and _p_height is not None \
        and _width is not None and _height is not None:

        dpg.set_item_pos(item, align_coord((_width, _height), (_p_width, _p_height), pos))

    return