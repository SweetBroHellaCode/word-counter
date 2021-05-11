from flask import Flask, request, render_template, session, redirect
from flask_bootstrap import Bootstrap
from components.textform import TextForm
import numpy as np
import pandas as pd

# Create the Flask application and set the location for templates
app = Flask(__name__, template_folder='./templates')
# Add Bootstrap for initial styling
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def text_form_word_count():
    form = TextForm(request.form)
	# Confirm that if the form is sent via POST that it also is validated before processing
    if request.method == 'POST' and form.validate():
		# Create a Dataframe to hold the split submitted text into a singular column
        df = pd.DataFrame(form.text.data.split())
		# Return the size of the Dataframe to reveal the number of words submitted 
        return str(df.size)
	# When receiving GET requests serve the word count form
    return render_template('form.html', form=form)
	
if __name__ == '__main__':
    app.run(host='0.0.0.0')
	