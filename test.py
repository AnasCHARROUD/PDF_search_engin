#!/usr/bin/env python
# coding: utf-8

# In[1]:



from io import StringIO
import os
import pandas as pd
import numpy as np
import ast 
from tqdm import tqdm


# In[2]:


def search_contents(query,dictt):
    page_content=0
    h=[]
    try:
        page_content =dictt[query]
    except:
        dicttt = list(dictt)
        for item in dicttt:
            if(query in item):
                h.append(dictt[item])
    if(page_content==0):
        return h
    else:
        return page_content
        


# In[3]:


def principle_function(query,data):
    list_of_condidate = []
    for i in tqdm(range(len(data))):
        end_page_contents = data.iloc[i][2]
        contents = data.iloc[i][1]
        pdf_name = data.iloc[i][0]
        contents = ast.literal_eval(contents)
        if(None in list(contents)):
            contents.pop(None)
        result=search_contents(query,contents)
        exact_page = 0
        if(type(result)==list):
            if(len(result)>0):
                if(result[0]<contents[list(contents)[-1]]):
                    exact_page = end_page_contents+result[0]
                
        else:
            if(result<contents[list(contents)[-1]]):
                exact_page = end_page_contents+result
        if(exact_page!=0):
            pdf_information = {}
            pdf_information.update({'name':query})
            pdf_information.update({'path':pdf_name})
            pdf_information.update({'where_in_pdf':exact_page})
            list_of_condidate.append(pdf_information)
    return list_of_condidate







