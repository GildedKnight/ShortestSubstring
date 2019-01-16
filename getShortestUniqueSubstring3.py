import array
import time

# Function to check if all the characters in the array are present in the substring
def found(arr,substr):
	result = True
	for char in arr:
		if char not in substr:
			result = False
	return result
	
def getShortestUniqueSubstring(arr,str):
	substr = ""		#Variable to hold the current substring being checked
	smallest = ""		# Variable to stor the smallest substring found so far
	searchSpace = str	# The string over which to search for the beginning of matching substring found
	
	# If length of string is less than length of array, there is no way the string can contain all the characters of array
	if len(str) < len(arr):
		return ""

	# If the array is empty, return empty string
	if len(arr) == 0:
		return ""
	
	# If the array contains only one character, use the find method to find the index where it occurs in string and return the string
	if len(arr) == 1:
		index = str.find(arr[0])
		return str[index: index + 1]

	# For each character in the string
	for chars in str:
		
		substr += chars				# Add the character to the substring being checked
		result = found(arr, substr)		# Determine if the resulting substring contains all the characters
		
		# Check if matching substring or its substring can be the new smallest substring by removing one character from left of substring in each pass
		while result == True:

			# If the length of matching substring is equal to the length of array, return this substring
			if len(substr) == len(arr):
				return substr

			# If no smallest string has been found so far, then the currently found matching substring is the smallest
			if len(smallest) == 0:
				smallest = substr
			
			# If the length of the smallest string found so far is same or greater than the length of currently found matching substring, then the currently found matching substring is the new smallest
			elif len(smallest) >= len(substr):
				smallest = substr
			
			# Modify the string to be searched next time for the presence of matching substring and reduce the size of currently found substring to check for smaller match
			index =  searchSpace.find(substr)
			substr = substr[1:]
			searchSpace = searchSpace[index + 1:]
			result = found(arr, substr)

	return smallest

if __name__ == "__main__":
	#arr = array.array('u', ['a', 'b', 'd', 'e', 'f','g','h','c','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$'])
	arr = array.array('u',[])
	#str = ("adklmnjtwb" + "cefghiopqr" + "suvxyz!#@%" + "#ag$%tlm*c" + "1234567890") * 10
	str = "a"
	start_time = time.time()
	print(getShortestUniqueSubstring(arr, str))
	print("--- %s seconds ---" % (time.time() - start_time))
