from wtforms import Form, StringField, validators

class TextForm(Form):
	# Singular field with a validation check to confirm at least one character is provided
    text = StringField('Please add text below and click submit to display the amount of words in the provided text', [validators.Length(min=1)])


