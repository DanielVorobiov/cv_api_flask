from flask import Flask
import click
from flask.cli import with_appcontext

from cv_data import cv_data

app = Flask(__name__)

about_value = cv_data['about']
experience_value = cv_data['experience']
education_value = cv_data['education']
volunteering_value = cv_data['volunteering']
contacts_value = cv_data['contacts']
soft_skills_value = cv_data['soft-skills']
technical_skills_value = cv_data['technical-skills']
languages_value = cv_data['languages']
awards_value = cv_data['awards']
hobbies_value = cv_data['hobbies']


@app.route('/', methods=['GET'])
def index():
    return 'Hi, this is my CV!'


@app.route('/about/', methods=['GET'])
def about():
    return {'value': about_value}


@app.route('/experience/', methods=['GET'])
def experience():
    return {'value': experience_value}


@app.route('/education/', methods=['GET'])
def education():
    return {'value': education_value}


@ app.route('/volunteering/', methods=['GET'])
def volunteering():
    return {'value': volunteering_value}


@ app.route('/contacts/', methods=['GET'])
def contacts():
    return {'value': contacts_value}


@ app.route('/soft-skills/', methods=['GET'])
def soft_skills():
    return {'value': soft_skills_value}


@ app.route('/technical-skills/', methods=['GET'])
def technical_skills():
    return {'value': technical_skills_value}


@ app.route('/languages/', methods=['GET'])
def languages():
    return {'value': languages_value}


@ app.route('/awards/', methods=['GET'])
def awards():
    return {'value': awards_value}


@ app.route('/hobbies/', methods=['GET'])
def hobbies():
    return {'value': hobbies_value}


@ app.cli.command(name='about')
def about_command():
    print(about_value)


@ app.cli.command(name='experience')
def experience_command():
    print(experience_value)


@ app.cli.command(name='education')
def education_command():
    print(education_value)


@ app.cli.command(name='volunteering')
def volunteering_command():
    print(volunteering_value)


@ app.cli.command(name='contacts')
def contacts_command():
    print(contacts_value)


@ app.cli.command(name='soft-skills')
def soft_skills_command():
    print(soft_skills_value)


@ app.cli.command(name='technical-skills')
def technical_skills_command():
    print(technical_skills_value)


@ app.cli.command(name='languages')
def languages_command():
    print(languages_value)


@ app.cli.command(name='awards')
def awards_command():
    print(awards_value)


@ app.cli.command(name='hobbies')
def hobbies_command():
    print(hobbies_value)


if __name__ == '__main__':
    app.run(debug=True)
