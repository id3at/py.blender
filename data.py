""" Autor id3at
Program tworzy obiekt tekstowy z aktualną datą i czasem w programie blender 2.81
który zmienia się wraz z klatkami animacji
"""

import bpy
import datetime
g = datetime.datetime.today()
bpy.ops.object.text_add(enter_editmode=False, location=(0, 0, 0))

def u(g): 
    f = bpy.context.scene.objects['Text']
    g = datetime.datetime.today()
    f.data.body = f'{g}'
bpy.app.handlers.frame_change_pre.append(u)
