# recursively walks a specific directory and extracts files from all .zips into single directory


import zipfile
import fnmatch
import os

rootPath = r"/users/username/dev/extractzip/tmp/"
pattern = '*.zip'
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
        zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))
