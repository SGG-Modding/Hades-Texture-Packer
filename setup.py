   
"""setup.py: setuptools control."""
 
 
import re
from setuptools import setup 
 
# with open("README.md", "rb") as f:
#     long_descr = f.read().decode("utf-8")
 
 
setup(
    name = "hades_texture_pack",
    packages = ["texture_packing_wheel"],
    entry_points = {
        "console_scripts": ['hades_texture_pack = texture_packing_wheel.cli:main']
        },
    version = "1.3",
    description = "Format images into an atlas and manifest for packing with deppth",
    #long_description = long_descr,
    author = "Neil Sandberg & erumi321 & zannc",
    author_email = "erumi321@gmail.com",
    url = "",
    )