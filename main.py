#!/usr/bin/env python
# coding: utf-8

# In[7]:


import sys
import os
sys.path.append('C:\ProgramData\Anaconda3\Lib\site-packages')


# In[8]:


from flask import Flask, render_template, request, redirect,send_from_directory,send_file,abort,url_for
import pandas as pd
from test import *

df = pd.read_excel('contents.xlsx')
get_list_of_pdfs = []


# In[9]:


app = Flask(__name__,template_folder="template")
o=-1
@app.route("/")
def hello():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    query = request.form.get('query1')
    selected = request.form.get('query')
    if (not query and selected=='select'):
        return render_template('failure.html')
    if(selected=='select'):
        get_list_of_pdfs.append(principle_function(query.lower(),df)) 
    else:
        get_list_of_pdfs.append(principle_function(selected.lower(),df))
    return redirect('/get-pdf')

@app.route("/get-pdf")
def get_pdf():
    try:
        return render_template('view.html',get_list_of_pdfs = get_list_of_pdfs,o=o)
    except FileNotFoundError:
        abort(404)
@app.route("/clear")
def get_clear():
    get_list_of_pdfs.clear()
    return {}

if __name__ == "__main__":
    app.run(debug=True ,host='192.168.1.38',port=5000,use_reloader=False)


# In[ ]:




