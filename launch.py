from flask import Flask
from flask import request
from flask import render_template
import time
import compileA
import os
import firePyth
app = Flask(__name__)

@app.route("/res/")
def compilerPlain():
	return render_template('pyth/home.html')



@app.route('/res/', methods=['POST'])
def my_formPyth_postsdfsDDD(code=None,exCode=None,startTime=None,timeA=None):
	exCode=""
	code=""
	code = request.form['code']
	exCode=compileA.com(code)
	if len(str(exCode))==0:
		try:     
			exec code
		except Exception as e: 
			exCode = e
	startTime=time.time()
	timeA = time.time() - startTime
	return render_template('pyth/res.html',exCode=exCode,timeA=timeA,code=code)

@app.route('/res/setMenu/')
def my_formPythRasdasESdd():
	return render_template('pyth/setMenu.html')

@app.route('/load/<lessonName>/')
def my_formPythRLeLoadssond(lessonName):
	return render_template('pyth/loading.html',lessonName = lessonName)

@app.route('/lesson/<lessonName>/')
def my_formRLessonPythdasESdd(lessonName, lessonDetails = [],helpV = [],lengthO = None,Precode = None):
	lessonDetails = []
	lessonDetails = firePyth.getRespArr(lessonName)
	helpV = []
	print "Almost"
	print "Lesson Name: "+lessonName
	if lessonName == "Final Project":
		print "if"
		helpV = firePyth.getVids("Rock Paper Scissors in Python")
	else:
		print "else"
		helpV = firePyth.getVids(lessonName)
	print "Yo"
	lengthO = 0
	Precode = """ """
	Precode = firePyth.getPreCode(lessonName)
	if Precode == None:
		Precode = ""
	lengthO = len(helpV)
	return render_template('pyth/lesson.html',lessonName = lessonName,lessonDetails = lessonDetails,helpV=helpV,lengthO = lengthO,Precode = Precode)
@app.route('/res/succ/<less>')
def succLPythesson(less):
	print "enter"
	return render_template("pyth/succ.html",less=less)
@app.route('/res/userCont/')
def userCoPythnt(names = [], sumSL = []):
	names = []
	names = firePyth.getUserCont()
	sumSL = []
	for item in names:
		sumSL.append(firePyth.getSummary(item))
	return render_template("pyth/userCont.html",names = names, sumSL=sumSL)
@app.route('/res/addLesson')
def addLOythess():
	return render_template("pyth/add.html")
@app.route('/res/addLesson/', methods=['POST'])
def addLPythesonPost(name = None, lesson = None, project = None, summary = None, array = [], preCode = None, exCode = None,message =None,ex = None):
	name = ""
	name = request.form['name']
	print "Name: "+name
	lesson = ""
	lesson = request.form['lesson']
	print "lesson: "+lesson
	project = ""
	project = request.form['project']
	summary = ""
	summary = request.form['summary']
	print "SUmmary: "+summary
	preCode = """ """
	preCode = request.form['preCode']
	print "Precode: "+preCode
	exCode = """ """
	exCode = request.form['exCode']
	print "Excode: "+exCode
	ex = ""
	ex = request.form['ex']
	if ex == None or ex == "":
		ex = ""
	print "ex: "+ex
	print "If"
	if ex == "code":
		exCode=compileA.com(exCode)
		if len(str(exCode))==0:
			try:     
				exec code
			except Exception as e: 
				exCode = e
	print "COnt"
	if "exCode" in name or "preCode" in name:
		message = ""
		message = "'Excode or 'preCode' can not be in Lesson Name"
		return render_template("pyth/add.html",message=message)
	if (name == "" or lesson =="" or project =="" or summary =="" or exCode == ""):
		message = ""
		message = "Please fill all fields"
		return render_template("pyth/add.html",message=message)
	array = []
	array = [summary,lesson,project]
	if firePyth.putInFirebase(name,str(array)) == 1:
		firePyth.putExCode(name,exCode)
		firePyth.putPreCode(name,preCode)
	else:
		message = ""
		message = "Lesson Name Already in system :( try different name!"
		return render_template("pyth/add.html",message=message)
	return render_template("pyth/succAdd.html",name=name)
@app.route('/res/lesson/grade/<lessonName>', methods=['POST'])
def gradeCodeLesson(lessonName, lessonDetails = [],helpV = [],lengthO = None,Precode = None,code=None,exCode=None,section=None,gradeCode = None, message = None):
	lessonDetails = []
	lessonDetails = firePyth.getRespArr(lessonName)
	helpV = []
	print "Almost"
	helpV = firePyth.getVids(lessonName)
	print "Yo"
	lengthO = 0
	code = """ """
	code = """
nameVar = 0
age = 18"""
	lengthO = len(helpV)
	exCode=""" """
	code=""
	code = request.form['code']
	exCode=compileA.com(code)
	if len(str(exCode))==0:
		try:     
			exec code
		except Exception as e: 
			exCode = e
	section = ""
	section = "sec"
	exCode = exCode.strip()
	gradeCode = firePyth.getExCode(lessonName)
	gradeCode = gradeCode.strip()
	if gradeCode == exCode:
		return render_template("pyth/succ.html",less=lessonName)
	message = ""
	message = "Your code is not quite right"
	return render_template('pyth/lessonRes.html',lessonName = lessonName,lessonDetails = lessonDetails,helpV=helpV,lengthO = lengthO,exCode=exCode,code=code,section=section, message = message)








if __name__ == '__main__':
    app.run()













