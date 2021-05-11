from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
from components.textform import TextForm


app = Flask(__name__, template_folder='./templates')
'''
@app.route('/')
def my_form():
    return render_template('text-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
	df = pd.DataFrame(text.split(" "))
	return str(df.size)
'''

@app.route('/', methods=['GET', 'POST'])
def register():
    form = TextForm(request.form)
    if request.method == 'POST' and form.validate():
        df = pd.DataFrame(form.text.data.split(" "))
        return str(df.size)
    return render_template('form.html', form=form)
	
if __name__ == '__main__':
    app.run(host='0.0.0.0')