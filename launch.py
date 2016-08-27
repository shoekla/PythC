from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
import time
import compileA
import os
import firePyth
import scrape
app = Flask(__name__)

@app.route('/')
def goToLogin():
	return redirect("/login/")
@app.route("/res/")
def compilerPlain():
	return redirect("/login/")
	#return render_template('pyth/home.html')

@app.route('/login/')
def loginUser():
	return render_template("pyth/login.html")
@app.route('/create/')
def CreateUser():
	return render_template("pyth/createAccount.html")

@app.route('/forgotPass/')
def emailUser():
	return render_template("pyth/emailPass.html")
@app.route('/emailPassForUser/',methods=['POST'])
def emailPassUser(email=None,passW=None):
	print "Sign"
	email = None
	passW = None
	email = ""
	passW = ""
	email = request.form['email']
	email = email.strip()
	passW = scrape.getPass(email)
	if passW == "":
		return render_template("pyth/emailPass.html",mess="Email not found :(")
	else:
		print "Sending mail"
		scrape.sendEmailForPass(passW,email)
		print "Ok"
		return render_template("pyth/login.html",mess="Email sent with Password")

@app.route('/addPythCUser/',methods=['POST'])
def createPythUSer(email = None,passW = None):
	print "Sign"
	email = None
	passW = None
	email = ""
	passW = ""
	email = request.form['email']
	email = email.strip()
	passW = request.form['passW']
	passW = passW.strip()
	print "Sign2"
	if scrape.isGood(email):
		print "is Godd"
		return render_template("pyth/createAccount.html",mess="Email already In System :(")
	else:
		print "isdsjf"
		scrape.addUser(email,passW)
		return render_template("pyth/login.html",mess="You Were added! Please Sign in")

@app.route('/loginPythCUSer/',methods=['POST'])
def loginPythoUser(email=None,passW=None):
	print "Sign"
	email = None
	passW = None
	email = ""
	passW = ""
	email = request.form['email']
	email = email.strip()
	passW = request.form['passW']
	passW = passW.strip()
	print "Sign2"
	if scrape.loginUser(email,passW):
		return render_template('pyth/home.html',email=email)
	else:
		return render_template("pyth/login.html",mess="Invalid Login Credentials")


@app.route('/res/setMenu/')
def my_formPythRasdasESdd():
	return redirect("/login/")
	#return render_template('pyth/setMenu.html')

@app.route('/load/<lessonName>/')
def my_formPythRLeLoadssond(lessonName):
	return redirect("/login/")
	#return render_template('pyth/loading.html',lessonName = lessonName)

@app.route('/res/succ/<less>')
def succLPythesson(less):
	return redirect("/login/")
	print "enter"
	return render_template("pyth/succ.html",less=less)
@app.route('/res/userCont/')
def userCoPythnt(names = [], sumSL = []):
	return redirect("/login/")
	names = []
	names = firePyth.getUserCont()
	sumSL = []
	for item in names:
		sumSL.append(firePyth.getSummary(item))
	return render_template("pyth/userCont.html",names = names, sumSL=sumSL)



@app.route('/backToRes/',methods=['POST'])
def resBack(email = None):
	email = None
	email = request.form['email']
	return render_template('pyth/home.html',email=email)

@app.route('/setLess/',methods=['POST'])
def my_forsetMenu(email = None):
	email = None
	email = request.form['email']
	return render_template('pyth/setMenu.html',email = email)

@app.route('/userLess/',methods=['POST'])
def userLessonCOntent(names = [], sumSL = [],email = None):
	email = None
	email = request.form['email']
	names = []
	names = firePyth.getUserCont()
	sumSL = []
	for item in names:
		sumSL.append(firePyth.getSummary(item))
	return render_template("pyth/userCont.html",names = names, sumSL=sumSL,email=email)
@app.route('/res/', methods=['POST'])
def my_formPyth_postsdfsDDD(code=None,exCode=None,startTime=None,timeA=None,email = None):
	email = None
	email = request.form['email']
	exCode=""
	code=""
	code = request.form['code']
	startTime=time.time()
	exCode=compileA.com(code)
	if len(str(exCode))==0:
		try:     
			exec code
		except Exception as e: 
			exCode = e
	
	timeA = time.time() - startTime
	return render_template('pyth/res.html',exCode=exCode,timeA=timeA,code=code,email=email)
@app.route('/loginRes/',methods=['POST'])
def loginCompile(code = None,exCode = None):
	code = None
	code = ""
	code = request.form['code']
	exCode = None
	exCode = ""
	exCode=compileA.com(code)
	return render_template("pyth/login.html",mess="You're Coding Already!",exCode =exCode,code = code)
@app.route('/lesson/<lessonName>/',methods=['POST'])
def my_formRLessonPythdasESdd(lessonName, lessonDetails = [],helpV = [],lengthO = None,Precode = None,email = None):
	email = None
	email = request.form['email']
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
	print "Precode: "+str(Precode)
	if Precode == None:
		Precode = ""
	lengthO = len(helpV)
	return render_template('pyth/lesson.html',lessonName = lessonName,lessonDetails = lessonDetails,helpV=helpV,lengthO = lengthO,Precode = Precode,email=email)

