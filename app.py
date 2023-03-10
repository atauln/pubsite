from flask import Flask, render_template, send_from_directory
import os

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

@app.route('/skills')
def technologies():
    return render_template('skills.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')
