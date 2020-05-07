# -*- coding: utf-8 -*-
"""
Created on Thu May  7 03:25:30 2020

@author: HP
"""
import html2text
import os

DATA_DIR = "D:/reserch/law casess/Act, No. 20"
xxx = []
outputfile = 0

for file in os.listdir(DATA_DIR):
    if file.endswith(".html"):
        outputfile=outputfile+1
        print(os.path.join(DATA_DIR+"/", file))
        xx = os.path.join(DATA_DIR+"/", file)
        xxx.append(xx)
        with open(xx, 'r') as f_html:
            html = f_html.read()
            name_of_file = str(outputfile)
            completeName = os.path.join(DATA_DIR, name_of_file+".txt")
            with open(completeName, 'wb') as f:
                f.write(html2text.html2text(html).encode('utf-8'))
           