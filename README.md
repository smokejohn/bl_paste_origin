# Blender Operator: Paste objects at scene origin

## This is a simple blender addon that pastes objects from the clipboard to the scene origin

By default CTRL+V pastes geometry from the clipboard with its location information unchanged, if the objects was 500 units from the origin in the source file then it will be 500 units from the origin when you paste it.

This simple operator centers the geomtry at the scene origin, if you are pasting a group of objects they are centered around the origin as a group

***By default this operator binds itself to the hotkey CTRL+SHIFT+V***

You can rebind this operator in the Keymap [Edit -> Preferences -> Keymap]
The operator name is object.paste_origin
