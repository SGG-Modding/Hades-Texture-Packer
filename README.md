# Hades Texture Packer
 Creates atlases and the required manifests for textures then sorts them into a package structure to be packed by [deppth](https://github.com/quaerus/deppth)

# Installation
To install the texture packer, install [deppth](https://github.com/quaerus/deppth) and make sure all of its dependencies are downloaded, then pip install the wheel (make sure the extension .whl is in the wheel name when installing it)

# How to Use
Open command prompt and cd to a parent folder, in that folder, have a folder with .pngs (must be a png otherwise the image will not be used) and nested folders with more images.
For this example, the folder with images in it will be called NewIconPkg, with the following setup, and the package we want is ModAuthor-NewIconPackage.\
The package name must include the mod GUID (ModAuthor-ModName) in order to work with Hell2Modding.
```
├── NewIconPkg
│   ├── GUI
│   │   ├── image1.png
│   │   ├── image2.ppng
│   │   ├── image3.png
│   │   │ Icons
│   │   │   ├── Iconimage.png
```

Now call
```
texture_packing_wheel pk -s NewIconPkg -b ModAuthor-NewIconPackage
```
this will generate a folder called ModAuthor-NewIconPackage in the parent directory that will be correctly formatted for deppth packaging, as well as 2 package files to use.\
This will output the following path to the files from the example above
```
ModAuthor-NewIconPackage/GUI/image1.png through 3
and
ModAuthor-NewIconPackage/GUI/Icons/Iconimage.png
```

All image file paths will follow the file path inside the folder they were originally in, plus the package name appended to the start of it - in order to work with Hell2Modding. For example, if the package was in the folder by itself its file path in-game would just be the ``ModAuthor-NewIconPackage\\{Name}``, but if its path was `NewIconPkg/GUI/Icons` then its file path in-game would be `ModAuthor-NewIconPackage\\GUI\\Icons\\{Name}`

## Args
* `-s` or `--source` is the name of the folder you want to recursively search for in images
* `-b` or `--basename` is the name of the package and folder that will be formatted to be packed.
* `-dp` or `--deppthpack` (not used above) set to anything but "True" to disable automatic Deppth Packing.
* `-iH` or `--includehulls` (not used above) set to anything but "False" to calculate hull points.
