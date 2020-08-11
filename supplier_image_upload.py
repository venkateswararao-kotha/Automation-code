#! /usr/bin/env python3

import os
import requests
from pathlib import Path

dirpath = "/home/student-04-58ef1df2e460/supplier-data/images" #TODO
files = [f for f in os.listdir(dirpath)
           if os.path.isfile(os.path.join(dirpath, f)) and
              f.endswith('.' + 'jpeg')]
print(files)
os.chdir("/home/student-04-58ef1df2e460/supplier-data/images")
url = "http://34.71.61.27/upload/" # TODO


for file in files:
    with open(file,'rb') as opened:
        response = requests.post(url, files={'file':opened})
        if not response.ok:
            response.raise_for_status()
