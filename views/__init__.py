#! /usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Program Name:              vis
# Program Description:       Measures sequences of vertical intervals.
#
# Filename: views/__init__.py
# Purpose: Load the vis views modules.
#
# Copyright (C) 2012, 2013 Christopher Antila, Jamie Klassen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------

__all__ = ['main', 'VisOffsetSelector', 'icons_rc', 'web_view', 'Ui_select_offset',
           'Ui_web_display']

from desktop_vis.views import main
from desktop_vis.views import VisOffsetSelector
from desktop_vis.views import icons_rc
from desktop_vis.views import web_view
from desktop_vis.views import Ui_select_offset
from desktop_vis.views import Ui_web_display
