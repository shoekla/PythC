import urllib2
import re
import csv
import time
import requests
import string
from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup, SoupStrainer
import urllib2
import os
import firePyth
from firebase import firebase

firebase = firebase.FirebaseApplication('https://pythc.firebaseio.com/', None)



def is_in_arr(lis,s):
	result=False
	for item in lis:
		if item==s:
			result=True
	return result

def deleteDuplicates(lis):
	newLis=[]
	for item in lis:
		if item not in newLis:
			newLis.append(item)
	return newLis

def sendEmailForPass(password,email):
	url = "http://abirshukla.pythonanywhere.com/pythEmail/PythC%20Password/"+str(password)+"/"+str(email)+"/"
	print url
	source_code=requests.get(url)
	print "1"
	plain_text=source_code.text
	print "2"
	soup=BeautifulSoup(plain_text)
	print "Done"
	return ""
	
def getResp(phrase):
	a = firebase.get(phrase,None)
	if a == None:
		return None
	keys = []
	for key in a:
		"""
		print "key: %s , value: %s" % (key, a[key])
		"""
		keys.append(key)
	return a[keys[0]]

def addUser(email,passW):
	users = eval(getResp("Users"))
	users.append(email)
	firebase.delete('Users',None)
	firebase.post("Users",str(users))
	b = eval(getResp("passwords"))
	b.append(passW)
	firebase.delete('passwords',None)
	userData = eval(getResp("UserData"))
	userData.append([[],[str(email),"Nick Name",'This is my summary, I love to code!',"http://www.priorlakeassociation.org/wp-content/uploads/2011/06/blank-profile.png","show"]])
	firebase.delete("UserData",None)
	firebase.post("UserData",str(userData))
	firebase.post("passwords",str(b))
def isGood(user):
	users = eval(getResp("Users"))
	return user in users
def loginUser(user,passW):
	print "Logging In"
	users = eval(getResp("Users"))
	b = eval(getResp("passwords"))
	for i in range(0,len(users)):
		if users[i] == user:
			if b[i] == passW:
				return True
			else:
				return False
	return False
def getPass(user):
	print "Logging In"
	users = eval(getResp("Users"))
	b = eval(getResp("passwords"))
	for i in range(0,len(users)):
		if users[i] == user:
			print "User [i] "+str(b[i])
			return b[i]
	return ""


def completeLess(lessonName,email):
	try:
		users = eval(getResp("Users"))
		userData = eval(getResp("UserData"))
		for i in range(0,len(users)):
			if users[i] == email:
				if lessonName in userData[i][0]:
					return "You already completed this lesson!"
				userData[i][0].append(lessonName)
				firebase.delete("UserData",None)
				firebase.post("UserData",str(userData))
				return "You have been awarded 10 points!"

	except:
		return "An Error Has Occured :("	
def getUserData(email):
	try:
		users = eval(getResp("Users"))
		userData = eval(getResp("UserData"))
		for i in range(0,len(users)):
			if users[i] == email:
				return userData[i]	


	except:
		return [[],[]]
def editUserData(name,nick,summary,pic,email,contact):
	try:
		users = eval(getResp("Users"))
		userData = eval(getResp("UserData"))
		for i in range(0,len(users)):
			if users[i] == email:
				print userData
				print "Change"	
				userData[i][1]=[str(name),str(nick),str(summary),str(pic),str(contact)]
				print userData
				firebase.delete("UserData",None)
				firebase.post("UserData",str(userData))
				return

	except:
		return
def deleteA(email):
	try:
		users = eval(getResp("Users"))
		userData = eval(getResp("UserData"))
		b = eval(getResp("passwords"))
		for i in range(0,len(users)):
			if users[i] == email:
				del users[i]
				del userData[i]
				del b[i]
				firebase.delete("UserData",None)
				firebase.delete('Users',None)
				firebase.post("Users",str(users))
				firebase.post("UserData",str(userData))
				firebase.delete('passwords',None)
				firebase.post("passwords",str(b))
				return "Account Deleted"

	except:
		return "Error Occured"
def getNextLesson(lesson):
	names = firePyth.getUserCont()
	print "One if"
	if lesson in names:
		for i in range(0,len(names)):
			if names[i] == lesson:
				if i < len(names)-1:
					return names[i+1]
				else:
					return "No Lesson"
	print "2 if"
	names = ["Lesson 1 Syntax and Printing","Lesson 2 Variables in Python","Lesson 3 Conditionals","Lesson 4 Control Flow","Lesson 5 Methods","Lesson 6 Data Structures","Final Project"] + names
	if lesson in names:
		for i in range(0,len(names)):
			if names[i] == lesson:
				if i < len(names)-1:
					return names[i+1]
				else:
					return "No Lesson"
	return "No Lesson"





