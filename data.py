""" Autor id3at
Skrypt tworzy obiekt tekstowy z aktualną datą i czasem w programie blender 2.81
który zmienia się wraz z klatkami animacji
"""

# %a - Weekday as locale’s abbreviated name. Sun, Mon, …, Sat (en_US);
# %A - Weekday as locale’s full name. Sunday, Monday, …, Saturday (en_US);
# %b Month as locale’s abbreviated name. Jan, Feb, …, Dec (en_US);
# %B Month as locale’s full name. January, February, 
# %c Locale’s appropriate date and time representation.  Tue Aug 16 21:30:00 1988 (en_US);
#more in https://docs.python.org/3/library/datetime.html

import bpy
import datetime

g = datetime.datetime.today()
bpy.ops.object.text_add(enter_editmode=False, location=(0, 0, 0))

def u(g): 
    f = bpy.context.scene.objects['Text']
    g = datetime.datetime.today()
    f.data.body = f'{g: %a, %b, %Y, %X}'
bpy.app.handlers.frame_change_pre.append(u)
