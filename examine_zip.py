#!/usr/bin/env python3

import zipfile

ZIPFILE='sample.zip'
CHUNK_SIZE=10

# Standard zip stuff
zipObj = zipfile.ZipFile(ZIPFILE)
for component in zipObj.namelist():
    print(component, end = "")
    comp_file = zipObj.open(component)
    data_chunk = comp_file.read(CHUNK_SIZE)
    file_length = len(data_chunk)
    while(data_chunk):
        data_chunk = comp_file.read(CHUNK_SIZE)
        file_length += len(data_chunk)
    print(f" size {file_length}")
    
    
    

