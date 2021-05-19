# graphsciics
A Python library for ascii-based graphics, with basic animation support as of version 0.0.2.

Usage:

`from graphsciics.graphsciics import *`

`from graphsciics.animate import *`

`canvas = Canvas(1, 1)`

`rect1 = Rectangle(1, 1, Cursor(0, 0))`

`rect2 = Rectangle(2, 2, Cursor(0, 0))`

`anim.addframe(rect1)`

`anim.addframe(rect2)`

`canvas.draw(anim)`
