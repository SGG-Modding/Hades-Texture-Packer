# Hades Texture Packer
 Creates atlases and the required manifests for textures then sorts them into a package structure to be packed by (deppth)[https://github.com/quaerus/deppth]

# Installation
To install the texture packer, install (deppth)[https://github.com/quaerus/deppth] and make sure all of its dependencies are dowloaded, then pip install the wheel (make sure the extension .whl is in teh wheel name when installing it)

# How to Use
Open command prompt and cd to a parent folder, in that folder have a folder with .pngs (must be a png otherwise the image will not be used) and nested folders with more images. For this example the folder with images in it will be called NewIconPkg, and the package we want is NewIconPackage. Now call
```
texture_packing_wheel pk -s NewIconPkg -b NewIconPackage
```
this will generate a folder called NewIconPackage in the parent directory that will be correctly formatted for deppth packaging.

All image file path will follow file path inside the folder they were originally in. For example if the package was in the folder by itself its file path ingame would just be its name, but if it's path was `NewIconPkg/GUI/Icons` then its file path in game would `GUI\\Icons\\{Name}`

## Args
* `-s` or `--source` is the name of the folder you want to recursivly search for in images
* `b` or `--basename` is the name of the package and folder that will be formatted to be packed.
* `-iH` or `--includehulls` (not used above) set to anything but "False" to calculate hull points
