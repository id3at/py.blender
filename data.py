import bpy
import datetime
g = datetime.datetime.today()

def u(g):
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.text_add(enter_editmode=False, location=(0, 0, 0))
    f = bpy.context.scene.objects['Text']
    g = datetime.datetime.today()
    f.data.body = f'{g}'
bpy.app.handlers.frame_change_pre.append(u)