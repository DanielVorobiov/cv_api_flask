from flask import Flask
import click
from flask.cli import with_appcontext

from cv_data import cv_data

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hi, this is my CV!'


@app.route('/about/', methods=['GET'])
def about():
    return {'value': cv_data['about']}


@app.route('/experience/', methods=['GET'])
def experience():
    return {'value': cv_data['experience']}


@app.route('/education/', methods=['GET'])
def education():
    return {'value': cv_data['education']}


@app.route('/volunteering/', methods=['GET'])
def volunteering():
    return {'value': cv_data['volunteering']}


@app.route('/contacts/', methods=['GET'])
def contacts():
    return {'value': cv_data['contacts']}


@app.route('/soft-skills/', methods=['GET'])
def soft_skills():
    return {'value': cv_data['soft-skills']}


@app.route('/technical-skills/', methods=['GET'])
def technical_skills():
    return {'value': cv_data['technical-skills']}


@app.route('/languages/', methods=['GET'])
def languages():
    return {'value': cv_data['languages']}


@app.route('/awards/', methods=['GET'])
def awards():
    return {'value': cv_data['awards']}


@app.route('/hobbies/', methods=['GET'])
def hobbies():
    return {'value': cv_data['hobbies']}


@app.cli.command(name='about')
def about_command():
    print(cv_data['about'])


@app.cli.command(name='experience')
def experience_command():
    print(cv_data['experience'])


@app.cli.command(name='education')
def education_command():
    print(cv_data['education'])


@app.cli.command(name='volunteering')
def volunteering_command():
    print(cv_data['volunteering'])


@app.cli.command(name='contacts')
def contacts_command():
    print(cv_data['contacts'])


@app.cli.command(name='soft-skills')
def soft_skills_command():
    print(cv_data['soft-skills'])


@app.cli.command(name='technical-skills')
def technical_skills_command():
    print(cv_data['technical-skills'])


@app.cli.command(name='languages')
def languages_command():
    print(cv_data['languages'])


@app.cli.command(name='awards')
def awards_command():
    print(cv_data['awards'])


@app.cli.command(name='hobbies')
def hobbies_command():
    print(cv_data['hobbies'])


if __name__ == '__main__':
    app.run(debug=True)
