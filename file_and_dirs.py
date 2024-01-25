#!/usr/bin/env python3

import os
import tempfile
import shutil

DIRNAME='sample_directory'

print("--- BASICS ---")
print(os.listdir(DIRNAME))

try:
    print(os.stat(f"{DIRNAME}/nonexistant_file"))
except:
    print('yeah, that threw')
print(os.stat(f"{DIRNAME}/a"))
print(os.stat(f"{DIRNAME}/b"))
print(os.stat(f"{DIRNAME}/nonempty_file"))


print("\n--- COPY PLAIN FILES --")
original_file='sample_directory/nonempty_file'
other_file='sample_directory/copy_file'
with open(original_file, 'r') as orig:
    print(f"orig: {original_file} {orig}")
    with open(other_file, 'w') as other:
        print(f"other: {other_file} {other}")
        shutil.copyfileobj(orig, other)
print(os.stat(other_file))

print("\n--- TEMPORARY FILES ---")
original_file='sample_directory/nonempty_file'
print(f"{os.stat(original_file)}\n")
if (1):
    with tempfile.NamedTemporaryFile() as temp:
        print(f"tempfile type:{type(temp)} tempfile:{temp}\n")
        with open(original_file, 'rb') as orig:
            print(f"origfile tempfile:{orig}\n")
            shutil.copyfileobj(orig, temp)
            temp.flush()
        print(type(temp))
        print(temp.name)
        print(os.stat(temp.name))
        ## XXX print(os.stat(temp))
        #   TypeError: stat: path should be string, bytes, os.PathLike or integer, not _TemporaryFileWrapper
        ## XXX print(os.stat(orig))

