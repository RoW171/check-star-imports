# check-star-imports
python debugging tool to show how many objects were imported when using a 'star import'

The idea behind this was to show how important it is to know what you are doing when imporing with asterisks

## Usage

The module consists out of a single class 'check_star_imports' which is used as a contextmanager like this:

    from checkstarimport import *  # see what I did there
    
    with check_str_import:
        from string import *
    
    # this will print out:
    12 objects were imported!
    


## Why

I came up with this after workig with some opengl stuff and pyglet. I ended up with something like this:

`from pyglet.gl import glDisable, glViewport, glMatrixMode, glLoadIdentity, glOrtho, glEnable, gluPerspective,
        glRotatef, glTranslatef, glClearColor, glBlendFunc, glTexParameteri, glFogfv, GLfloat, glHint, glFogi, glFogf,
        GL_DEPTH_TEST, GL_PROJECTION, GL_MODELVIEW, GL_CULL_FACE, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_BLEND,
        GL_LINE_SMOOTH, GL_LINE_SMOOTH_HINT, GL_NICEST, GL_NEAREST, GL_LINEAR, GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
        GL_TEXTURE_MAG_FILTER, GL_FOG, GL_FOG_COLOR, GL_FOG_HINT, GL_DONT_CARE, GL_FOG_MODE, GL_FOG_START, GL_FOG_END`

It seemed like a reaonable idea to use this instead:

`from pyglet.gl import *`

Until I checked globals() and noticed the latter just imported 9214 objects!

Hopefully this will educate people to know what they are importing or
to use [`__all__`](https://docs.python.org/3/tutorial/modules.html, "Python Docs")(6.4.1.) in their projects.



