from datetime import date
from urllib import request
from flask import Flask, render_template, request, url_for
import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails = {}

@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = datetime.datetime.today()
    print(currentDate)
    return render_template('index.html', currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']
    if number:
        try:
            number = int(number)
            if number % 2 == 0:
                display = str(number) + " is even"
            else:
                display = str(number) + " is odd"
        except:
            display = "Provided input is not an integer"
    else:
        display = "No number provided"

    # Write your to code here to check whether number is even or odd and render result.html page
    return render_template('result.html', display=display)


@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    # Append this value to studentOrganisationDetails
    studentOrg = request.form['organisation']
    studentOrganisationDetails[studentName] = studentOrg
    # Display studentDetails.html with all students and organisations
    return render_template('StudentDetails.html', studentOrganisationDetails=studentOrganisationDetails)
#if __name__ == "__main__":
#    app.run(debug=True)#Whenever you launch into production environment, set to False