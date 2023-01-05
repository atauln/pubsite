from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/technologies')
def technologies():
    return render_template('technologies.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')
