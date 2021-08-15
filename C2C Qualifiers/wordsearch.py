#!/usr/bin/python3

from pwn import *

class LetterClass:
	def __init__(self,x,y,letter):
		self.x = x
		self.y = y
		self.letter = letter


def getSurroundingLetters(inLetterObj,letterObjs):
	results = []
	for letterObj in letterObjs:
		if (letterObj.x == inLetterObj.x + 1 or letterObj.x == inLetterObj.x -1 or letterObj.x == inLetterObj.x) and (letterObj.y == inLetterObj.y + 1 or letterObj.y == inLetterObj.y -1 or letterObj.y == inLetterObj.y):
			results.append(letterObj)
	return results
	
	
def CheckLetterObjsToWord(word,letterObjs):
	foundLetters = ""
	for letterobj in letterObjs:
		foundLetters += letterobj.letter
	print(foundLetters)
	if foundLetters == word:
		return True
	else:
		return False
				
def TryHorizontal(wordAsList, startPosition, letterobjs,word):
	print("trying horizontal")
	result = []
	result.append(startPosition)
	nextObject = startPosition
	for letter in wordAsList:
		for letterobj in letterobjs:
			if letterobj.x == nextObject.x + 1 and letterobj.y == nextObject.y:
				nextObject = letterobj				
				break
		if nextObject == None:
			ret = []
			return ret
		if nextObject.letter == letter:
			result.append(nextObject)
	if CheckLetterObjsToWord(word,result):
		return result
	else:
		ret = []
		return ret
	

def TryNegHorizontal(wordAsList, startPosition, letterobjs,word):
	print("trying neg horizontal")
	result = []
	result.append(startPosition)
	nextObject = startPosition
	for letter in wordAsList:
		for letterobj in letterobjs:
			if letterobj.x == nextObject.x - 1 and letterobj.y == nextObject.y:
				nextObject = letterobj
				break
		if nextObject == None:
			ret = []
			return ret
		if nextObject.letter == letter:
			result.append(nextObject)
	if CheckLetterObjsToWord(word,result):
		return result
	else:
		ret = []
		return ret


def TryVertical(wordAsList, startPosition, letterobjs,word):
	print("trying vertical")
	result = []
	result.append(startPosition)
	nextObject = startPosition
	for letter in wordAsList:
		for letterobj in letterobjs:
			if letterobj.y == nextObject.y + 1 and letterobj.x == nextObject.x:
				nextObject = letterobj
				break
		if nextObject == None:
			ret = []
			return ret
		if nextObject.letter == letter:
			result.append(nextObject)
	if CheckLetterObjsToWord(word,result):
		return result
	else:
		ret = []
		return ret

def TryNegVertical(wordAsList, startPosition, letterobjs,word):
	print("trying neg vertical")
	result = []
	result.append(startPosition)
	nextObject = startPosition
	for letter in wordAsList:
		for letterobj in letterobjs:
			if letterobj.y == nextObject.y - 1 and letterobj.x == nextObject.x:
				nextObject = letterobj
				break
		if nextObject == None:
			ret = []
			return ret
		if nextObject.letter == letter:
			result.append(nextObject)
	if CheckLetterObjsToWord(word,result):
		return result
	else:
		ret = []
		return ret
		
def TryUpRight(wordAsList, startPosition, letterobjs,word):
	print("trying up right")
	result = []
	result.append(startPosition)
	nextObject = startPosition
	for letter in wordAsList:
		for letterobj in letterobjs:
			if letterobj.y == nextObject.y + 1 and letterobj.x == nextObject.x + 1:
				nextObject = letterobj
				break
		if nextObject == None:
			ret = []
			return ret
		if nextObject.letter == letter:
			result.append(nextObject)
	if CheckLetterObjsToWord(word,result):
		return result
	else:
		ret = []
		return ret
		
def TryUpLeft(wordAsList, startPosition, letterobjs,word):
	print("trying up left")
	result = []
	result.append(startPosition)
	nextObject = startPosition
	for letter in wordAsList:
		for letterobj in letterobjs:
			if letterobj.y == nextObject.y + 1 and letterobj.x == nextObject.x - 1:
				nextObject = letterobj
				break
		if nextObject == None:
			ret = []
			return ret
		if nextObject.letter == letter:
			result.append(nextObject)
	if CheckLetterObjsToWord(word,result):
		return result
	else:
		ret = []
		return ret
		
def TryDownLeft(wordAsList, startPosition, letterobjs,word):
	print("trying down left")
	result = []
	result.append(startPosition)
	nextObject = startPosition
	for letter in wordAsList:
		for letterobj in letterobjs:
			if letterobj.y == nextObject.y - 1 and letterobj.x == nextObject.x - 1:
				nextObject = letterobj
				break
		if nextObject == None:
			ret = []
			return ret
		if nextObject.letter == letter:
			result.append(nextObject)
	if CheckLetterObjsToWord(word,result):
		return result
	else:
		ret = []
		return ret

