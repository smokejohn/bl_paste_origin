# Blender Operator: Paste objects at scene origin

### This is a simple blender addon that pastes objects from the clipboard to the scene origin

## Info

By default CTRL+V pastes geometry from the clipboard with its location information unchanged, if the objects was 500 units from the origin in the source file then it will be 500 units from the origin when you paste it.

This simple operator centers the geomtry at the scene origin, if you are pasting a group of objects they are centered around the origin as a group

**By default this operator binds itself to the hotkey CTRL+SHIFT+V**

You can rebind this operator in the Keymap **[Edit -> Preferences -> Keymap].**
The operator name is object.paste_origin

## Installing

**You can install this addon by downloading the zip file from the [Releases page](https://github.com/smokejohn/bl_paste_origin/releases)**

The zip file can be used to install the addon via the Blender Preferences GUI:

**[Edit -> Preferences -> Add-ons -> Install... -> select paste_origin.zip -> press OK]**


or by placing the source files in the following directory in a folder called paste_origin:

### Windows
X:\Users\[profile]\AppData\Roaming\Blender Foundation\Blender\2.8x\scripts\addons\
```
../addons/
    └── paste_origin
        └── __init__.py
```
### Linux
~/.config/blender/2.8x/scripts/addons/
```
../addons/
    └── paste_origin
        └── __init__.py
```
