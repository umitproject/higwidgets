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
higwidgets/higlabels.py

   labels related classes
"""

__all__ = ['HIGSectionLabel', 'HIGHintSectionLabel', 'HIGEntryLabel',
        'HIGDialogLabel']

import gtk

class HIGSectionLabel(gtk.Label):
    """
    Bold label, used to define sections
    """
    def __init__(self, text=None):
        gtk.Label.__init__(self)
        if text:
            self.set_markup("<b>%s</b>" % (text))
            self.set_justify(gtk.JUSTIFY_LEFT)
            self.set_alignment(0, 0.50)
            self.set_line_wrap(True)
    def set_new_text(self,text):
        self.set_markup("<b>%s</b>" % (text))
        self.set_justify(gtk.JUSTIFY_LEFT)
        self.set_alignment(0, 0.50)
        self.set_line_wrap(True)
        

    def _set_text(self, text):
        self.set_markup("<b>%s</b>" % (text))

class HIGHintSectionLabel(gtk.HBox, object):
    """
    Bold label used to define sections, with a little icon that shows up
    a hint when mouse is over it.
    """
    def __init__(self, text=None, hint=None):
        gtk.HBox.__init__(self)

        self.label = HIGSectionLabel(text)
        self.hint = Hint(hint)

        self.pack_start(self.label, False, False)
        self.pack_start(self.hint, False, False, 5)

class HIGHintLabel(gtk.HBox, object):
    """
    Label used to define sections, with a little icon that shows up a hint when mouse is
    over it.
    """
    def __init__(self, text=None, hint=None):
        gtk.HBox.__init__(self)

        self.label = gtk.Label(text)
        self.hint = Hint(hint)

        self.pack_start(self.label, False, False)
        self.pack_start(self.hint, False, False, 5)


class Hint(gtk.EventBox, object):
    def __init__(self, hint):
        gtk.EventBox.__init__(self)
        self.hint = hint

        self.hint_image = gtk.Image()
        self.hint_image.set_from_stock(gtk.STOCK_DIALOG_INFO,
                gtk.ICON_SIZE_SMALL_TOOLBAR)

        self.add(self.hint_image)
        
        self.connect("button-press-event", self.show_hint)

    def show_hint(self, widget, event=None):
        hint_window = HintWindow(self.hint)
        hint_window.show_all()

    
class HintWindow(gtk.Window):
    def __init__(self, hint):
        gtk.Window.__init__(self, gtk.WINDOW_POPUP)
        self.set_position(gtk.WIN_POS_MOUSE)
        bg_color = gtk.gdk.color_parse("#fbff99")

        self.modify_bg(gtk.STATE_NORMAL, bg_color)

        self.event = gtk.EventBox()
        self.event.modify_bg(gtk.STATE_NORMAL, bg_color)
        self.event.set_border_width(10)
        self.event.connect("button-press-event", self.close)

        self.hint_label = gtk.Label(hint)
        self.hint_label.set_use_markup(True)
        self.hint_label.set_line_wrap(True)

        self.event.add(self.hint_label)
        self.add(self.event)

    def close(self, widget, event=None):
        self.destroy()
        

class HIGEntryLabel(gtk.Label):
    """
    Simple label, like the ones used to label entries
    """
    def __init__(self, text=None, underline=False):
        gtk.Label.__init__(self)
        if text is not None:
            self.set_text(text)
        self.set_justify(gtk.JUSTIFY_LEFT)
        self.set_alignment(0, 0.50)
        self.set_use_underline(underline)
        self.set_use_markup(True)
        self.set_line_wrap(True)

class HIGDialogLabel(gtk.Label):
    """
    Centered, line-wrappable label, usually used on dialogs.
    """
    def __init__(self, text=None):
        gtk.Label.__init__(self, text)
        self.set_justify(gtk.JUSTIFY_CENTER)
        self.set_use_underline(True)
        self.set_use_markup(True)
        self.set_line_wrap(True)

class HIGLabel(gtk.Label):
    def __init__(self, text=''):
        gtk.Label.__init__(self)

        self.set_text(text)
        self.set_justify(gtk.JUSTIFY_LEFT)
        self.set_alignment(0, 0.50)
        self.set_line_wrap(True)

if __name__ == "__main__":
    w = gtk.Window()
    h = HIGHintSectionLabel("Label", "Hint")
    test = HIGEntryLabel("x86_64")
    box = gtk.VBox()
    box.add(h)
    box.add(test)
    w.add(box)
    w.connect("delete-event", lambda x, y: gtk.main_quit())
    w.show_all()

    gtk.main()