@app.route('/res/lesson/grade/<lessonName>/', methods=['POST'])
def gradeCodeLesson(lessonName, lessonDetails = [],helpV = [],lengthO = None,Precode = None,code=None,exCode=None,section=None,gradeCode = None, message = None,email = None,award = None):
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
	print "22222"
	gradeCode = firePyth.getExCode(lessonName)
	gradeCode = gradeCode.strip()
	print "Before If"
	email = None
	email = request.form['email']
	if gradeCode == exCode:
		print "Inside"
		award = None
		award = scrape.completeLess(lessonName,email)
		print "Returning"
		return render_template("pyth/succ.html",less=lessonName,email = email,award = award)
	message = ""
	message = "Your code is not quite right"
	return render_template('pyth/lessonRes.html',lessonName = lessonName,lessonDetails = lessonDetails,helpV=helpV,lengthO = lengthO,exCode=exCode,code=code,section=section, message = message,email = email)
@app.route("/userProfile/",methods=['POST'])
def userProf(email = None,userData = [],points = None,pointMess = None,sumSL = [],name = None,nick = None,summary = None,pic = None,lessons = []):
	email = None 
	email = request.form['email']
	userData = []
	userData = scrape.getUserData(email)
	print userData
	points = None
	points = 0
	print "2"
	points = len(userData[0]) * 10
	pointMess = None
	pointMess = ""
	pointMess = str(points)
	sumSL = []
	print "4"
	for item in userData[0]:
		sumSL.append(firePyth.getSummary(item))
	print "5"
	name = None
	name = ""
	nick = None 
	nick = ""
	summary = None
	summary = ""
	pic = None 
	lessons = []

	name = userData[1][0]
	print name
	nick=userData[1][1]
	print nick
	summary = userData[1][2]
	print summary
	pic = userData[1][3]
	print pic
	lessons=userData[0]
	print lessons
	print "6"
	return render_template("pyth/userProf.html",email = email,pointMess = pointMess,name = name,nick = nick,summary = summary,pic = pic,lessons = lessons,sumSL=sumSL)


@app.route('/soon/',methods=['POST'])
def comicngsoonguys(email = None):
	email = None
	email = request.form['email']
	return render_template("pyth/soon.html",email = email)
@app.route('/edit/',methods = ['POST'])
def edit(email = None,nick = None,summary = None,pic = None):
	email = None
	email = request.form['email']
	name = None
	name = ""
	name = request.form['name']
	nick = None 
	nick = ""
	nick = request.form['nick']
	summary = None
	summary = ""
	summary = request.form['summary']
	pic = None 
	pic = request.form['pic']
	return render_template("pyth/edit.html",name = name,nick = nick,summary = summary,pic = pic,email=email)
@app.route('/submitEditLesson/',methods=['POST'])
def subitedit(email = None,nick = None,summary = None,pic = None,points = None,pointMess = None,lessons = [],sumSL = [],userData = []):
	email = None
	email = request.form['email']
	name = None
	name = ""
	name = request.form['name']
	nick = None 
	nick = ""
	nick = request.form['nick']
	summary = None
	summary = ""
	summary = request.form['summary']
	pic = None 
	pic = request.form['pic']
	scrape.editUserData(name,nick,summary,pic,email)
	userData = []
	userData = scrape.getUserData(email)
	lessons = []
	lessons = userData[0]
	print userData
	points = None
	points = 0
	print "2"
	points = len(lessons) * 10
	pointMess = None
	pointMess = ""
	pointMess = str(points)
	sumSL = []
	print "4"
	for item in userData[0]:
		sumSL.append(firePyth.getSummary(item))
	return render_template("pyth/userProf.html",email = email,pointMess = pointMess,name = name,nick = nick,summary = summary,pic = pic,lessons = lessons,sumSL=sumSL)
@app.route('/sure/',methods = ['POST'])
def forSure(email = None):
	email = None
	email = ""
	email = request.form['email']
	return render_template("pyth/forsure.html",email = email)
@app.route('/deleteAccount/',methods=['POST'])
def deleteAccount(email = None,mess = None):
	email = None
	email = ""
	email = request.form['email']
	mess = None
	mess = ""
	mess = scrape.deleteA(email)
	return render_template("pyth/login.html",mess=mess)
@app.route('/res/addLesson/',methods=["POST"])
def addLOythess(email = None):
	email = None
	email = request.form['email']
	return render_template("pyth/add.html",email =email)
@app.route('/res/addLessonSubmit/', methods=['POST'])
def addLPythesonPost(name = None, lesson = None, project = None, summary = None, array = [], preCode = None, exCode = None,message =None,ex = None,email = None):
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
	print "Summary: "+summary
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
		return render_template("pyth/add.html",message=message,name = name,lesson = lesson,summary = summary,preCode =preCode,exCode =exCode,project=project)
	if (name == "" or lesson =="" or project =="" or summary =="" or exCode == ""):
		message = ""
		message = "Please fill all fields"
		return render_template("pyth/add.html",message=message,name = name,lesson = lesson,summary = summary,preCode =preCode,exCode =exCode,project = project)
	array = []
	array = [summary,lesson,project]
	if firePyth.putInFirebase(name,str(array)) == 1:
		firePyth.putExCode(name,exCode)
		firePyth.putPreCode(name,preCode)
	else:
		message = ""
		message = "Lesson Name Already in system :( try different name!"
		return render_template("pyth/add.html",message=message,name = name,lesson = lesson,summary = summary,preCode =preCode,exCode =exCode,project = project)
	email = None
	email = ""
	email = request.form['email']
	scrape.completeLess(name,email)
	return render_template("pyth/succAdd.html",name=name,email = email)


if __name__ == '__main__':
    app.run()













