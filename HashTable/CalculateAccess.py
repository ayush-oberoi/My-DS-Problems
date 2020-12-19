MyDictionary = {
	'Name' : 'Ayush',
	'Interest' : 'Microsoft Azure Cloud',
	'College' : 'Gcoej',
}

print(MyDictionary['Name'])  			#Searching O(1)
MyDictionary['Age']=22       			#Insert O(1)
MyDictionary.pop('Age')      			#Delete  O(1)
MyDictionary['Name'] = 'Ayush Oberoi' #mModify O(1)
print(MyDictionary)