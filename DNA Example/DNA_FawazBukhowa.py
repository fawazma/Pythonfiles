#This is the find function
#returns the value of the index

def find(string, substring, start, end):
	if substring in string[start:end+1]: #substring is checked in string slice using in operator.
                                           #Slice values passed as parameters to function
		return string.index(substring) #returns index of substring where found


#This is the multi_find function
#returns string of indices where substring occurs in string
	
def multi_find(string, substring, start, end):
	indices=[] #indices will be appended to this declared list

	new_string=string[:end+1] #new string slices provided string using the value in the 'end' variable
	
	for i, _ in enumerate(new_string, start): #for loop traverses the new string.
                                                  #enumerate() method enumerates the indices of new_string.
                                                  #Argument 'start' tells enumerate where to start

		if new_string[i:i+len(substring)]==substring: #checks if the combined characters of substring are in new_string
			indices.append(i)               #appends index of first character of substring to indices[]
	return str(indices).strip('[]')                 #returns indices as string



#This function returns True if substring is found in find and multi_find functions as well as index or indices found respectively
#Function returns false where substring is not found

def substring_match(sequence, subseq, start, end):
	find_result=find(sequence, subseq, start, end) #result of find function is stored in find_result variable
	multi_find_result=multi_find(sequence, subseq, start, end) #result of multi_find function is stored in multi_find_result variable
	if find_result>0 and multi_find_result!='': #checks the values of variables find_result and multi_find_result to determine if substring has been found
		print (True)
		print ('Substring found in find function. Index -> ', find_result)
		print ('Substring found in multi_find function. Indices -> ', multi_find_result)
	else:
		print (False)
		print ('Substring not found')

sequence = input("Enter the DNA sequence within quotation marks: ")
subseq = input("Enter the DNA base within quotation marks: ")
start=int(input("Enter search index start point. No quotation marks needed: "))
end = int(input("Enter search index end point. No quotation marks needed: "))

print ("Find function result:")
print (find(sequence, subseq, start, end))

print ("Multi_find function result:")
print (multi_find(sequence, subseq, start, end))
substring_match(sequence, subseq, start, end)
