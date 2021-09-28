   
"""setup.py: setuptools control."""
 
 
import re
from setuptools import setup 
 
# with open("README.md", "rb") as f:
#     long_descr = f.read().decode("utf-8")
 
 
setup(
    name = "texture_packing_wheel",
    packages = ["texture_packing_wheel"],
    entry_points = {
        "console_scripts": ['texture_packing_wheel = texture_packing_wheel.cli:main']
        },
    version = "1.0",
    description = "Format images into an atlas and manifest for packing with deppth",
    #long_description = long_descr,
    author = "Neil Sandberg & erumi321",
    author_email = "erumi321@gmail.com",
    url = "",
    )