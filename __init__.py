bl_info = {
    "name": "Paste at Origin",
    "author": "Johannes Rauch",
    "blender": (2, 80, 0),
    "description": "Pastes the object from the clipboard at the scene origin",
    "category": "Object",
}

import bpy
import mathutils

from bpy.types import Operator

class PasteOrigin(Operator):
    ''' Operator that pastes the object in the buffer to the origin '''

    bl_idname = "object.paste_origin"
    bl_label = "Paste at origin"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        context = bpy.context
        scene = context.scene

        result = bpy.ops.view3d.pastebuffer()
        if result == {'FINISHED'}:
        # paste operator finished successfully
            if len(context.selected_objects) > 0:
            # we have a selection
                objects = context.selected_objects
                if len(objects) > 1:
                    # multiple objects
                    # calc average
                    avg_pos = mathutils.Vector()
                    for obj in objects:
                        avg_pos += obj.location

                    avg_pos *= 1/len(objects)

                    # use average position and center the objects around it
                    for obj in objects:
                        obj.location -= avg_pos

                else:
                    # single object
                    # center
                    context.selected_objects[0].location = (0, 0, 0)

        return {'FINISHED'}

addon_keymaps = []

def register():
    bpy.utils.register_class(PasteOrigin)

    #keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(PasteOrigin.bl_idname, 'V', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append(km)


def unregister():
    bpy.utils.unregister_class(PasteOrigin)

    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)

    del addon_keymaps[:]
