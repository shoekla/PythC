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
	url = "abirshukla.pythonanywhere.com/pythEmail/PythC Password/"+str(password)+"/"+str(email)+"/"
	print url
	source_code=requests.get(url)
	plain_text=source_code.text
	soup=BeautifulSoup(plain_text)
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
	userData.append([])
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



