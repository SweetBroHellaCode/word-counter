from wtforms import Form, StringField, validators

class TextForm(Form):
    text = StringField('Text', [validators.Length(min=1)])


