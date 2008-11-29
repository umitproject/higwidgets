#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005-2006 Insecure.Com LLC.
# Copyright (C) 2007-2008 Adriano Monteiro Marques
#
# Author: Adriano Monteiro Marques <adriano@umitproject.org>
#         Cleber Rodrigues <cleber.gnu@gmail.com>
#
# This library is free software; you can redistribute it and/or modify 
# it under the terms of the GNU Lesser General Public License as published 
# by the Free Software Foundation; either version 2.1 of the License, or 
# (at your option) any later version.
#
# This library is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public 
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public License 
# along with this library; if not, write to the Free Software Foundation, 
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA 

"""
higwidgets/higlogindialog.py

   a basic login/authentication dialog
"""

__all__ = ['HIGTable']

import gtk

#from higlabels import *
#from higentries import *
from higwidgets.higboxes import HIGBox

class HIGTable(gtk.Table):
    """
    A HIGFied table
    """

    # TODO:
    # - Automatic position packing,
    # - Gereric attach function that detects the widget type
    
    def __init__(self, rows=1, columns=1, homogeneous=False):
        gtk.Table.__init__(self, rows, columns, homogeneous)
        self.set_row_spacings(6)
        self.set_col_spacings(12)
        
        self.rows = rows
        self.columns = columns
		
    def attach_label(self, widget, x0, x, y0, y):
        self.attach(widget, x0, x, y0, y, xoptions=gtk.FILL)
            
    def attach_entry(self, widget, x0, x, y0, y):
        self.attach(widget, x0, x, y0, y, xoptions=gtk.FILL|gtk.EXPAND)

class HIGTableRNet(gtk.Table, HIGBox):
    def __init__(self, rows=1, columns=1, homogeneous=False):
        gtk.Table.__init__(self, rows, columns, homogeneous)
        self._set_spacing(12)

        self.__rows = rows
        self.__columns = columns

        self.__last_point = (0, 0)


    def _set_spacing(self, spacing):
        self.set_row_spacings(spacing)
        self.set_col_spacings(spacing)


    def _resize(self, rows, columns):
        self.__rows = rows
        self.__columns = columns

        self.resize(rows, columns)


    def _attach_next(self,
                     child,
                     xoptions=gtk.EXPAND|gtk.FILL,
                     yoptions=gtk.EXPAND|gtk.FILL,
                     xpadding=0,
                     ypadding=0):
        row, column = self.__last_point

        if row != self.__rows:

            self.attach(child,
                        column,
                        column + 1,
                        row,
                        row + 1,
                        xoptions,
                        yoptions,
                        xpadding,
                        ypadding)

            if column + 1 == self.__columns:

                column = 0
                row += 1

            else:
                column += 1

            self.__last_point = (row, column)
