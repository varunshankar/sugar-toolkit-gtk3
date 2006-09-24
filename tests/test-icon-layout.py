#!/usr/bin/python
import pygtk
pygtk.require('2.0')

from sugar.session.UITestSession import UITestSession

session = UITestSession()
session.start()

import sys
import random

import gtk
import goocanvas

from view.home.IconLayout import IconLayout
from sugar.canvas import IconColor
from sugar.canvas.IconItem import IconItem
from sugar.canvas.CanvasView import CanvasView

window = gtk.Window()
window.connect("destroy", lambda w: gtk.main_quit())
window.show()

canvas = CanvasView()
canvas.show()
window.add(canvas)

canvas_model = goocanvas.CanvasModelSimple()
root = canvas_model.get_root_item()

item = goocanvas.Rect(x=0, y=0, width=1200, height=900,
                      line_width=0.0, fill_color='#e2e2e2')
root.add_child(item)

icon_layout = IconLayout(1200, 900)

for i in range(0, 20):
	color = IconColor.IconColor()

	icon = IconItem(size=75, color=color,
					icon_name='stock-buddy')
	root.add_child(icon)

	icon_layout.add_icon(icon)

canvas.set_model(canvas_model)

gtk.main()
