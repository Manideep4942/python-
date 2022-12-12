thislist=["apple","banana","cherry"]
print(thislist[1])#note the firtst index is 0
#if you give negative index it will come form the reverse...
#ex shown by using the thislist again
print(thislist[-1])
"""
THE RANGE OF THE INDEX USED IN PYTHON
"""
thislist2=["banana","apple","orange","kiwi","watermelon","orange"]
print(thislist2[:4])#it will return the items form index 0 to 4

thislist3=["banana","apple","orange","kiwi","watermelon","orange"]
print(thislist2[2:])# it will return the items from index 2 to end of list

"""
The range of the negative index....
"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

"""
check if item exists 
to determine if a specified itmes is present in al ist use the 'in' :keyword
"""
thislist4=["apple","banana","cherry"]
if "apple" in thislist:
    print("yes , apple is in the fruits list..")
