#Access values of dictionary inside a list
l1=[1,2,3,4,5,{"k1":"SHIVAM","k2":"CHAMP"}]
print(l1[5])

#Access value of list inside dictionary
my_dict={"m1":"20","m2":"[6,7,8,9,0]","m3":"9807"}
i=my_dict.get("m2")
print(i)