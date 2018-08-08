from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/student/<int:student_id>')
def student_id(student_id):
	return render_template("student.html",student_id = student_id ) 

add_student("Alex","2019", False )


def display_student(student_id):

	return render_template("student.html",
		# student_id =  student_id,
		student= query_by_id(student_id)
		)

display_student(1)


app.run(debug=True)
