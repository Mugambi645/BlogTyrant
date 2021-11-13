from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ArticleForm(FlaskForm):
    title = StringField("Article Title", validators = [Required()])
    content = TextAreaField('Write your article here')
    submit = SubmitField('Submit')