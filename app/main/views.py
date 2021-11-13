from flask import render_template,request
from . import main
@main.route('/')
def index():
    '''
    view root page function that returns the index page and its data
    '''
    return render_template('main/index.html')
