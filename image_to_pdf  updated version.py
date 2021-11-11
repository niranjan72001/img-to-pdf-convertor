#!/usr/bin/env python
# coding: utf-8

# In[2]:


from fpdf import FPDF#please install the library before running 
import os
import tkinter as tk
from tkinter import filedialog
root=tk.Tk()
file_path=list(filedialog.askopenfilenames(parent=root,title='choose a file'))
print(file_path)
matches=[".jpeg",".png",".gif",".tif",".tiff",".jpg",".bmp",".eps",".raw", ".cr2", ".nef", ".orf", ".sr2"]#list of all the major extensions
img_list = [x for x in file_path if any(y in x for y in matches)]# extracts all images alone  in the given file address
if(img_list!=[]):
    pdf=FPDF(unit='pt',orientation="L",format="A4")
    pdf.set_auto_page_break(0)
    for img in img_list:
        pdf.add_page()
        pdf.image(img,w=500,h=500,x=150)
         
    name=input("how do you want your pdf file to be named . pls enter in the format filename.pdf\n")
    pdf.output(name)
    print("the pdf file  is created and saved it into the following path folder:\n",os.getcwd())
    


# In[ ]:




