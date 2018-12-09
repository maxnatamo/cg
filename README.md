cg - Config Generator

## Usage

cg uses Xresources - or other X-related config file - to make configs, out of presets.

    usage: cg [ X-config ]

    cg - Generate config files, using X-related variables.

## Getting started.

`cg` uses input files from the `presets_folder` in the config.py file. To make a preset, place the config file in this folder and change the file respectively.

To use the X-variable `color0`, replace the respective part of your preset to include `${color0}`. The format is used, to not interfere with other functionality.

### Example

dunst requires a INI-style config file, which is not easily scriptable. Therefore, you can do something like this, to change the colors:

```
[urgency_low]
background	= "${color0}"
foreground	= "${color7}"

[urgency_normal]
background	= "${color0}"
foreground	= "${color7}"

[urgency_critical]
background	= "${color1}"
foreground	= "${foreground}"
```
