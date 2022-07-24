# Set Up
A virtual environment  is necessary in order to start the project. Create one in the same folder as the source code of the project using the following command:
```sh
python -m venv venv
```
Activate the environment by going to venv/Scripts and typing 'activate' in  the command line

Afterward, make sure to install the required libraries for the project using the following command from the source folder of the project:

```sh
pip install -r requirements.txt
```

To launch the project use the following command:

```sh
flask run
```
This command will start the local server on http://127.0.0.1:8000/

# Using the API

The purpose of this API is to show information about the candidate from his Curriculum Vitae. As a CV, the API separates the info based on different categories. Since the API is used only to read data, GET is the only acceptable type of request. All available categories and their endpoints are specified below.

- To get a short description of the candidate use http://127.0.0.1:5000/about/
- To get information about the working experience of the candidate use http://127.0.0.1:5000/experience/
- To get data about the educational background of the candidate use  http://127.0.0.1:5000/education/
- To get information about the candidate's volunteering activities use http://127.0.0.1:5000/volunteering/
- To get data about the soft skills that the candidate posses use: http://127.0.0.1:5000/soft-skills/
- To get data about the technical skills that the candidate posses use: http://127.0.0.1:5000/technical-skills/
- To get information about the languages the candidate can speak use: http://127.0.0.1:5000/languages/
- To get data about the awards and certifications the candidate has received, use: http://127.0.0.1:5000/awards/
- To get data about the candidate's hobbies use: http://127.0.0.1:5000/hobbies/
- To get the contact information of the candidate use: http://127.0.0.1:5000/contacts/



# CLI Commands
To print the information from a specific category it's necessary to set the flask app global environment variable. To do this on windows use:
```sh
set FLASK_APP=app
```

After setting the flask app, a set of commands becomes available to execute from the command line. Depending on the information needed to be shown in the CMD, use the command:

```sh
flask 'category name'
```
Here is the list of all available categories:
- about
- experience
- education
- volunteering
- soft-skills
- technical-skills
- languages
- awards
- hobbies
- contacts
