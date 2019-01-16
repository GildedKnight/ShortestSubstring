import array
import time

def getShortestUniqueSubstring(arr,str):
	headIndex = 0
	result = ""
	uniqueCounter = 0
	countMap = Map()

	# Initialize countMap
	for i in range(len(arr)):
		countMap.setValueOf(arr[i],0)

	#scan string
	for tailIndex in range(len(str)):
		tailChar = str[tailIndex]
		
		#Skip all the characters not in arr
		if countMap.keyExists(tailChar) == False:
			continue
		
		tailCount = countMap.getValueOf(tailChar)
		if tailCount == 0:
			uniqueCounter = uniqueCounter + 1

		countMap.setValueOf(tailChar, tailCount + 1)

		# push head forward
		while uniqueCounter == len(arr):
			tempLength = tailIndex - headIndex + 1
			if tempLength == len(arr):
				#return a substring of str from
				# headIndex to tailIndex(inclusive)
				return str[headIndex:tailIndex+1]

			if result == "" or tempLength < len(result):
				#return a substring of str from
				# headIndex to tailIndex(inclusive)
				result = str[headIndex:tailIndex+1]

			headChar = str[headIndex]

			if countMap.keyExists(headChar):
				headCount = countMap.getValueOf(headChar) -1
			if headCount == 0:
				uniqueCounter = uniqueCounter - 1
			countMap.setValueOf(headChar, headCount)

			headIndex = headIndex + 1

	return result
class Map:
	
	HashTable = {}
	
	def getValueOf(self,char):
		return self.HashTable[char]
	
	def setValueOf(self,char,int):
		self.HashTable[char] = int

	def keyExists(self,char):
		return char in self.HashTable.keys()

if __name__ == "__main__":
	arr = array.array('u',['a','b','c'])
	str = "abdaaabanc"
	
	print(getShortestUniqueSubstring(arr,str))
