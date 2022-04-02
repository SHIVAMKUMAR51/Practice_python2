#STRING METHODS
#capitalize()-converts the first character to upper case
abc="hi!, my name is Shivam."
i=abc.capitalize()
print(i)

#casefold()-converts string into lower case
abc="HI,everyone"
i=abc.casefold()
print(i)

#center()-returns a centered string
a="abcdefghi"
x=a.center(100)
print(x)

#count()-returns the number of times a specified value occurs in a string
txt="I like python, python is my favourite language."
i=txt.count("python")
print(i)

#encode()-returns an encoded version of the string
txt="my name is Shivam!"
i=txt.encode()
print(i)

#endswith()-returns true if the string ends with the specified value
txt="hello, welcome to the world of python"
i=txt.endswith(".")
print(i)

#expandtabs()-set the tab size of the string
a="h\te\tllo"
i=a.expandtabs(5)
print(i)

#find()-searches the string for a specified value amd returns the position of where it was found
q="hey, I am learning from mycaptain."
i=q.find("I")
print(i)

#format()-formats specified values in string
txt = "For only {price:.2f} dollars!"
print(txt.format (price=49))

#join()-converts the elements of an iterable into string
myTuple = ("John", "Peter", "Vicky")
i = " & ".join(myTuple)
print(i)

#translate()-returns a translated string
mydict = {83:  85}
txt = "Hello Sam!"
print(txt.translate(mydict))