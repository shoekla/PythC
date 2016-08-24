
from firebase import firebase
import random
import urllib2
import re
import nltk
import csv
import time
import requests
import string
from bs4 import BeautifulSoup
from urllib2 import urlopen
import os

firebase = firebase.FirebaseApplication('https://pythc.firebaseio.com/', None)

def getMe():
	return conv
def putInFirebase(phrase,response):
	phrase = phrase.strip()
	if getResp(phrase) == None:
		firebase.post(phrase,response)
		keys = eval(getResp("Keys"))
		keys.append(phrase)
		firebase.delete("Keys",None)
		firebase.post("Keys",str(keys))
		incrementN()
		return 1
	else:
		print "Already In system"
		return 0
def addToConvYou(phrase):
	w = phrase.lower()
	phrase = "(YOU)"+phrase
	conv.append(phrase)
	print "YYYYYys"
	getMyResp(w)
def getRandR():
	arr = eval(getResp('randomR'))
	return arr
def addToRand(phrase):
	arr = eval(getResp('randomR'))
	if phrase not in arr:
		arr.append(phrase)
		firebase.delete('randomR',None)
		firebase.post('randomR',str(arr))
		return 'green'
	return 'red'

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

def getRespArr(phrase):
	a = firebase.get(phrase,None)
	if a == None:
		return None
	keys = []
	for key in a:
		"""
		print "key: %s , value: %s" % (key, a[key])
		"""
		keys.append(key)
	return eval(a[keys[0]])
def getKey(phrase):
	a = firebase.get(phrase,None)
	if a == None:
		return None
	keys = []
	for key in a:
		"""
		print "key: %s , value: %s" % (key, a[key])
		"""
		keys.append(key)
	return keys[0]
def incrementN():
	a = firebase.get("NumOfPhrases",None)
	print a
	keys = []
	count = 0
	for key in a:
		"""
		print "key: %s , value: %s" % (key, a[key])
		"""
		keys.append(key)
		count = count +1
	i = int(a[keys[count-1]])
	i = i+1
	firebase.delete('NumOfPhrases',None)
	firebase.post("NumOfPhrases",str(i))
def getRandLen():
	arr = eval(getResp('randomR'))
	return len(arr)
def getGoodLink(url):
	k = url.rfind("/")
	return url[:k+1]
def crawlYouTube(url,pages):
	print "Crawl Start"
	try:
		arr=[]
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('a'):

			href=link.get('href')
			href_test=str(href)
			if href_test.startswith("http"):
					pages.append(str(href))
			else:
				lin=getGoodLink(url)
				pages.append(lin+str(href))

	except:
		print "Error at: "+str(url)
def deleteDuplicates(lis):
	newLis=[]
	for item in lis:
		if item not in newLis:
			newLis.append(item)
	return newLis

def getVids(movie):
	movie = "python "+movie
	movie = movie.replace(" ","+")
	link = "https://www.youtube.com/results?search_query="+movie
	return getVideoSearch(link)
def getVideoSearch(url):
	a = []
	crawlYouTube(url,a)
	b=[]
	c=[]
	print "Close"
	for item in a:
		if "/watch" in item:
			b.append(item)
	for item in b:
		c.append(str(item[33:]))
	new=deleteDuplicates(c)
	resAct = []
	for item in new:
		if "list=" not in item:
			resAct.append(item)
	return resAct
def getPreCode(phrase):
	phrase = phrase +" preCode"
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
def getExCode(phrase):
	phrase = phrase +" exCode"
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
def putPreCode(name,c):
	name = name + " preCode"
	putInFirebase(name,c)

def putExCode(name,c):
	name = name + " exCode"
	putInFirebase(name,c)
def getUserCont():
	arr = getRespArr("Keys")
	res = []
	for item in arr:
		if "exCode" not in item and "preCode" not in item:
			res.append(item)
	return res
def getSummary(key):
	a = getRespArr(key)
	return a[0]
def addUser(userName,password):
	userName = userName.strip()
	if getResp(userName) == None:
		firstArray = [userName,password,0,[]]
		firebase.post(userName,str(firstArray))
		users = eval(getResp("Users"))
		users.append(userName)
		firebase.delete("Users",None)
		firebase.post("Users",str(users))
		incrementN()
		return 1
	else:
		print "Already In system"
		return 0
def getUsers():
	return getResp("Users")
#addUser("Abir","aadi2247")