def TryDownRight(wordAsList, startPosition, letterobjs,word):
	print("trying down right")
	result = []
	result.append(startPosition)
	nextObject = startPosition
	for letter in wordAsList:
		for letterobj in letterobjs:
			if letterobj.y == nextObject.y - 1 and letterobj.x == nextObject.x + 1:
				nextObject = letterobj
				break
		if nextObject == None:
			ret = []
			return ret
		print(nextObject.letter)
		if nextObject.letter == letter:
			result.append(nextObject)
	if CheckLetterObjsToWord(word,result):
		return result
	else:
		ret = []
		return ret
	
	
	
#script start
		
r = remote("word-search.ctf.fifthdoma.in",4243)

while(True):


	r.recvuntil("Remaining words:\n")

	recv = str(r.recvuntil("  0"))
	wordlist = recv.split("\\n")
	if len(wordlist) == 1:
		print(str(r.recvall()))
		break
	wordlist.pop()
	wordlist[0] = wordlist[0].replace("'b","")
	wordlist[0] = wordlist[0].replace("'","")
	wordlist[-1] = wordlist[-1].replace("'","")
	if len(wordlist) == 1:
		wordlist[0] = wordlist[0].replace("b","")
	print(wordlist)

	#receive until after first line of index
	letterobjs = []

	recv = str(r.recvuntil("\n"))
	for i in range(0,15,1):
		recv = str(r.recvuntil("\n",drop=True))
		print(recv)
		letterlist = recv.split("  ")
		letterlist[0] = letterlist[0][-1]
		#letterlist.pop(0)
		j=0
		for inletter in letterlist:
			inletter = inletter.replace("'b","")
			inletter = inletter.replace("'","")
			letterobjs.append(LetterClass(j,i,inletter))
			j=j+1

	for letterobj in letterobjs:
		print("%s %s %s" %(letterobj.x,letterobj.y,letterobj.letter))

	breakme = False;
	goodResult = []
	for word in wordlist:
		print("attempting to find word:")
		print(word)
		startPositions = []
		wordAsList = list(word)
		firstLetter = wordAsList.pop(0)
		for letterobj in letterobjs:
			if letterobj.letter == firstLetter:
				startPositions.append(letterobj)
		startPositionResults = []
		for startPosition in startPositions:
			
			print(wordAsList)			
			
			horizontalTry = TryHorizontal(wordAsList, startPosition, letterobjs,word)
			
			if len(horizontalTry) > 0:
				goodResult = horizontalTry	
				break
				
				
			horizontalNegTry = TryNegHorizontal(wordAsList, startPosition, letterobjs,word)
			
			if len(horizontalNegTry) > 0:
				goodResult = horizontalNegTry	
				break
				
				
			verticalTry = TryVertical(wordAsList, startPosition, letterobjs,word)
			
			if len(verticalTry) > 0:
				goodResult = verticalTry	
				break
				
			verticalNegTry = TryNegVertical(wordAsList, startPosition, letterobjs,word)
			
			if len(verticalNegTry) > 0:
				goodResult = verticalNegTry	
				break
				
				
			upRightTry = TryUpRight(wordAsList, startPosition, letterobjs,word)
			
			if len(upRightTry) > 0:
				goodResult = upRightTry	
				break
				
				
			upLeftTry = TryUpLeft(wordAsList, startPosition, letterobjs,word)
			
			if len(upLeftTry) > 0:
				goodResult = upLeftTry				
				break
				
				
			downLeftTry = TryDownLeft(wordAsList, startPosition, letterobjs,word)
			
			if len(downLeftTry) > 0:
				goodResult = downLeftTry	
				break
				
				
			downRightTry = TryDownRight(wordAsList, startPosition, letterobjs,word)
			
			if len(downRightTry) > 0:
				goodResult = downRightTry	
				break
				
					
		if len(goodResult) > 0:
			break	

				
			
	print("in successville")
	positionResult = ""
	for position in goodResult:
		positionResult += position.letter
	print(positionResult)
	print(word)
	if positionResult == word:
		print(word)
		print(positionResult)
		r.recvuntil("ow 1 column 2",drop=True)
		print("%s, %s\n" %(goodResult[0].y,goodResult[0].x))
		r.send("%s, %s\n" %(goodResult[0].y,goodResult[0].x))
		r.recvuntil("Input end coordinate of word, e.g: 3, 4 for row 3 column 4",drop=True)
		print("%s, %s\n" %(goodResult[-1].y,goodResult[-1].x))
		r.send("%s, %s\n" %(goodResult[-1].y,goodResult[-1].x))
		print("an iteration is complete-----------------------------------------------------------------------------")
		print(str(r.readline()))
		print(str(r.readline()))
		print(str(r.readline()))
		
			
			