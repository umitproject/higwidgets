#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2005-2006 Insecure.Com LLC.
# Copyright (C) 2007-2008 Adriano Monteiro Marques
#
# Author: Adriano Monteiro Marques <adriano@umitproject.org>
#         Cleber Rodrigues <cleber.gnu@gmail.com>
#         João Paulo de Souza Medeiros <ignotus21@gmail.com>
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
higwidgets/higboxes.py

   box related classes
"""

__all__ = ['HIGHBox', 'HIGVBox']

import gtk

class HIGBox(gtk.Box):
    def _pack_noexpand_nofill(self, widget):
        self.pack_start(widget, expand=False, fill=False)

    def _pack_expand_fill(self, widget):
        self.pack_start(widget, expand=True, fill=True)

    # Methods included for RadialNet integration
    def _pack_expand_nofill(self, widget):
        self.pack_start(widget, expand=True, fill=False)

    def _pack_end_noexpand_nofill(self, widget):
        self.pack_end(widget, expand=False, fill=False)

    def _pack_end_expand_fill(self, widget):
        self.pack_end(widget, expand=True, fill=True)

    def _pack_end_expand_nofill(self, widget):
        self.pack_end(widget, expand=True, fill=False)

class HIGHBox(gtk.HBox, HIGBox):
    def __init__(self, homogeneous=False, spacing=12):
        gtk.HBox.__init__(self, homogeneous, spacing)

    pack_section_label = HIGBox._pack_noexpand_nofill
    pack_label = HIGBox._pack_noexpand_nofill
    pack_entry = HIGBox._pack_expand_fill

class HIGVBox(gtk.VBox, HIGBox):
    def __init__(self, homogeneous=False, spacing=12):
        gtk.VBox.__init__(self, homogeneous, spacing)

    # Packs a widget as a line, so it doesn't expand vertically
    pack_line = HIGBox._pack_noexpand_nofill

class HIGSpacer(HIGHBox):
    def __init__(self, widget=None):
        HIGHBox.__init__(self)
        self.set_spacing(6)
        
        self._pack_noexpand_nofill(hig_box_space_holder())
        
        if widget:
            self._pack_expand_fill(widget)
            self.child = widget
    
    def get_child(self):
        return self.child

def hig_box_space_holder():
    return gtk.Label("    ")


class HIGStatusbar(gtk.Statusbar, HIGBox):
    def __init__(self, homogeneous=False, spacing=12):
        gtk.HBox.__init__(self, homogeneous, spacing)


class HIGScrolledWindow(gtk.ScrolledWindow):
    def __init__(self):
        gtk.ScrolledWindow.__init__(self)
        self.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.set_shadow_type(gtk.SHADOW_NONE)
        self.set_border_width(6)

