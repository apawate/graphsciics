# graphsciics
A Python library for ascii-based graphics, with features such as animation and custom shapes as of version 0.0.3.

A basic program:

`from graphsciics.graphsciics import *`

`from graphsciics.animate import *`

`from graphsciics.custom import *`

`canvas = Canvas(1, 1)`

`custom = Custom()`

`custom.build()` (this will prompt the user and build a custom shape line by line)

`rect1 = Rectangle(1, 1, Cursor(0, 0))`

`rect2 = Rectangle(2, 2, Cursor(0, 0))`

`anim = Animation(1)`

`anim.addframe(rect1)`

`anim.addframe(rect2)`

`anim.addframe(custom)`

`canvas.draw(anim)`
