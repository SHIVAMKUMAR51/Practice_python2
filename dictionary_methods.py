#METHODS OF DICTIONARY

#clear()-Removes all the elements from dictionary
l1={"k1":"1","k2":"2","k3":"3"}
l1.clear()
print(l1)


#copy()-Returns a copy of the dictionary
l1={"k1":"1","k2":"2","k3":"3"}
i=l1.copy()
print(i)

#fromkeys()-Returns a dictionary with a specified keys and value
#creates a dictionary with 3 
i=('k1','k2','k3')
j=7
l1=dict.fromkeys(i,j)
print(l1)

#get()-Returns the value of the specified key
l1={"k1":"1","k2":"2","k3":"3"}
i=l1.get("k2")
print(i)

#items()-Returns a list containing tuple for each key-value pairs
l1={"k1":"1","k2":"2","k3":"3"}
i=l1.items()
print(i)

#keys()-Returns a list containing dictionary's keys
l1={"k1":"1","k2":"2","k3":"3"}
i=l1.keys()
print(i)

#pop()-Removes the element with a specified key
l1={"k1":"1","k2":"2","k3":"3"}
l1.pop("k2")
print(l1)

#popitem()-Returns the last inserted key-value pair
l1={"k1":"1","k2":"2","k3":"3"}
l1.popitem()
print(l1)

#setdefault()-Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
l1={"k1":"1","k2":"2","k3":"3"}
l1.setdefault("k4", "SHIVAM")
print(l1)

#update()-Updates the dictionary with the specified key-value pairs
l1={"k1":"1","k2":"2","k3":"3"}
l1.update({"k5":"tree"})
print(l1)

#values()-Returns a list of all values in the dictionary
l1={"k1":"1","k2":"2","k3":"3"}
i=l1.values()
print(i)