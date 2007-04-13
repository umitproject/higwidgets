# -*- Mode: Python; coding: iso-8859-1 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## This file is part of higwidgets
## Copyright (C) 2005 Cleber Rodrigues <cleber@globalred.com.br>
## All rights reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307,
## USA.
##
## Author(s): Cleber Rodrigues <cleber@globalred.com.br>
##
"""
higwidgets/higwindows.py

   window related classes
"""

import gtk

class HIGWindow(gtk.Window):
    """HIGFied Window"""
    def __init__(self, type=gtk.WINDOW_TOPLEVEL):
        gtk.Window.__init__(self, type)
        self.set_border_width(5)

# The Application main window should have no borders...
# so it should be really a gtk.Window
HIGMainWindow = gtk.Window
