#!/usr/bin/env python3

import zipfile

ZIPFILE='sample.zip'
CHUNK_SIZE=50

# ...the file header is like the first 50 bytes...so ignore the rest. 
# EXCEPT, zip is smart enough to skip the haders.
zipObj = zipfile.ZipFile(ZIPFILE)
for component in zipObj.namelist():
    print(f"COMPONENT: {component}")
    comp_file = zipObj.open(component)
    data_chunk = comp_file.read(CHUNK_SIZE)
    file_length = len(data_chunk)
    print(f"  DATA: {data_chunk}")
    #while(data_chunk):
    #    data_chunk = comp_file.read(CHUNK_SIZE)
    #    file_length += len(data_chunk)
    print(f" size {file_length}")
    
    
    

