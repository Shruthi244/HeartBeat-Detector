#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
    return"Welcoming you all to this interesting application"

if __name__=='__main__':
    app.run()

