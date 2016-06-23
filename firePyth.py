
from firebase import firebase
import enchant
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

firebase = firebase.FirebaseApplication('YOUR-FIREBASE-URL', None)

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
def getMyResp(p):
	keys  = eval(getResp("Keys"))
	for item in keys:
		if item in p:
			arrR = eval(getResp(item))
			resP = arrR[random.randint(0, len(arrR)-1)]
			b = "(ME)"+resP[1:]
			conv.append(b)
			return;
	if "?" in p:
		b = "(ME)Good Question that I don't know the answer to ;)"
		conv.append(b)
		return;
	print "1"
	if getResp(p) != None:
			arrR = eval(getResp(p))
			resP = arrR[random.randint(0, len(arrR)-1)]
			b = "(ME)"+resP[1:]
			conv.append(b)
			return;
	print "2"
	s = p.split(' ')
	for item in s:
		if getResp(item) != None:
			if getResp(item).startswith('C'):
				arrR = eval(getResp(item))
				resP = arrR[random.randint(0, len(arrR)-1)]
				b = "(ME)"+resP[1:]
				conv.append(b)
				return;
	print s
	if '?' in p:
		b = "(ME) Good Question That I don't know the answer to"
		conv.append(b)
		return;
	print "3"
	d = enchant.Dict("en_US")
	print "4"
	for item in s:
		if d.check(item) == False:
			arrSug = d.suggest(item)
			stringA = "("
			count = 0
			for sug in arrSug:
				if count == 0:
					stringA = stringA +sug
				else:
					stringA = stringA+","+sug
				count = count+1
			stringA = stringA +')'
			b = "(ME)"+"I didn't understand '"+item+"' try one of the following: "+stringA
			conv.append(b)
			return;
	print "5"
	rA = getRandR()
	b = "(ME)"+rA[random.randint(0, len(rA)-1)]
	print b
	conv.append(b)
	return;


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


